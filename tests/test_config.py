"""The committed configuration must be internally consistent.

Config is where subjective judgement lives, which makes it the easiest place for a silent
error to change a ranking. These tests check the real files in `config/`, not fixtures.
"""

import json
import os
import unittest

from core.config import (
    load_catalyst_status_weights,
    load_json,
    load_weight_sets,
    default_weight_set,
    weighted_pipeline_total,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE_CONFIG = os.path.join(REPO_ROOT, "config", "core", "engine.json")
DOMAIN_CONFIG_DIR = os.path.join(REPO_ROOT, "config", "domains", "japan_ski_property")
WEIGHTS_CONFIG = os.path.join(DOMAIN_CONFIG_DIR, "weights.json")
COMPONENTS_CONFIG = os.path.join(DOMAIN_CONFIG_DIR, "scoring_components.json")
FILTERS_CONFIG = os.path.join(DOMAIN_CONFIG_DIR, "filters.json")


class TestWeightSets(unittest.TestCase):
    def setUp(self):
        self.weight_sets = load_weight_sets(WEIGHTS_CONFIG)
        self.components = load_json(COMPONENTS_CONFIG)["components"]

    def test_all_weight_sets_load(self):
        self.assertIn("balanced", self.weight_sets)
        self.assertGreaterEqual(len(self.weight_sets), 3)

    def test_default_weight_set_exists(self):
        self.assertEqual(default_weight_set(WEIGHTS_CONFIG).weight_set_id, "balanced")

    def test_every_weighted_component_is_defined(self):
        """A weight on an undefined component would silently do nothing."""
        for name, weight_set in self.weight_sets.items():
            for component_key in weight_set.weights:
                with self.subTest(weight_set=name, component=component_key):
                    self.assertIn(
                        component_key, self.components,
                        "%s weights unknown component %r" % (name, component_key),
                    )

    def test_every_defined_component_is_weighted_in_every_set(self):
        """A component defined but unweighted would be scored and then ignored."""
        for name, weight_set in self.weight_sets.items():
            missing = set(self.components) - set(weight_set.weights)
            with self.subTest(weight_set=name):
                self.assertEqual(
                    set(), missing,
                    "%s omits components: %s" % (name, sorted(missing)),
                )

    def test_gating_components_are_defined_and_weighted(self):
        gating = load_json(COMPONENTS_CONFIG)["gating_components"]
        for key in gating:
            self.assertIn(key, self.components)
            for name, weight_set in self.weight_sets.items():
                with self.subTest(weight_set=name, component=key):
                    self.assertGreater(weight_set.weights[key], 0.0)

    def test_weight_sets_are_actually_different(self):
        """Distinct profiles must produce distinct rankings, or they are decoration."""
        pure = self.weight_sets["pure_investment"].weights
        lifestyle = self.weight_sets["lifestyle"].weights
        self.assertGreater(lifestyle["town_vibe"], pure["town_vibe"])
        self.assertGreater(pure["rental_demand"], lifestyle["rental_demand"])

    def test_emerging_upside_does_not_underweight_risk(self):
        """The optimistic profile must not be allowed to reward optimism.

        An emerging-market bias with a low risk weight would systematically flatter
        exactly the markets most likely to be cheap for good reason.
        """
        emerging = self.weight_sets["emerging_upside"].weights
        balanced = self.weight_sets["balanced"].weights
        self.assertGreaterEqual(emerging["risk"], balanced["risk"])

    def test_owner_preference_is_flagged_as_unset(self):
        """Until the owners state a preference, no profile may be presented as theirs."""
        document = load_json(WEIGHTS_CONFIG, strip_comments=False)
        self.assertFalse(document["owner_preference_status"]["set_by_owner"])


class TestEngineConfig(unittest.TestCase):
    def setUp(self):
        self.status_weights = load_catalyst_status_weights(ENGINE_CONFIG)

    def test_rumour_contributes_nothing(self):
        self.assertEqual(self.status_weights["rumoured"], 0.0)
        self.assertEqual(self.status_weights["cancelled"], 0.0)

    def test_status_weights_increase_monotonically_along_the_ladder(self):
        ladder = [
            "rumoured", "proposed", "announced", "planning",
            "approved", "funded", "under_construction", "completed",
        ]
        values = [self.status_weights[s] for s in ladder]
        self.assertEqual(values, sorted(values), "Status weights must not decrease up the ladder")

    def test_proposal_is_weighted_far_below_construction(self):
        self.assertLess(self.status_weights["proposed"], self.status_weights["under_construction"] / 4)

    def test_weighted_pipeline_discounts_by_status(self):
        pipeline = [
            {"rooms": 100, "status": "rumoured"},
            {"rooms": 100, "status": "under_construction"},
        ]
        total = weighted_pipeline_total(pipeline, self.status_weights)
        self.assertEqual(total, 95.0)
        self.assertLess(total, 200.0)

    def test_unknown_status_contributes_nothing(self):
        total = weighted_pipeline_total([{"rooms": 500, "status": "not_a_status"}], self.status_weights)
        self.assertEqual(total, 0.0)

    def test_candidate_sources_are_not_citable_by_config(self):
        document = load_json(ENGINE_CONFIG, strip_comments=False)
        self.assertFalse(document["citation_rules"]["candidate_sources_citable"])

    def test_collection_defaults_to_no_permission(self):
        document = load_json(ENGINE_CONFIG, strip_comments=False)
        ethics = document["collection_ethics"]
        self.assertTrue(ethics["require_robots_check_before_automation"])
        self.assertFalse(ethics["default_permission_when_unchecked"])


class TestFilters(unittest.TestCase):
    def setUp(self):
        self.filters = load_json(FILTERS_CONFIG)

    def test_price_tiers_are_contiguous_and_ordered(self):
        tiers = self.filters["price_tiers_aud"]
        for earlier, later in zip(tiers, tiers[1:]):
            self.assertEqual(earlier["max"], later["min"], "Gap or overlap between price tiers")

    def test_primary_currency_is_aud(self):
        self.assertEqual(self.filters["primary_currency"], "AUD")

    def test_lift_proximity_bands_match_the_brief(self):
        bands = {b["key"]: b for b in self.filters["lift_proximity_bands_minutes"]}
        self.assertEqual(bands["0_5"]["max_minutes"], 5)
        self.assertEqual(bands["5_10"]["max_minutes"], 10)
        self.assertEqual(bands["10_15"]["max_minutes"], 15)

    def test_no_assumed_optimal_guest_capacity(self):
        self.assertGreater(len(self.filters["guest_capacity_options"]), 3)

    def test_undetermined_thresholds_are_null_not_invented(self):
        """A threshold that needs real data must be null until that data exists."""
        signals = self.filters["opportunity_signals"]
        self.assertIsNone(signals["high_capacity_per_dollar_threshold"])

    def test_legal_operating_path_is_required_by_default(self):
        self.assertTrue(self.filters["default_hard_filters"]["require_legal_operating_path"])


class TestConfigFilesAreValidJson(unittest.TestCase):
    def test_all_config_files_parse(self):
        config_root = os.path.join(REPO_ROOT, "config")
        found = 0
        for dirpath, _dirnames, filenames in os.walk(config_root):
            for filename in filenames:
                if not filename.endswith(".json"):
                    continue
                found += 1
                path = os.path.join(dirpath, filename)
                with self.subTest(config=os.path.relpath(path, REPO_ROOT)):
                    with open(path, "r", encoding="utf-8") as handle:
                        json.load(handle)
        self.assertGreater(found, 0)


if __name__ == "__main__":
    unittest.main()
