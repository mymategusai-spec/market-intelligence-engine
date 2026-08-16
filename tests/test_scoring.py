"""Scoring behaviour.

The properties worth protecting: weights come from config, missing data is never
flattered into a middle value, confidence propagates pessimistically, and a disqualified
market is excluded rather than merely ranked last.
"""

import unittest

from core.models.common import Confidence
from core.scoring.engine import ScoreComponent, WeightSet, rank, score


def component(key, value, confidence=Confidence.HIGH):
    return ScoreComponent(
        component_key=key,
        label=key.replace("_", " ").title(),
        value=value,
        confidence=confidence,
        rationale="test rationale for %s" % key,
    )


WEIGHTS = WeightSet(
    weight_set_id="test_balanced",
    weights={"affordability": 2.0, "snow_reliability": 3.0, "town_vibe": 1.0},
)


class TestScoring(unittest.TestCase):
    def test_weighted_average_is_normalised_over_applied_weights(self):
        result = score(
            "market_a",
            [component("affordability", 8.0), component("snow_reliability", 6.0), component("town_vibe", 4.0)],
            WEIGHTS,
        )
        # (8*2 + 6*3 + 4*1) / 6 = 38/6
        self.assertAlmostEqual(result.total_score, 38.0 / 6.0, places=4)

    def test_missing_components_are_reported_not_defaulted(self):
        result = score("market_b", [component("affordability", 8.0)], WEIGHTS)
        self.assertEqual(result.total_score, 8.0)
        self.assertIn("snow_reliability", result.components_missing)
        self.assertIn("town_vibe", result.components_missing)

    def test_missing_components_reduce_confidence(self):
        """A partially scored market cannot be high confidence, however good its parts."""
        result = score("market_c", [component("affordability", 9.0, Confidence.HIGH)], WEIGHTS)
        self.assertEqual(result.overall_confidence, Confidence.MEDIUM)

    def test_confidence_propagates_pessimistically(self):
        result = score(
            "market_d",
            [
                component("affordability", 8.0, Confidence.HIGH),
                component("snow_reliability", 8.0, Confidence.LOW),
                component("town_vibe", 8.0, Confidence.HIGH),
            ],
            WEIGHTS,
        )
        self.assertEqual(result.overall_confidence, Confidence.LOW)

    def test_zero_weight_component_does_not_drag_confidence(self):
        weights = WeightSet(weight_set_id="focus", weights={"affordability": 1.0})
        result = score(
            "market_e",
            [
                component("affordability", 7.0, Confidence.HIGH),
                component("town_vibe", 2.0, Confidence.UNKNOWN),
            ],
            weights,
        )
        self.assertEqual(result.overall_confidence, Confidence.HIGH)
        self.assertEqual(result.total_score, 7.0)

    def test_changing_weights_changes_the_ranking(self):
        """The dashboard's whole premise: re-weighting must actually re-rank."""
        cheap_market = [component("affordability", 9.0), component("snow_reliability", 4.0)]
        snowy_market = [component("affordability", 3.0), component("snow_reliability", 9.0)]

        value_weights = WeightSet(weight_set_id="value", weights={"affordability": 5.0, "snow_reliability": 1.0})
        snow_weights = WeightSet(weight_set_id="snow", weights={"affordability": 1.0, "snow_reliability": 5.0})

        by_value = rank([score("cheap", cheap_market, value_weights), score("snowy", snowy_market, value_weights)])
        by_snow = rank([score("cheap", cheap_market, snow_weights), score("snowy", snowy_market, snow_weights)])

        self.assertEqual(by_value[0].subject_id, "cheap")
        self.assertEqual(by_snow[0].subject_id, "snowy")

    def test_disqualified_subject_is_excluded_from_ranking(self):
        """Illegality is not a low score. It is exclusion."""
        good = score("legal_market", [component("affordability", 5.0)], WEIGHTS)
        illegal = score(
            "illegal_market",
            [component("affordability", 10.0)],
            WEIGHTS,
            disqualified=True,
            disqualification_reason="Commercial accommodation licence unobtainable",
        )
        ranked = rank([good, illegal])
        self.assertEqual([r.subject_id for r in ranked], ["legal_market"])

    def test_disqualification_requires_a_reason(self):
        with self.assertRaises(ValueError):
            score("x", [component("affordability", 5.0)], WEIGHTS, disqualified=True)

    def test_component_requires_rationale(self):
        with self.assertRaises(ValueError):
            ScoreComponent(
                component_key="affordability",
                label="Affordability",
                value=5.0,
                confidence=Confidence.HIGH,
                rationale="   ",
            )

    def test_out_of_range_component_rejected(self):
        with self.assertRaises(ValueError):
            component("affordability", 11.0)

    def test_duplicate_components_rejected(self):
        with self.assertRaises(ValueError):
            score("x", [component("affordability", 5.0), component("affordability", 6.0)], WEIGHTS)

    def test_empty_weight_set_rejected(self):
        with self.assertRaises(ValueError):
            WeightSet(weight_set_id="empty", weights={})

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            WeightSet(weight_set_id="bad", weights={"affordability": -1.0})

    def test_explain_names_the_weight_set(self):
        result = score("market_f", [component("affordability", 8.0)], WEIGHTS)
        self.assertIn("test_balanced", result.explain())

    def test_explain_of_disqualified_states_the_reason(self):
        result = score(
            "market_g",
            [component("affordability", 8.0)],
            WEIGHTS,
            disqualified=True,
            disqualification_reason="Zoning prohibits lodging",
        )
        self.assertIn("Zoning prohibits lodging", result.explain())


if __name__ == "__main__":
    unittest.main()
