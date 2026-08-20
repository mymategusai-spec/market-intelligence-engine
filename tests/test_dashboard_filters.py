"""Every dashboard filter the brief requires must map to a real field.

Cheaper to catch a missing field now than after a dashboard is built on it. This does
not test a UI - it tests that the DATA MODEL can answer the questions the dashboard is
supposed to ask.
"""

import json
import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#: Filters required by master prompt sections 37 and 57, mapped to where each is served.
REQUIRED_FILTERS = {
    "town": ("property", "market"),
    "neighbourhood": ("property", "neighbourhood"),
    "purchase_price": ("property", "asking_price_jpy"),
    "purchase_price_aud": ("property", "asking_price_aud"),
    "property_type": ("property", "property_type"),
    "bedrooms": ("property", "bedrooms"),
    "bathrooms": ("property", "bathrooms"),
    "guest_capacity": ("property", "practical_guest_capacity"),
    "licence": ("property", "licence_status"),
    "listing_age": ("property", "first_seen"),
    "source_confidence": ("property", "source_id"),
    "renovation_condition": ("property", "renovation_condition"),
    "total_project_cost": ("computed", "scripts/analysis/property_costs.py"),
    "renovation_cost": ("computed", "scripts/analysis/property_costs.py"),
    "price_reduction": ("computed", "data/property-listings/listing-events.jsonl"),
    "snow_score": ("score", "snow_reliability"),
    "town_vibe": ("score", "town_vibe"),
    "tourism_growth": ("score", "tourism_growth"),
    "property_growth": ("score", "property_price_momentum"),
    "infrastructure": ("score", "infrastructure"),
    "future_supply": ("score", "future_supply_balance"),
    "risk": ("score", "risk"),
    "management": ("score", "management_availability"),
    "town_access": ("score", "accessibility"),
    "projected_revenue": ("KNOWN_GAP", "no ADR obtained - see accommodation-market-evidence.md"),
    "distance_to_lifts": ("KNOWN_GAP", "not populated for any property"),
}


def load(path):
    with open(os.path.join(REPO_ROOT, path), "r", encoding="utf-8") as handle:
        return json.load(handle)


class TestDashboardFilters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.props = load("data/property-listings/candidate-properties-2026-08-20.json")["properties"]
        cls.components = load("config/domains/japan_ski_property/scoring_components.json")["components"]
        cls.filters = load("config/domains/japan_ski_property/filters.json")

    def test_property_filters_exist_on_at_least_one_record(self):
        """A filter field must appear on real data, not merely in a schema."""
        missing = []
        for label, (kind, field) in REQUIRED_FILTERS.items():
            if kind != "property":
                continue
            if not any(field in p for p in self.props):
                missing.append("%s -> %s" % (label, field))
        self.assertEqual([], missing, "Filter fields absent from all property records: %s" % missing)

    def test_score_filters_are_defined_components(self):
        missing = [
            "%s -> %s" % (label, field)
            for label, (kind, field) in REQUIRED_FILTERS.items()
            if kind == "score" and field not in self.components
        ]
        self.assertEqual([], missing, "Scorecard components missing: %s" % missing)

    def test_computed_filter_sources_exist(self):
        missing = [
            "%s -> %s" % (label, path)
            for label, (kind, path) in REQUIRED_FILTERS.items()
            if kind == "computed" and not os.path.exists(os.path.join(REPO_ROOT, path))
        ]
        self.assertEqual([], missing, "Computed filter sources missing: %s" % missing)

    def test_known_gaps_are_declared_not_silently_missing(self):
        """Gaps must be explicit. A silently absent filter looks like a working one."""
        gaps = {k: v[1] for k, v in REQUIRED_FILTERS.items() if v[0] == "KNOWN_GAP"}
        self.assertIn("projected_revenue", gaps)
        self.assertIn("distance_to_lifts", gaps)
        for label, reason in gaps.items():
            self.assertTrue(reason.strip(), "Gap %s must state a reason" % label)

    def test_price_tiers_cover_the_observed_range(self):
        """Filter bands must span real data, or properties fall outside every tier."""
        tiers = self.filters["price_tiers_aud"]
        prices = [p["asking_price_aud"] for p in self.props if p.get("asking_price_aud")]
        self.assertTrue(prices)
        lowest, highest = min(prices), max(prices)
        self.assertLessEqual(tiers[0]["min"], lowest)
        self.assertIsNone(tiers[-1]["max"], "Top tier must be open-ended to catch outliers")
        self.assertLess(tiers[-1]["min"], highest)

    def test_every_property_falls_into_exactly_one_price_tier(self):
        tiers = self.filters["price_tiers_aud"]
        for p in self.props:
            price = p.get("asking_price_aud")
            if price is None:
                continue
            matches = [
                t for t in tiers
                if t["min"] <= price and (t["max"] is None or price < t["max"])
            ]
            self.assertEqual(1, len(matches),
                             "%s at A$%s matched %d tiers" % (p["property_id"], price, len(matches)))

    def test_currency_is_aud_primary_with_jpy_retained(self):
        self.assertEqual("AUD", self.filters["primary_currency"])
        self.assertEqual("JPY", self.filters["secondary_currency"])
        both = [p for p in self.props if p.get("asking_price_aud") and p.get("asking_price_jpy")]
        self.assertTrue(both, "Records must carry both AUD and the JPY source value")


if __name__ == "__main__":
    unittest.main()
