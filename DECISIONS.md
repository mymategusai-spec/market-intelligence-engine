# Decision Log

Dated record of decisions that are expensive to reverse or that shape later work. Newest first.

Each entry records: the decision, the evidence behind it, confidence, and **what would change
it**. A decision without a reversal trigger is a belief, not a decision.

---

## D-0012 · 2026-08-16 · Neighbourhood analysis is mandatory before any property is scored

**Decision.** No property may be scored on a market-level view alone. Every candidate must be
placed in a named submarket with its own price and convenience characteristics.

**Evidence.** Within-municipality land-price spreads are **11.1× in Hakuba** (¥67,500 vs
¥6,100/m²) and **14.0× in Myoko** (¥35,800 vs ¥2,550/m²), against a between-municipality spread
of roughly 6× across the whole longlist. Neighbourhood choice accounts for about twice the
variance that town choice does. Myoko's cheapest rural parcels are not a discount on Myoko
Kogen; they are a different and largely unrentable product.

**Confidence.** High — measured directly from official survey points.

**Changes it if:** nothing. This strengthens an existing architectural commitment
(`neighbourhood.json`) with measured evidence.

---

## D-0011 · 2026-08-16 · Yuzawa is the benchmark every cheap market must be tested against

**Decision.** Any market proposed as cheap-and-undervalued must explicitly answer: *what is
different here that was not true of Yuzawa?* A candidate that cannot answer it is not treated as
distinguished from a documented long-run decline.

**Evidence.** Yuzawa has fallen **85% from its 1993 peak** (¥190,062 → ¥28,100/m²) and was
**still falling in 2026** (−0.44%) — despite direct Shinkansen access from Tokyo, extensive
terrain, onsen, and abundant cheap apartment stock. It scores well on every naive screening
criterion this project might use. Bubble-era oversupply into a shrinking domestic market has not
cleared in three decades.

**Confidence.** High.

**Changes it if:** nothing. Yuzawa may itself become interesting if the overhang finally clears —
that would be a finding, not a reason to drop the test.

---

## D-0010 · 2026-08-16 · Minpaku-only status constrains diversification, not the core case

**Decision.** A property limited to the 180-night minpaku regime is **not** treated as
disqualified. It is scored down on `off_season_demand` and `capital_growth_potential`, while its
core winter case is scored normally. A transferable 旅館業法 licence is scored as a significant
positive.

**Evidence.** The 180-night cap is widely described as crippling, but a Japanese ski season runs
roughly December to early April — on the order of 100–140 sellable nights. A winter-dominant
property is unlikely to reach 180 nights of *demand*, so the cap does not bind on core trading.
What it forecloses is the four-season upside the brief asks about in §19.

**Confidence.** Medium. The reasoning is sound but rests on a seasonal-demand estimate, not on
observed occupancy data for a specific town.

**Changes it if:** Phase 8 occupancy data shows achievable winter-plus-shoulder nights
approaching or exceeding 180 in a candidate market — in which case the cap becomes binding and
this decision must be revisited for that market.

---

## D-0009 · 2026-08-16 · Weight commentary by the publisher's transactional interest

**Decision.** Sources publishing on markets in which they transact are registered with an
explicit conflict note, capped at Tier 4–5, and may not alone support a material investment
claim. Where a market's attractiveness is asserted mainly by such sources, that fact is reported
as part of the finding.

**Evidence.** Phase 4 screening found that the most prominent English-language commentary
promoting "emerging" Japanese ski markets is published by brokerages and developers — including
a land-price commentary site sharing a name with the developer of the largest project in the
market it highlights. Meanwhile the best available official land-price data for that same market
is flat to slightly negative. Screening on accessible sentiment would have selected for
marketing spend rather than fundamentals.

**Confidence.** High. This is standard source-criticism, and the specific conflict was directly
observed.

**Changes it if:** nothing. Conflicted sources remain useful — they are often first to real
information — but they are labelled.

---

## D-0008 · 2026-08-16 · Screening must actively discover unfashionable markets

**Decision.** Phase 4 screening treats the master prompt's named longlist as a starting point,
not the search space. Screening must actively surface overlooked and emerging towns, including
markets with little or no English-language listing presence.

**Evidence.** Master prompt §9 requires active discovery of additional locations and forbids
assuming Myoko is the winner. Undervaluation, if it exists, is least likely to persist in the
markets already saturated with foreign capital and English-language marketing (Niseko, Hakuba) —
so a screen limited to well-known names would systematically exclude the thesis's best
candidates.

**Confidence.** High for the reasoning; the resulting candidate set is untested.

**Changes it if:** discovery consistently surfaces towns that fail on gating criteria
(legality, management availability, guest viability), indicating the fringe is cheap for sound
reasons — which is itself a finding worth recording, not a reason to stop looking.

---

## D-0007 · 2026-08-16 · Static, client-side dashboard on committed data

**Decision.** The dashboard will be a static site generated from committed data, with filtering
and re-weighting done client-side, deployable to GitHub Pages.

**Evidence.** Master prompt §53 forbids creating paid cloud resources autonomously; §57 requires
an interactive decision tool. A static site satisfies both at zero cost, and cannot drift from
the repository because it is generated from it.

