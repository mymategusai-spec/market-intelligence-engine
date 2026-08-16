"""Financial modelling.

The rule under test is the one the master prompt states most emphatically: purchase price
is never the investment. These tests make sure the yield the engine reports is the yield
the owners would actually experience.
"""

import unittest

from core.financial.model import CapitalStack, OperatingCosts, OwnerUse, compute
from core.models.common import Confidence, Money


def stack(**overrides):
    defaults = dict(
        purchase_price=Money.of(300_000, "AUD"),
        acquisition_costs=Money.of(15_000, "AUD"),
        taxes=Money.of(12_000, "AUD"),
        legal=Money.of(8_000, "AUD"),
        due_diligence=Money.of(5_000, "AUD"),
        renovation=Money.of(150_000, "AUD"),
        furnishing=Money.of(30_000, "AUD"),
        licensing_compliance=Money.of(10_000, "AUD"),
        working_capital=Money.of(20_000, "AUD"),
        contingency=Money.of(40_000, "AUD"),
    )
    defaults.update(overrides)
    return CapitalStack(**defaults)


class TestCapitalStack(unittest.TestCase):
    def test_total_project_cost_sums_every_component(self):
        self.assertEqual(stack().total_project_cost().amount, 590_000)

    def test_cost_above_purchase_price_is_reported(self):
        self.assertEqual(stack().cost_above_purchase_price().amount, 290_000)

    def test_missing_components_are_listed(self):
        partial = CapitalStack(purchase_price=Money.of(300_000, "AUD"))
        missing = partial.missing_components()
        self.assertIn("renovation", missing)
        self.assertIn("contingency", missing)
        self.assertIn("licensing_compliance", missing)

    def test_estimate_ranges_survive_into_total(self):
        with_estimate = stack(renovation=Money.estimate(100_000, 250_000, "AUD"))
        total = with_estimate.total_project_cost()
        self.assertTrue(total.is_estimate)
        # Firm components total 440,000; renovation contributes 100,000-250,000.
        self.assertEqual(total.range_low, 540_000)
        self.assertEqual(total.range_high, 690_000)
        self.assertEqual(total.amount, 615_000)


class TestCompute(unittest.TestCase):
    def test_yield_on_total_project_cost_is_lower_than_on_purchase_price(self):
        """The gap between these two numbers is where optimistic arithmetic hides."""
        result = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(90_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown(
                "AUD",
                management=Money.of(18_000, "AUD"),
                cleaning=Money.of(9_000, "AUD"),
                utilities=Money.of(8_000, "AUD"),
            ),
        )
        self.assertEqual(result.noi.amount, 55_000)
        self.assertAlmostEqual(result.yield_on_purchase_price_percent, 55_000 / 300_000 * 100, places=4)
        self.assertAlmostEqual(result.yield_on_total_project_cost_percent, 55_000 / 590_000 * 100, places=4)
        self.assertGreater(result.yield_on_purchase_price_percent, result.yield_on_total_project_cost_percent)
        self.assertAlmostEqual(result.yield_gap_percentage_points, 18.3333 - 9.3220, places=2)

    def test_owner_use_reduces_revenue(self):
        without = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(90_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
        )
        with_use = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(90_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
            owner_use=OwnerUse(
                weeks_per_year=3,
                season="peak",
                revenue_foregone=Money.of(21_000, "AUD"),
            ),
        )
        self.assertEqual(without.noi.amount - with_use.noi.amount, 21_000)
        self.assertTrue(any("owner use" in c for c in with_use.caveats))

    def test_separate_quarters_avoid_the_revenue_hit(self):
        result = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(90_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
            owner_use=OwnerUse(
                weeks_per_year=3,
                season="peak",
                revenue_foregone=Money.of(21_000, "AUD"),
                offset_by_separate_quarters=True,
            ),
        )
        self.assertEqual(result.noi.amount, 80_000)

    def test_incomplete_capital_stack_raises_a_caveat(self):
        result = compute(
            capital=CapitalStack(purchase_price=Money.of(300_000, "AUD")),
            gross_annual_revenue=Money.of(50_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
        )
        self.assertTrue(any("understated" in c for c in result.caveats))

    def test_missing_contingency_is_called_out(self):
        result = compute(
            capital=stack(contingency=None),
            gross_annual_revenue=Money.of(50_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
        )
        self.assertTrue(any("contingency" in c for c in result.caveats))

    def test_currency_mismatch_is_refused(self):
        with self.assertRaises(ValueError):
            compute(
                capital=stack(),
                gross_annual_revenue=Money.of(9_000_000, "JPY"),
                operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
            )

    def test_breakeven_occupancy_is_computed(self):
        result = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(100_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(40_000, "AUD")),
        )
        self.assertAlmostEqual(result.breakeven_occupancy_percent, 40.0, places=4)

    def test_estimated_inputs_force_low_confidence(self):
        result = compute(
            capital=stack(renovation=Money.estimate(100_000, 250_000, "AUD")),
            gross_annual_revenue=Money.of(90_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(10_000, "AUD")),
            input_confidence=[Confidence.HIGH],
        )
        self.assertEqual(result.confidence, Confidence.LOW)

    def test_negative_noi_is_reported_not_hidden(self):
        result = compute(
            capital=stack(),
            gross_annual_revenue=Money.of(20_000, "AUD"),
            operating_costs=OperatingCosts.from_breakdown("AUD", management=Money.of(45_000, "AUD")),
        )
        self.assertEqual(result.noi.amount, -25_000)
        self.assertLess(result.yield_on_total_project_cost_percent, 0)


if __name__ == "__main__":
    unittest.main()
