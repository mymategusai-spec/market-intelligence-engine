"""Money, FX and confidence propagation.

Currency handling is the most dangerous quiet failure mode in this project: the owners
think in AUD, the market prices in JPY, and a conversion without its rate date silently
rots. These tests exist to make that failure loud.
"""

import unittest
from datetime import date

from core.models.common import (
    ClaimType,
    Confidence,
    FxConversion,
    Money,
    Provenance,
    sum_money,
    weakest,
)


class TestMoney(unittest.TestCase):
    def test_conversion_requires_rate_and_date(self):
        with self.assertRaises(ValueError):
            Money(amount=100.0, currency="JPY", converted_amount=1.0, converted_currency="AUD")

    def test_conversion_records_rate_and_date(self):
        fx = FxConversion("JPY", "AUD", rate=0.0102, rate_date=date(2026, 8, 16))
        jpy = Money.of(30_000_000, "JPY").converted_to(fx)
        self.assertAlmostEqual(jpy.converted_amount, 306_000.0, places=2)
        self.assertEqual(jpy.amount, 30_000_000)
        self.assertEqual(jpy.fx.rate_date, date(2026, 8, 16))

    def test_original_amount_is_never_lost(self):
        fx = FxConversion("JPY", "AUD", rate=0.0102, rate_date=date(2026, 8, 16))
        converted = Money.of(30_000_000, "JPY").converted_to(fx)
        self.assertEqual(converted.in_currency("JPY"), 30_000_000)
        self.assertAlmostEqual(converted.in_currency("AUD"), 306_000.0, places=2)

    def test_unavailable_conversion_raises_rather_than_guessing(self):
        with self.assertRaises(ValueError):
            Money.of(30_000_000, "JPY").in_currency("AUD")

    def test_mismatched_fx_direction_rejected(self):
        fx = FxConversion("AUD", "JPY", rate=98.0, rate_date=date(2026, 8, 16))
        with self.assertRaises(ValueError):
            Money.of(30_000_000, "JPY").converted_to(fx)

    def test_cannot_add_different_currencies(self):
        with self.assertRaises(ValueError):
            Money.of(100, "AUD") + Money.of(100, "JPY")

    def test_addition_preserves_estimate_ranges(self):
        firm = Money.of(400_000, "AUD")
        rough = Money.estimate(80_000, 160_000, "AUD")
        total = firm + rough
        self.assertTrue(total.is_estimate)
        self.assertEqual(total.range_low, 480_000)
        self.assertEqual(total.range_high, 560_000)
        self.assertEqual(total.amount, 520_000)

    def test_estimate_midpoint_and_flagging(self):
        estimate = Money.estimate(100_000, 200_000, "AUD")
        self.assertEqual(estimate.amount, 150_000)
        self.assertTrue(estimate.is_estimate)

    def test_inverted_range_rejected(self):
        with self.assertRaises(ValueError):
            Money(amount=1.0, currency="AUD", range_low=10.0, range_high=1.0)

    def test_sum_money_skips_missing_components(self):
        total = sum_money(Money.of(10, "AUD"), None, Money.of(5, "AUD"), currency="AUD")
        self.assertEqual(total.amount, 15)

    def test_negative_fx_rate_rejected(self):
        with self.assertRaises(ValueError):
            FxConversion("JPY", "AUD", rate=-0.01, rate_date=date(2026, 8, 16))


class TestConfidence(unittest.TestCase):
    def test_weakest_wins(self):
        self.assertEqual(weakest(Confidence.HIGH, Confidence.LOW), Confidence.LOW)
        self.assertEqual(weakest(Confidence.HIGH, Confidence.MEDIUM), Confidence.MEDIUM)
        self.assertEqual(weakest(Confidence.HIGH, Confidence.HIGH), Confidence.HIGH)

    def test_unknown_is_weakest_of_all(self):
        self.assertEqual(weakest(Confidence.HIGH, Confidence.UNKNOWN), Confidence.UNKNOWN)

    def test_empty_is_unknown(self):
        self.assertEqual(weakest(), Confidence.UNKNOWN)


class TestProvenance(unittest.TestCase):
    def test_source_id_is_required(self):
        with self.assertRaises(ValueError):
            Provenance(
                source_id="",
                retrieved_at=date(2026, 8, 16),
                claim_type=ClaimType.FACT,
                confidence=Confidence.HIGH,
            )

    def test_valid_provenance_constructs(self):
        provenance = Provenance(
            source_id="JP-MLIT-CHIKA",
            retrieved_at=date(2026, 8, 16),
            claim_type=ClaimType.FACT,
            confidence=Confidence.HIGH,
        )
        self.assertEqual(provenance.claim_type, ClaimType.FACT)


if __name__ == "__main__":
    unittest.main()
