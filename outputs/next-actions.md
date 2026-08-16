# Next Actions

**Last updated:** 2026-08-16
**Branch:** `main`
**Current phase:** 2–4 (core schemas, domain schemas, destination screening)
**Overall status:** Foundations built. Research beginning. **No investment conclusion reached.**

This is the handoff file. An agent picking up this repository should read this first, then
`prompts/master-prompt.md`, then `PROJECT_BRIEF.md` and `RESEARCH_PLAN.md`.

---

## Where the project stands

Phase 1 is complete: the two-layer architecture, repository structure, dependency policy and
foundational documentation are in place, and the owner's master prompt is saved as the
authoritative brief.

Nothing has been researched yet. The source register is populated with identified official
sources, but every row is `CANDIDATE` — **none has been accessed, and nothing in it may be
cited as evidence yet.**

---

## Immediate next actions

In priority order. Each is independently startable.

1. **Finish Phase 2 — core schemas.** Author `schemas/core/*.json` for `source`, `observation`,
   `entity`, `asset`, `snapshot`, `event`, `market_catalyst`, `value_add_project`,
   `location_metric`, `market_indicator`, `risk_factor`, `score`, `financial_model`. Mirror in
   `core/models/` dataclasses. Enforce: no observation without a `source_id`; FX carries rate
   and rate date.
2. **Finish Phase 3 — domain schemas.** `property`, `town_profile`, `neighbourhood`, `ski_area`,
   `renovation_budget`, `development_project`, `management_provider`, `inspector`. The property
   schema must carry the full attribute set from master prompt §20 including first/last seen and
   listing status.
3. **Phase 4 — destination screening.** Screen the longlist and actively discover overlooked
   towns. Record every claim with provenance. Do **not** assume Myoko.
4. **Verify source access.** For each Tier 1 source, confirm the URL, check access method and
   record it as `ACCESSED` in `SOURCES.md`. Prioritise `JP-JMA-SNOW` (snow reality vs marketing
   claims), `JP-MLIT-TORIHIKI` (transaction vs asking prices) and `JP-JTA-SHUKUHAKU`
   (accommodation demand).
5. **Check portal terms before any automated collection.** Phase 13's design depends on what
   robots.txt and site terms permit. Establish this early — it may constrain the whole
   collection approach.
6. **Write the boundary test** (`tests/test_core_is_domain_agnostic.py`) before `core/` grows.
   Enforcing the rule after the fact is much harder.

---

## Known blockers

| Blocker | Impact | Workaround in use |
| --- | --- | --- |
| `gh` CLI token invalid | No PR/issue/API operations via `gh` | None needed — `git push` works via keychain; fix with `gh auth login -h github.com` when convenient |
| No Python package manager or index access in the sandbox | Cannot install third-party libraries | **Resolved by design** — stdlib-only core (`DECISIONS.md` D-0002) |
| Portal terms unverified | Phase 13 collection design cannot be finalised | Verify robots.txt and terms before building any collector |

---

## Requires owner approval

Never actioned autonomously (master prompt §53). Nothing here is currently blocking research.

| Item | Why it needs approval | When it will matter |
| --- | --- | --- |
| Contacting agents, sellers, inspectors, contractors | External contact with real people | Phase 15/16, and before any inspection |
| Purchasing paid data sources | Spends money | If Phase 7/13 finds material data is paywalled — candidates will be listed in `SOURCES.md` |
| Creating paid cloud resources | Spends money | Only if the static dashboard proves insufficient (D-0007) |
| Any property transaction step | Financial commitment | Not applicable at this stage |

---

## Open questions for the owner

None blocking. Recorded for when convenient:

- **Capital ceiling.** Currently assumed open-ended (`ASSUMPTIONS.md` A3). A rough ceiling would
  sharpen screening considerably, but the engine will derive shoestring/sensible/strong
  requirements regardless.
- **Return vs lifestyle weighting.** The scoring axes are adjustable by design; owner
  preferences would set sensible defaults rather than neutral ones.

---

## Standing rules for whoever works next

- Do not delete historical observations. Append.
- Do not present an `ESTIMATE` as a `FACT`, or cite a `CANDIDATE` source as evidence.
- Do not let a proposed development score like a funded one.
- Do not assume a residential property can legally be operated as commercial accommodation.
- Search Japanese-language sources, not only English ones.
- Commit and push to `origin/main` after every meaningful work unit.
- Update this file, `CHANGELOG.md`, `SOURCES.md`, `ASSUMPTIONS.md` and `DECISIONS.md` as work
  proceeds — not in a batch at the end.

---

## Session log

**2026-08-16 —** Intake blocker (master prompt absent) recorded, then resolved when the owner
supplied the brief. Master prompt saved. Phase 1 completed: architecture, structure,
documentation, dependency policy, source register, assumptions and decision log. Phases 2–4
started.
