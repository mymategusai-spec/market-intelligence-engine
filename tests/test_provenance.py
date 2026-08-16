"""Citation rules and collection permissions.

The single most important behaviour: a source that has been *identified* but not
*retrieved* cannot be cited. That is the guard rail between research and invention.
"""

import unittest

from core.models.common import Confidence, SourceStatus
from core.provenance.registry import CitationError, Source, SourceRegistry


def source(source_id="TEST-1", status=SourceStatus.ACCESSED, tier=1, **overrides):
    defaults = dict(
        source_id=source_id,
        name="Test source",
        publisher="Test publisher",
        source_type="official_statistics",
        reliability_tier=tier,
        status=status,
    )
    defaults.update(overrides)
    return Source(**defaults)


class TestCitation(unittest.TestCase):
    def test_candidate_source_cannot_be_cited(self):
        registry = SourceRegistry()
        registry.add(source("JP-MLIT-CHIKA", status=SourceStatus.CANDIDATE))
        with self.assertRaises(CitationError):
            registry.require_citable("JP-MLIT-CHIKA")

    def test_accessed_source_can_be_cited(self):
        registry = SourceRegistry()
        registry.add(source("JP-MLIT-CHIKA", status=SourceStatus.ACCESSED))
        self.assertEqual(registry.require_citable("JP-MLIT-CHIKA").source_id, "JP-MLIT-CHIKA")

    def test_blocked_source_cannot_be_cited(self):
        registry = SourceRegistry()
        registry.add(source("X", status=SourceStatus.BLOCKED))
        with self.assertRaises(CitationError):
            registry.require_citable("X")

    def test_unknown_source_raises(self):
        with self.assertRaises(CitationError):
            SourceRegistry().require_citable("NOPE")

    def test_tier_drives_default_confidence(self):
        self.assertEqual(source(tier=1).default_confidence, Confidence.HIGH)
        self.assertEqual(source(tier=4).default_confidence, Confidence.MEDIUM)
        self.assertEqual(source(tier=6).default_confidence, Confidence.LOW)


class TestAutomationPermission(unittest.TestCase):
    def test_unchecked_source_is_not_crawlable(self):
        """Absence of a check is not permission."""
        self.assertFalse(source(access_method="permitted_fetch").automation_permitted)

    def test_checked_and_permitted_source_is_crawlable(self):
        candidate = source(
            access_method="permitted_fetch",
            robots_checked=True,
            terms_reviewed=True,
            robots_permits_automation=True,
        )
        self.assertTrue(candidate.automation_permitted)

    def test_robots_disallow_blocks_crawling_even_when_reviewed(self):
        candidate = source(
            access_method="permitted_fetch",
            robots_checked=True,
            terms_reviewed=True,
            robots_permits_automation=False,
        )
        self.assertFalse(candidate.automation_permitted)

    def test_prohibited_method_is_never_crawlable(self):
        candidate = source(
            access_method="prohibited",
            robots_checked=True,
            terms_reviewed=True,
            robots_permits_automation=True,
        )
        self.assertFalse(candidate.automation_permitted)

    def test_official_api_is_crawlable(self):
        self.assertTrue(source(access_method="api").automation_permitted)

    def test_unverified_access_is_listed_for_review(self):
        registry = SourceRegistry()
        registry.add(source("PORTAL-A", access_method="permitted_fetch"))
        registry.add(source("GOV-API", access_method="api"))
        unverified = [s.source_id for s in registry.unverified_access()]
        self.assertEqual(unverified, ["PORTAL-A"])

    def test_paid_sources_are_surfaced_for_owner_decision(self):
        registry = SourceRegistry()
        registry.add(source("PAID", requires_payment=True))
        registry.add(source("FREE"))
        self.assertEqual([s.source_id for s in registry.paid_sources()], ["PAID"])


class TestRegistryLoading(unittest.TestCase):
    def test_from_records_parses_access_block(self):
        registry = SourceRegistry.from_records(
            [
                {
                    "source_id": "JP-ESTAT",
                    "name": "e-Stat",
                    "publisher": "Statistics Bureau",
                    "source_type": "official_statistics",
                    "reliability_tier": 1,
                    "status": "CANDIDATE",
                    "access": {"method": "api", "robots_checked": False, "terms_reviewed": False},
                }
            ]
        )
        loaded = registry.get("JP-ESTAT")
        self.assertEqual(loaded.access_method, "api")
        self.assertFalse(loaded.citable)

    def test_citable_sources_filters_correctly(self):
        registry = SourceRegistry()
        registry.add(source("A", status=SourceStatus.ACCESSED))
        registry.add(source("B", status=SourceStatus.CANDIDATE))
        self.assertEqual([s.source_id for s in registry.citable_sources()], ["A"])


if __name__ == "__main__":
    unittest.main()
