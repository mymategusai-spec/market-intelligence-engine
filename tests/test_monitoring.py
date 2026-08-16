"""Change detection and listing history.

Two invariants matter here: history is never destroyed, and the engine does not infer a
sale from a disappearance. A listing vanishing means "no longer observed" — anything
stronger is a guess wearing a fact's clothes.
"""

import unittest
from datetime import date

from core.monitoring.diff import ListingHistory, content_hash, diff_states


class TestDiff(unittest.TestCase):
    def test_new_listing_detected(self):
        events = diff_states("p1", None, {"asking_price_amount": 30_000_000}, date(2026, 8, 16))
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].event_type, "asset_listed")

    def test_disappearance_is_removal_not_sale(self):
        events = diff_states("p1", {"asking_price_amount": 30_000_000}, None, date(2026, 8, 16))
        self.assertEqual(events[0].event_type, "asset_removed")
        self.assertIn("Cause unknown", events[0].description)
        self.assertIn("retained", events[0].description)

    def test_price_reduction_detected_with_percentage(self):
        events = diff_states(
            "p1",
            {"asking_price_amount": 30_000_000},
            {"asking_price_amount": 24_000_000},
            date(2026, 8, 16),
        )
        self.assertEqual(events[0].event_type, "asset_price_reduced")
        self.assertAlmostEqual(events[0].change_percent, -20.0, places=4)
        self.assertEqual(events[0].materiality, "major")

    def test_price_increase_detected(self):
        events = diff_states(
            "p1",
            {"asking_price_amount": 20_000_000},
            {"asking_price_amount": 22_000_000},
            date(2026, 8, 16),
        )
        self.assertEqual(events[0].event_type, "asset_price_increased")
        self.assertAlmostEqual(events[0].change_percent, 10.0, places=4)

    def test_materiality_thresholds(self):
        cases = [(1.0, "minor"), (5.0, "notable"), (12.0, "significant"), (25.0, "major")]
        for pct, expected in cases:
            base = 1_000_000
            events = diff_states(
                "p1",
                {"asking_price_amount": base},
                {"asking_price_amount": base * (1 - pct / 100.0)},
                date(2026, 8, 16),
            )
            self.assertEqual(events[0].materiality, expected, "at %.1f%%" % pct)

    def test_no_change_produces_no_events(self):
        state = {"asking_price_amount": 30_000_000}
        self.assertEqual(diff_states("p1", state, dict(state), date(2026, 8, 16)), [])

    def test_watched_field_change_detected(self):
        events = diff_states(
            "p1",
            {"asking_price_amount": 100, "licence_status": "none"},
            {"asking_price_amount": 100, "licence_status": "ryokan"},
            date(2026, 8, 16),
            watch_fields=["licence_status"],
        )
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].field_name, "licence_status")

    def test_content_hash_is_order_independent(self):
        self.assertEqual(content_hash({"a": 1, "b": 2}), content_hash({"b": 2, "a": 1}))

    def test_content_hash_changes_with_content(self):
        self.assertNotEqual(content_hash({"a": 1}), content_hash({"a": 2}))


class TestListingHistory(unittest.TestCase):
    def _history(self):
        history = ListingHistory(subject_id="p1")
        history.append(date(2025, 1, 10), {"asking_price_amount": 30_000_000})
        history.append(date(2025, 6, 10), {"asking_price_amount": 27_000_000})
        history.append(date(2026, 1, 10), {"asking_price_amount": 24_000_000})
        return history

    def test_days_on_market(self):
        self.assertEqual(self._history().days_on_market(), 365)

    def test_price_trajectory_is_ordered(self):
        trajectory = self._history().price_trajectory()
        self.assertEqual([row["price"] for row in trajectory], [30_000_000, 27_000_000, 24_000_000])

    def test_total_price_change(self):
        self.assertAlmostEqual(self._history().total_price_change_percent(), -20.0, places=4)

    def test_out_of_order_appends_are_sorted(self):
        history = ListingHistory(subject_id="p1")
        history.append(date(2026, 1, 10), {"asking_price_amount": 24_000_000})
        history.append(date(2025, 1, 10), {"asking_price_amount": 30_000_000})
        self.assertEqual(history.first_seen, date(2025, 1, 10))
        self.assertEqual(history.last_seen, date(2026, 1, 10))

    def test_history_is_never_shortened_by_appending(self):
        history = self._history()
        before = len(history.observations)
        history.append(date(2026, 3, 1), {"asking_price_amount": 24_000_000})
        self.assertEqual(len(history.observations), before + 1)

    def test_single_observation_has_no_change_percentage(self):
        history = ListingHistory(subject_id="p1")
        history.append(date(2026, 1, 1), {"asking_price_amount": 1_000_000})
        self.assertIsNone(history.total_price_change_percent())


if __name__ == "__main__":
    unittest.main()
