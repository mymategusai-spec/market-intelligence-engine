"""Reusable, domain-agnostic market intelligence engine.

This package must never import from ``domains``. It knows about assets, entities,
observations, sources, snapshots, events, catalysts, value-add projects, scores and
financial models — and nothing about any particular market.

The boundary is enforced by ``tests/test_core_is_domain_agnostic.py``.
"""
