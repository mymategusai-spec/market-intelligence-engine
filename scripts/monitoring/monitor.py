#!/usr/bin/env python3
"""Monitoring pipeline: snapshot in, events out.

Deliberately the simplest thing that works end to end. A simple pipeline that reliably
collects beats a sophisticated one that never runs (master prompt section 54).

    retrieve -> normalise -> diff vs last snapshot -> event -> append history

Collection itself is separate: this module operates on already-retrieved, normalised
records so it can be tested without network access and can never be the thing that
breaches a site's terms.

    python3 scripts/monitoring/monitor.py --status
    python3 scripts/monitoring/monitor.py --run

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from core.monitoring.diff import DerivedEvent, diff_states  # noqa: E402
from core.provenance.registry import SourceRegistry  # noqa: E402

LISTINGS_DIR = os.path.join(REPO_ROOT, "data", "property-listings")
HISTORY = os.path.join(LISTINGS_DIR, "listing-history.jsonl")
EVENTS = os.path.join(LISTINGS_DIR, "listing-events.jsonl")


def load_history():
    """Read the append-only history into {property_id: [observations]}."""
    by_property = {}
    if not os.path.exists(HISTORY):
        return by_property
    with open(HISTORY, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("record_type") != "listing_observation":
                continue
            by_property.setdefault(row["property_id"], []).append(row)
    for rows in by_property.values():
        rows.sort(key=lambda r: r["observed_on"])
    return by_property


def latest_state(observations):
    if not observations:
        return None
    row = observations[-1]
    return {
        "asking_price_amount": row.get("asking_price_jpy"),
        "listing_status": row.get("listing_status"),
    }


def run_cycle(current_records, observed_on, history=None):
    """Diff a freshly retrieved record set against history and derive events.

    ``current_records`` maps property_id -> normalised state. A property present in
    history but absent from the current set is reported as *removed, cause unknown* —
    never inferred as sold.
    """
    history = history if history is not None else load_history()
    events = []
    new_observations = []

    for property_id, state in current_records.items():
        observations = history.get(property_id)
        previous = latest_state(observations)

        if observations and observations[-1].get("listing_status") == "removed":
            # Back on the market after being recorded as gone. Neither the "new listing"
            # nor the "price change" branch of diff_states catches this, because the
            # previous observation exists but carries no price. Relisting is explicitly
            # a tracked event type, so it is emitted here.
            prior_price = next(
                (o.get("asking_price_jpy") for o in reversed(observations)
                 if o.get("asking_price_jpy") is not None), None)
            new_price = state.get("asking_price_amount")
            change = None
            if isinstance(prior_price, (int, float)) and isinstance(new_price, (int, float)) and prior_price:
                change = (new_price - prior_price) / prior_price * 100.0
            events.append(DerivedEvent(
                event_type="asset_relisted",
                subject_id=property_id,
                detected_at=observed_on,
                from_value=prior_price,
                to_value=new_price,
                change_percent=change,
                materiality="significant",
                description=(
                    "Back on the market after being recorded as removed. A relisting "
                    "means the earlier disappearance was NOT a sale - useful evidence "
                    "against reading absence as a transaction."
                ),
            ))
        else:
            events.extend(diff_states(property_id, previous, state, observed_on))
        new_observations.append({
            "record_type": "listing_observation",
            "property_id": property_id,
            "observed_on": observed_on.isoformat(),
            "asking_price_jpy": state.get("asking_price_amount"),
            "listing_status": state.get("listing_status", "active"),
            "source_id": state.get("source_id", "UNKNOWN"),
        })

    for property_id, observations in history.items():
        if property_id in current_records:
            continue
        last = observations[-1]
        if last.get("listing_status") == "removed":
            continue  # already recorded as gone; do not re-fire
        events.extend(diff_states(property_id, latest_state(observations), None, observed_on))
        new_observations.append({
            "record_type": "listing_observation",
            "property_id": property_id,
            "observed_on": observed_on.isoformat(),
            "asking_price_jpy": None,
            "listing_status": "removed",
            "source_id": last.get("source_id", "UNKNOWN"),
            "note": "Not observed in this cycle. Cause unknown - sold, withdrawn or delisted.",
        })

    return events, new_observations


def append_history(observations):
    """Append only. This function never rewrites or truncates the file."""
    with open(HISTORY, "a", encoding="utf-8") as handle:
        for row in observations:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_events(events):
    with open(EVENTS, "a", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps({
                "record_type": "event",
                "property_id": event.subject_id,
                "event_type": event.event_type,
                "detected_at": event.detected_at.isoformat(),
                "from_jpy": event.from_value,
                "to_jpy": event.to_value,
                "change_percent": event.change_percent,
                "materiality": event.materiality,
                "description": event.description,
            }, ensure_ascii=False) + "\n")


def status():
    history = load_history()
    total_obs = sum(len(v) for v in history.values())
    multi = {k: v for k, v in history.items() if len(v) > 1}
    print("Monitoring status")
    print("=" * 54)
    print("Tracked properties        : %d" % len(history))
    print("Total observations        : %d" % total_obs)
    print("Properties seen >1 time   : %d" % len(multi))
    if os.path.exists(EVENTS):
        with open(EVENTS, "r", encoding="utf-8") as handle:
            events = [json.loads(l) for l in handle if l.strip()]
        print("Events recorded           : %d" % len(events))
        for event in events[:10]:
            print("  %-28s %-24s %s%%" % (
                (event.get("name") or event["property_id"])[:27],
                event["event_type"],
                event.get("change_percent")))
    print()
    registry_path = os.path.join(REPO_ROOT, "data", "reference", "source-register.json")
    if os.path.exists(registry_path):
        registry = SourceRegistry.load(registry_path)
        print("Sources permitted for automation: %d of %d"
              % (len(registry.crawlable_sources()), len(registry.sources)))
        unverified = registry.unverified_access()
        if unverified:
            print("NOT cleared for automation (robots/terms unchecked):")
            for source in unverified:
                print("  - %s" % source.source_id)
    else:
        print("No machine-readable source register yet; see SOURCES.md.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--run", action="store_true", help="Run a cycle over the committed current set")
    args = parser.parse_args()

    if args.run:
        path = os.path.join(LISTINGS_DIR, "yuzawa-apartments-2026-08-20.json")
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        current = {
            row["property_id"]: {
                "asking_price_amount": row["asking_price_jpy"],
                "listing_status": "active",
                "source_id": row["source_id"],
            }
            for row in payload["listings"]
        }
        events, observations = run_cycle(current, date.today())
        print("Cycle complete: %d events, %d observations." % (len(events), len(observations)))
        print("Dry run - nothing written. Wire append_history/append_events into a scheduled job.")
        for event in events[:10]:
            print("  %s %s %s" % (event.subject_id, event.event_type, event.change_percent))
        return

    status()


if __name__ == "__main__":
    main()