**Confidence.** Medium.

**Changes it if:** client-side data volume makes in-browser filtering impractical, or a feature
genuinely requires server-side computation. Either would be an owner decision, since it implies
hosting and cost.

---

## D-0006 · 2026-08-16 · Development status ladder is enforced in scoring config

**Decision.** Development projects carry a status on the ladder rumoured → proposed → announced
→ planning → approved → funded → under construction → completed (→ cancelled), and the
confidence weight per status lives in config. Forward accommodation supply is computed with
those weights applied.

**Evidence.** Master prompt §31 and §56 state that a proposal must never be treated as
equivalent to something under construction, and that rumours must never be scored like funded
projects. Ski-resort development pipelines are notoriously full of announced projects that never
break ground; unweighted pipeline counts would systematically overstate future supply.

**Confidence.** High.

**Changes it if:** nothing foreseeable. The weights themselves are tunable; the principle is not.

---

## D-0005 · 2026-08-16 · Append-only history for observations, listings and pipeline

**Decision.** `data/snapshots/`, `data/property-listings/`, `data/transactions/` and
`data/infrastructure/` are append-only. Records are superseded, never edited or deleted. A
property leaving the market keeps its full record.

**Evidence.** Master prompt §22, §34 and §55. The engine's long-term value is the longitudinal
dataset it accumulates — asking-price trajectories, days on market, outcomes — which cannot be
reconstructed retrospectively from any external source. Deleting it destroys the only genuinely
proprietary asset the project builds.

**Confidence.** High.

**Changes it if:** nothing. Storage cost of text records is negligible against the value of the
history.

---

## D-0004 · 2026-08-16 · Data committed to git rather than an external database

**Decision.** Evidence is stored as JSON / JSONL / CSV in the repository.

**Evidence.** Master prompt §4 requires GitHub to be the source of truth and forbids dependence
on one local machine. Git provides full change history and diffability at no cost. A database
would add a second source of truth requiring hosting, credentials and backup, and would place
the evidence outside the artefact the owners actually possess.

**Confidence.** Medium-high. Reasonable at the expected volume (thousands of records, not
millions).

**Changes it if:** record volume or query complexity makes file scanning impractical. Intended
path is a DuckDB index built *over* the committed files — as an index, never as a replacement.

---

## D-0003 · 2026-08-16 · JSON Schema is the canonical contract

**Decision.** Record types are defined by JSON Schema documents in `schemas/`. Python
dataclasses mirror them for typed construction and are verified against them in tests.

**Evidence.** The consumers are heterogeneous — Python ingestion, JavaScript dashboard, and
future agents using neither. A language-agnostic contract survives all three; a Python class
hierarchy would not. Follows from D-0002.

**Confidence.** High.

**Changes it if:** the project consolidates on a single language *and* schema duplication
becomes a maintenance burden.

---

## D-0002 · 2026-08-16 · Core code is Python 3.9+ stdlib only

**Decision.** No third-party runtime dependencies in `core/`. Optional tooling is isolated in
`requirements-optional.txt` and never required to read, validate or extend data.

**Evidence.** The available environment is Python 3.9.6 with no package manager (`uv`, `pipx`,
`poetry` all absent) and no package-index access from the sandbox — verified at setup. A design
requiring Pydantic v2 would not run here at all. More broadly, master prompt §4 requires the
repo to work on any machine, and §54 warns against sophisticated architecture that never
collects data. Zero-install is the property that keeps the engine usable by future agents and CI.

**Confidence.** High.

**Changes it if:** the owner adopts a managed Python toolchain and dependency installation
becomes reliable in every target environment, *and* a specific need (e.g. heavy validation
performance) justifies the cost.

---

## D-0001 · 2026-08-16 · Two-layer architecture with an enforced boundary

**Decision.** Strict separation between a domain-agnostic `core/` and domain modules under
`domains/`. `core/` may not import from `domains/` and may not contain domain vocabulary. A test
enforces this rather than relying on discipline.

**Evidence.** Master prompt §3 and §49 require that adding a domain does not force a redesign of
the core. Boundaries maintained only by convention erode under delivery pressure, and the erosion
is invisible until the second domain is attempted — at which point it is expensive.

**Confidence.** High.

**Changes it if:** nothing foreseeable. If adding a domain ever requires changing `core/`, the
correct response is to fix the leaked abstraction, not to relax the rule.

---

## D-0000 · 2026-08-16 · Master prompt is the authoritative brief

**Decision.** `prompts/master-prompt.md` holds the owner's brief verbatim and governs where any
repository document conflicts with it. Later owner instructions are appended as dated amendments
and cross-referenced here.

**Evidence.** Master prompt §5 and §50 require that a future agent can understand the project
without access to the original conversation.

**Confidence.** High.

**Changes it if:** the owner issues a superseding brief, which would itself be recorded as an
amendment.

---

## Pending decisions requiring owner input

Recorded here when they arise; currently tracked in
[`outputs/next-actions.md`](outputs/next-actions.md) under "Requires owner approval". None are
blocking research at this stage.
