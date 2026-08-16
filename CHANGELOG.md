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

### Phase 21 — Risk and counter-thesis · `PARTIAL` (brought forward)

Brought forward because researching a thesis-critical risk *after* choosing a market would be
researching to confirm a decision already made.

- **Snow risk is real and elevation-specific.** Japan's operational ski resort count is at a
  record low, **40% below its 1999 peak**, attributed to lack of snow. Peer-reviewed work
  (1959–2020) finds declining maximum snow depth at **low elevations on the Japan Sea side**,
  but **no trend at high elevations in eastern Honshu** and a significant *increase* in maximum
  daily snowfall there; Sapporo and Akita show no clear long-term decline. Base elevation and
  regional regime are now first-class screening criteria (`DECISIONS.md` D-0013).
- Noted that **Takada — adjacent to Myoko — is one of two stations named as showing marked
  long-term decline**, and that Hakuba, the fastest-appreciating land market in Japan, is
  simultaneously piling snow onto its highest course to keep operating. Land prices and snow
  reliability are not measuring the same thing.
- **Rejected rather than recorded** a reported Myoko vertical of 1,724 m, which contradicts the
  same source's own statement that only five Japanese resorts exceed 1,000 m vertical.
- **Myoko is projected to lose 46.7% of its population by 2050** (IPSS 2023 projections), to
  ~16,200 people. In Hokkaido, 129 municipalities are projected to fall to ≤60% of current
  population by 2050.
- Added assumption **E6**: that tourism demand can decouple from resident decline. Hakuba and
  Kutchan appear to have decoupled; Myoko has not yet; Yuzawa did not over 33 years. This
  reframes the screening question from "is the town shrinking?" to "**has tourism demonstrably
  decoupled from resident decline here?**"
- Recorded the interaction as the most plausible current answer to *why hasn't capital
  arbitraged this away?* — **the discount may be compensation for real snow, labour and
  liquidity risk rather than an oversight.** Stated as a hypothesis to be tested in Phases 5–11,
  not as a conclusion.

### Phase 7 — Historical property markets · `PARTIAL` (brought forward)

- **Verified the 2026 land-price figures** against a second independent source, agreeing to
  within 0.02 percentage points. The Phase 4 headline tension is now corroborated rather than a
  lead. Data in `data/reference/land-prices-2026.json`; analysis in
  `domains/japan_ski_property/property_market/land-price-regimes.md`.
- **Established that Japanese ski land is three markets, not one:** recovering strongly
  (Hakuba +26.9% national #1, Nozawa Onsen +21.7% #2), established and still rising
  (Kutchan +12.3%, Furano +6.7%), and flat or falling (Myoko −0.79%, Yuzawa −0.44%).
- **Promoted Nozawa Onsen to serious research.** The national #2 performer receives a fraction
  of the promotional coverage Myoko does — exactly what an evidence-led screen should surface.
- **Documented Yuzawa as a 33-year value trap:** −85% from its 1993 peak and still falling,
  despite Shinkansen access, snow and cheap stock. Adopted as the benchmark every cheap
  candidate must be tested against (`DECISIONS.md` D-0011).
- **Reframed Hakuba** with 30-year context: down 84% from its 1995 peak to a 2018 low, nearly
  tripled since, and still 54% below peak. "Too expensive" is a claim about seven years, not
  thirty.
- **Measured the within-town spread at 11–14×** against a between-town spread of ~6×, making
  neighbourhood analysis mandatory before any property is scored (`DECISIONS.md` D-0012).
- Noted MLIT's own attribution of Hakuba's rise to foreign buyers **opening accommodation
  businesses** — this project's exact strategy, already executed at scale by others there.

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
