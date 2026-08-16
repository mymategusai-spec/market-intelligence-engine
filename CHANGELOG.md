# Changelog

Meaningful changes to the engine, its data and its conclusions. Newest first.

Format: date · phase · what changed · why it matters.

---

## 2026-08-16

### Phase 4 — Destination screening · `ACTIVE` (first pass)

- Verified three Tier 1 sources as `ACCESSED`: the MLIT 令和8年地価公示 release (2026-03-17,
  26,000 points), the MLIT Real Estate Information Library (free API since April 2024 covering
  **actual transaction prices** from Q3 2005), and JMA downloadable station snow data.
- **Recorded the pass's main finding: a contradiction between narrative and official data.**
  Hakuba recorded the largest residential land-price rise in Japan (+33.0%) and Kutchan
  continued rising, while Myoko — the market most heavily promoted to the exact buyer profile
  this project describes — appears flat to slightly negative. Per-market figures are marked
  `UNVERIFIED` pending primary MLIT data.
- Identified that the most prominent commentary promoting "emerging" markets is published by
  brokerages and developers with direct transactional interests, including a land-price
  commentary site sharing a name with the developer of the largest project in the market it
  promotes. Recorded as `DECISIONS.md` D-0009 and `ASSUMPTIONS.md` F6.
- Logged the Patience Capital Group Myoko development (350 ha, ~US$1.4bn, first stage 2028,
  ¥35bn of up to ¥70bn raised) as a partially-funded catalyst — and noted it **cannot** enter
  forward supply until its accommodation capacity is established, because a large nearby
  development raises a destination's profile and its competing supply simultaneously.
- Flagged Myoko's reported −24.7% population projection to 2035 as material to labour,
  amenities and exit, pending IPSS verification.

### Phase 12 — Regulation · `PARTIAL` (brought forward)

- Researched early because it is gating. **Foreign freehold ownership confirmed unrestricted**,
  with no nationality-based tax surcharge; acquisition costs evidenced at ~6–8% above purchase
  price; non-resident MoF reporting duty within 20 days.
- Established that the binding constraint is the **operating licence, not the buyer**, and
  reasoned that the minpaku 180-night cap likely does **not** bind on a winter-dominant ski
  property whose sellable season is ~100–140 nights — it constrains four-season upside instead
  (`DECISIONS.md` D-0010).
- Identified the **municipal ordinance layer as the largest open regulatory risk**: local rules
  can designate zero-day lodging zones, and local opposition to foreign investment is a leading
  indicator of tightening.
- Assumption C3 moved from Low to Low–Medium confidence; it can still fail municipally.

### Phase 3 — Domain module · `DONE`

- Domain schemas: property, town_profile, ski_area, neighbourhood, renovation_budget,
  service_provider. Snow is recorded twice — marketed and measured, with the measuring
  station's distance and elevation — because operator figures are marketing and valley
  stations under-report mountain snowfall.
- Config: 20 scorecard dimensions with definitions and derivation, five weight profiles, price
  tiers, proximity bands, disqualification rules. No profile is presented as the owners'
  preference, because none has been given.
- Config consistency tests: every weighted component is defined, the catalyst status ladder
  never decreases, and the emerging-upside profile cannot underweight risk relative to balanced.

### Phase 2 — Core schemas and engine · `DONE`

- JSON Schema contracts for all core record types, plus engine logic for money/FX, scoring,
  financial modelling, change detection and provenance. 104 tests, stdlib only.
- The core/domain boundary test earned its keep on first run: it caught `guest_capacity` and
  `snow_clearing` leaking into the core financial schema, now generalised to `capacity_units`
  and a `domain_costs` map.

### Phase 1 — Foundational repository · `DONE`

- Saved the owner's master prompt verbatim to `prompts/master-prompt.md` as the authoritative
  brief, with an amendments section for later owner instructions.
- Established the two-layer architecture: domain-agnostic `core/` and domain modules under
  `domains/`, with a one-directional dependency rule.
- Created the repository structure: `config/`, `core/`, `schemas/`, `domains/`, `data/`,
  `analysis/`, `app/`, `scripts/`, `workflows/`, `tests/`, `outputs/`.
- Wrote foundational documentation: `README.md`, `PROJECT_BRIEF.md`, `ARCHITECTURE.md`,
  `RESEARCH_PLAN.md`, `ASSUMPTIONS.md`, `DECISIONS.md`, `SOURCES.md`.
- Set the dependency policy to Python 3.9+ stdlib only after verifying the environment has no
  package manager and no package-index access (`DECISIONS.md` D-0002).
- Populated the source register with the official Japanese statistical, land-price, tourism,
  meteorological and regulatory sources the research will depend on, each marked `CANDIDATE`
  pending first access.
- Recorded initial assumptions, flagging **C2** (management procurable), **C3** (commercial
  operation legally achievable) and **E3** (snow viable over 10–15 years) as low-confidence
  gating assumptions that can each independently disqualify a market or the thesis.

### Repository intake

- Recorded and then resolved the intake blocker: the master prompt was not present in the
  repository at session start, and was supplied by the owner mid-session.

---

## Conventions

- **Data changes** note which append-only path was written and how many records were added.
- **Conclusion changes** note what evidence moved the conclusion, and its confidence.
- **Retractions** are recorded explicitly. A number that turns out to be wrong is corrected in
  the log, not quietly overwritten — the correction is itself intelligence about source
  reliability.
