"""Snapshot diffing and event derivation.

Snapshots record state; events record change. The engine keeps both, because a price of
X says far less than a fall from Y to X over N days — and it is the second that signals a
motivated seller.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Dict, List, Optional, Sequence


@dataclass(frozen=True)
class DerivedEvent:
    """A change detected between two snapshots."""

    event_type: str
    subject_id: str
    detected_at: date
    from_value: Any = None
    to_value: Any = None
    change_amount: Optional[float] = None
    change_percent: Optional[float] = None
    materiality: str = "minor"
    description: str = ""
    field_name: Optional[str] = None


def content_hash(state: Dict[str, Any]) -> str:
    """Stable hash of a snapshot's state, for cheap no-change detection."""
    canonical = json.dumps(state, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


#: Default materiality bands for a percentage price move, weakest first. Domains may
#: override: what counts as a significant move differs sharply between thin, illiquid
#: markets and liquid ones.
DEFAULT_MATERIALITY_BANDS = ((20.0, "major"), (10.0, "significant"), (3.0, "notable"))


def _materiality_for_price_change(
    change_percent: float,
    bands: Sequence[tuple] = DEFAULT_MATERIALITY_BANDS,
) -> str:
    """Classify a price move by rule rather than by mood.

    Defaults are deliberately conservative. In thin markets small nominal adjustments are
    routine, and treating every one as significant would drown the genuine signals.
    """
    magnitude = abs(change_percent)
    for threshold, label in bands:
        if magnitude >= threshold:
            return label
    return "minor"


def diff_states(
    subject_id: str,
    previous: Optional[Dict[str, Any]],
    current: Optional[Dict[str, Any]],
    detected_at: date,
    price_field: str = "asking_price_amount",
    watch_fields: Sequence[str] = (),
) -> List[DerivedEvent]:
    """Derive events from two consecutive snapshot states.

    Handles the three transitions that matter for a tracked asset:

    * appearance (a new listing),
    * disappearance (removed from market — never deleted from the record),
    * change of a watched field, with price treated specially.

    A disappearance is reported as ``asset_removed``, not ``asset_likely_sold``. Inferring
    a sale from an absence requires corroboration the diff does not have; that inference
    belongs to a later, explicitly labelled step.
    """
    events: List[DerivedEvent] = []

    if previous is None and current is not None:
        return [
            DerivedEvent(
                event_type="asset_listed",
                subject_id=subject_id,
                detected_at=detected_at,
                to_value=current.get(price_field),
                materiality="notable",
                description="First observed on market",
            )
        ]

    if previous is not None and current is None:
        return [
            DerivedEvent(
                event_type="asset_removed",
                subject_id=subject_id,
                detected_at=detected_at,
                from_value=previous.get(price_field),
                materiality="significant",
                description=(
                    "No longer observed. Cause unknown - sold, withdrawn or delisted. "
                    "Record retained for comparable analysis."
                ),
            )
        ]

    if previous is None or current is None:
        return events

    old_price = previous.get(price_field)
    new_price = current.get(price_field)
    if (
        isinstance(old_price, (int, float))
        and isinstance(new_price, (int, float))
        and old_price != new_price
        and old_price > 0
    ):
        change = new_price - old_price
        change_percent = (change / old_price) * 100.0
        events.append(
            DerivedEvent(
                event_type="asset_price_reduced" if change < 0 else "asset_price_increased",
                subject_id=subject_id,
                detected_at=detected_at,
                from_value=old_price,
                to_value=new_price,
                change_amount=change,
                change_percent=change_percent,
                materiality=_materiality_for_price_change(change_percent),
                description="Asking price moved %.1f%%" % change_percent,
                field_name=price_field,
            )
        )

    for name in watch_fields:
        if name == price_field:
            continue
        old_value = previous.get(name)
        new_value = current.get(name)
        if old_value != new_value:
            events.append(
                DerivedEvent(
                    event_type="entity_changed",
                    subject_id=subject_id,
                    detected_at=detected_at,
                    from_value=old_value,
                    to_value=new_value,
                    materiality="notable",
                    description="%s changed" % name,
                    field_name=name,
                )
            )

    return events


@dataclass
class ListingHistory:
    """The full observed life of a listing.

    Append-only. Records are never removed when a property leaves the market — the
    trajectory of a delisted listing is precisely the comparable evidence the engine
    exists to accumulate.
    """

    subject_id: str
    observations: List[Dict[str, Any]] = field(default_factory=list)

    def append(self, observed_on: date, state: Dict[str, Any]) -> None:
        self.observations.append({"observed_on": observed_on, "state": dict(state)})
        self.observations.sort(key=lambda row: row["observed_on"])

    @property
    def first_seen(self) -> Optional[date]:
        return self.observations[0]["observed_on"] if self.observations else None

    @property
    def last_seen(self) -> Optional[date]:
        return self.observations[-1]["observed_on"] if self.observations else None

    def days_on_market(self) -> Optional[int]:
        if not self.observations:
            return None
        return (self.last_seen - self.first_seen).days

    def price_trajectory(self, price_field: str = "asking_price_amount") -> List[Dict[str, Any]]:
        return [
            {"observed_on": row["observed_on"], "price": row["state"].get(price_field)}
            for row in self.observations
            if row["state"].get(price_field) is not None
        ]

    def total_price_change_percent(self, price_field: str = "asking_price_amount") -> Optional[float]:
        trajectory = self.price_trajectory(price_field)
        if len(trajectory) < 2:
            return None
        first = trajectory[0]["price"]
        last = trajectory[-1]["price"]
        if not first:
            return None
        return ((last - first) / first) * 100.0
