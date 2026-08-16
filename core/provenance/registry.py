"""The source register, and the rules that keep citations honest.

Two guarantees this module enforces:

1. A claim can only cite a source that exists in the register.
2. A source that has only been *identified* (``CANDIDATE``) can never be cited as
   evidence. Identifying a likely source is not the same as having read it, and the
   distinction is exactly where a research system quietly starts inventing things.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

from core.models.common import Confidence, SourceStatus


#: Default confidence implied by a source's reliability tier, before any
#: source-specific adjustment. Tier 1 is official statistics; tier 6 is anecdote.
TIER_DEFAULT_CONFIDENCE = {
    1: Confidence.HIGH,
    2: Confidence.HIGH,
    3: Confidence.MEDIUM,
    4: Confidence.MEDIUM,
    5: Confidence.LOW,
    6: Confidence.LOW,
}


class CitationError(Exception):
    """Raised when something is cited that cannot honestly be cited."""


@dataclass
class Source:
    source_id: str
    name: str
    publisher: str
    source_type: str
    reliability_tier: int
    status: SourceStatus
    url: Optional[str] = None
    language: Optional[str] = None
    geography: Optional[str] = None
    first_accessed: Optional[str] = None
    last_accessed: Optional[str] = None
    robots_checked: bool = False
    robots_permits_automation: Optional[bool] = None
    terms_reviewed: bool = False
    access_method: str = "manual"
    requires_payment: bool = False
    known_biases: Optional[str] = None
    blocked_reason: Optional[str] = None

    @property
    def citable(self) -> bool:
        """Only a source actually retrieved may support a claim."""
        return self.status == SourceStatus.ACCESSED

    @property
    def default_confidence(self) -> Confidence:
        return TIER_DEFAULT_CONFIDENCE.get(self.reliability_tier, Confidence.UNKNOWN)

    @property
    def automation_permitted(self) -> bool:
        """Whether automated collection from this source is allowed.

        Defaults to False. Absence of a check is not permission — a source is only
        crawlable once robots.txt and terms have been positively reviewed.
        """
        if self.access_method == "prohibited":
            return False
        if self.access_method in ("api", "bulk_download", "feed"):
            return True
        return bool(self.robots_checked and self.terms_reviewed and self.robots_permits_automation)


@dataclass
class SourceRegistry:
    sources: Dict[str, Source] = field(default_factory=dict)

    @classmethod
    def from_records(cls, records: Iterable[Dict[str, object]]) -> "SourceRegistry":
        registry = cls()
        for record in records:
            access = record.get("access", {}) or {}
            source = Source(
                source_id=str(record["source_id"]),
                name=str(record["name"]),
                publisher=str(record["publisher"]),
                source_type=str(record["source_type"]),
                reliability_tier=int(record["reliability_tier"]),
                status=SourceStatus(str(record["status"])),
                url=record.get("url"),
                language=record.get("language"),
                geography=record.get("geography"),
                first_accessed=record.get("first_accessed"),
                last_accessed=record.get("last_accessed"),
                robots_checked=bool(access.get("robots_checked", False)),
                robots_permits_automation=access.get("robots_permits_automation"),
                terms_reviewed=bool(access.get("terms_reviewed", False)),
                access_method=str(access.get("method", "manual")),
                requires_payment=bool(access.get("requires_payment", False)),
                known_biases=record.get("known_biases"),
                blocked_reason=record.get("blocked_reason"),
            )
            registry.add(source)
        return registry

    @classmethod
    def load(cls, path: str) -> "SourceRegistry":
        if not os.path.exists(path):
            return cls()
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        records = payload["sources"] if isinstance(payload, dict) else payload
        return cls.from_records(records)

    def add(self, source: Source) -> None:
        self.sources[source.source_id] = source

    def get(self, source_id: str) -> Source:
        if source_id not in self.sources:
            raise CitationError(
                "Unknown source_id %r. Register the source before citing it." % source_id
            )
        return self.sources[source_id]

    def require_citable(self, source_id: str) -> Source:
        """Fetch a source, refusing if it cannot honestly support a claim."""
        source = self.get(source_id)
        if not source.citable:
            raise CitationError(
                "Source %s has status %s and cannot be cited as evidence. "
                "Retrieve it and record the access date first."
                % (source_id, source.status.value)
            )
        return source

    def citable_sources(self) -> List[Source]:
        return [s for s in self.sources.values() if s.citable]

    def crawlable_sources(self) -> List[Source]:
        return [s for s in self.sources.values() if s.automation_permitted]

    def paid_sources(self) -> List[Source]:
        """Sources requiring payment — surfaced for owner decision, never bought."""
        return [s for s in self.sources.values() if s.requires_payment]

    def unverified_access(self) -> List[Source]:
        """Sources whose robots.txt or terms have not been reviewed.

        These must not be collected from automatically until checked.
        """
        return [
            s
            for s in self.sources.values()
            if s.access_method not in ("api", "bulk_download", "feed", "prohibited")
            and not (s.robots_checked and s.terms_reviewed)
        ]
