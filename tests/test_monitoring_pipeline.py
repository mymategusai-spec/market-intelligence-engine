"""The monitoring cycle.

Two invariants: history is only ever appended to, and a listing disappearing is recorded
as removed with cause unknown - never inferred as a sale.
"""

import os
import sys
import unittest
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.monitoring.monitor import latest_state, run_cycle  # noqa: E402


def hist(property_id, rows):
    return {property_id: [
        {"record_type": "listing_observation", "property_id": property_id,
         "observed_on": d, "asking_price_jpy": p, "listing_status": s}
        for d, p, s in rows
    ]}


class TestMonitoringCycle(unittest.TestCase):
    def test_new_listing_produces_listed_event(self):
        events, obs = run_cycle(
            {"P1": {"asking_price_amount": 10_000_000}}, date(2026, 8, 20), history={})
        self.assertEqual([e.event_type for e in events], ["asset_listed"])
        self.assertEqual(len(obs), 1)

    def test_price_reduction_detected_against_history(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active")])
        events, _ = run_cycle(
            {"P1": {"asking_price_amount": 8_000_000}}, date(2026, 8, 20), history=history)
        self.assertEqual(events[0].event_type, "asset_price_reduced")
        self.assertAlmostEqual(events[0].change_percent, -20.0)
        self.assertEqual(events[0].materiality, "major")

    def test_unchanged_price_produces_no_event(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active")])
        events, obs = run_cycle(
            {"P1": {"asking_price_amount": 10_000_000}}, date(2026, 8, 20), history=history)
        self.assertEqual(events, [])
        self.assertEqual(len(obs), 1, "An observation is still recorded even with no change")

    def test_disappearance_is_removal_not_sale(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active")])
        events, obs = run_cycle({}, date(2026, 8, 20), history=history)
        self.assertEqual(events[0].event_type, "asset_removed")
        self.assertIn("Cause unknown", events[0].description)
        self.assertEqual(obs[0]["listing_status"], "removed")
        self.assertNotIn("sold", events[0].event_type)

    def test_removal_does_not_refire_on_later_cycles(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active"),
                              ("2026-06-01", None, "removed")])
        events, obs = run_cycle({}, date(2026, 8, 20), history=history)
        self.assertEqual(events, [])
        self.assertEqual(obs, [])

    def test_relisting_after_removal_is_detected(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active"),
                              ("2026-06-01", None, "removed")])
        events, _ = run_cycle(
            {"P1": {"asking_price_amount": 9_000_000}}, date(2026, 8, 20), history=history)
        self.assertTrue(events, "A property reappearing must produce an event")

    def test_latest_state_uses_most_recent_observation(self):
        rows = hist("P1", [("2026-01-01", 10_000_000, "active"),
                           ("2026-06-01", 9_000_000, "active")])["P1"]
        self.assertEqual(latest_state(rows)["asking_price_amount"], 9_000_000)

    def test_multiple_properties_processed_independently(self):
        history = hist("P1", [("2026-01-01", 10_000_000, "active")])
        history.update(hist("P2", [("2026-01-01", 20_000_000, "active")]))
        events, obs = run_cycle(
            {"P1": {"asking_price_amount": 9_000_000},
             "P2": {"asking_price_amount": 20_000_000}},
            date(2026, 8, 20), history=history)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].subject_id, "P1")
        self.assertEqual(len(obs), 2)


if __name__ == "__main__":
    unittest.main()
