# Market Intelligence Engine

A reusable, persistent market-intelligence and opportunity-discovery platform.

The engine ingests evidence about a market, preserves it with full provenance, snapshots it
over time, detects change, scores opportunities against adjustable weightings, and models the
economics of specific assets. It is designed to become **more valuable the longer it runs**,
because it accumulates longitudinal history that cannot be bought retrospectively.

The first real-world implementation is the domain module **`japan_ski_property`**: an
investigation into whether two Australians should buy, renovate and operate an accommodation
property near excellent Japanese snow.

> The goal is not to build a website about Japanese ski houses. The goal is a reusable market
> intelligence system, with Japanese ski property as its first implementation.
> — `prompts/master-prompt.md`, §58

---

## Start here

| If you are… | Read |
| --- | --- |
| An AI agent picking up this repo | [`outputs/next-actions.md`](outputs/next-actions.md), then the [Agent continuity](#how-another-agent-continues-the-work) section below |
| Understanding *why* this project exists | [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md) |
| Understanding *how* it is built | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| Understanding *what* is being researched, and in what order | [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) |
| Checking what is taken on faith | [`ASSUMPTIONS.md`](ASSUMPTIONS.md) |
| Checking why something was decided | [`DECISIONS.md`](DECISIONS.md) |
| Checking where a number came from | [`SOURCES.md`](SOURCES.md) |
| The authoritative brief | [`prompts/master-prompt.md`](prompts/master-prompt.md) |

---

## Purpose

The engine exists to improve decision quality, not to justify a purchase. A conclusion of
"no current opportunity is attractive" is a legitimate and valuable output.

For the first domain it must eventually give defensible, evidence-backed answers to:

- Where in Japan is the best intersection of excellent snow, low entry price, growing tourism,
  good town amenities, accommodation demand, manageable renovation, realistic remote operation,
  year-round potential and future capital appreciation?
- What property type and guest capacity produce the best economics?
- How much AUD capital would two Australians realistically need?
- Which actual properties should they inspect first?
- What could destroy the thesis, and who buys the asset from them in 10–15 years?

---

## Architecture in one picture

```
                 ┌─────────────────────────────────────────────┐
   sources ─────▶│  ingestion    → raw capture + provenance     │
                 ├─────────────────────────────────────────────┤
                 │  CORE ENGINE (domain-agnostic)              │
                 │   entities · assets · observations          │
                 │   snapshots · events · change detection     │
                 │   catalysts · value-add projects · risks    │
                 │   scoring · filters · financial modelling   │
                 ├─────────────────────────────────────────────┤
                 │  DOMAIN MODULE  japan_ski_property          │
                 │   property/town/ski/renovation specialisms  │
                 │   weights · thresholds · vocabularies       │
                 ├─────────────────────────────────────────────┤
                 │  OUTPUTS   scorecards · shortlists ·        │
                 │            models · alerts · dashboard      │
                 └─────────────────────────────────────────────┘
```

The **core** knows nothing about skiing. It understands `asset`, `location_metric`,
`market_catalyst`, `value_add_project`, `observation`, `source`. The **domain module**
specialises those generics — `distance_to_lift` is a domain-defined `location_metric`, a new
gondola is a domain-defined `market_catalyst`, a renovation is a `value_add_project`.

Adding a second domain (commercial property, businesses for sale, another country) must not
require redesigning the core. See [`ARCHITECTURE.md`](ARCHITECTURE.md) §"Adding a new domain".

---

## Repository structure

```text
prompts/            Authoritative master prompt and reusable research prompts
config/             Configuration, separated from code
  core/               Engine-level config (confidence tiers, FX, event types)
  domains/            Per-domain config (weights, thresholds, vocabularies)
core/               Reusable engine code — domain-agnostic, stdlib-only
  models/             Core data model (dataclasses mirroring the JSON Schemas)
  provenance/         Source register, confidence, traceability
  scoring/            Weighted scoring, filters, opportunity detection
  financial/          Cash-flow and total-project-cost modelling
  monitoring/         Snapshot diffing and change detection
schemas/            Canonical JSON Schema contracts (language-agnostic)
  core/               Core entity schemas
  domains/            Domain-specific schemas
domains/            Domain modules: code + research content
  japan_ski_property/
    models/           Domain model code
    research/         Working research notes, per phase
    properties/       Property records
    town_profiles/    Town/vibe profiles
    neighbourhoods/   Micro-location submarkets
    tourism/          Tourism data and analysis
    property_market/  Land/property price history
    business_activity/Business formation, openings, closures
    infrastructure/   Development and infrastructure pipeline
    regulation/       Licensing, ownership, tax, compliance
    renovation/       Renovation cost models
    management/       Local operators, managers, service providers
    inspectors/       Independent inspector and contractor network
    financial_models/ Per-asset financial models
    outputs/          Domain deliverables (shortlists, recommendations)
data/               Evidence store, versioned in git
  raw/                Unmodified captures, exactly as retrieved
  cleaned/            Normalised, typed, unit-converted
  snapshots/          Append-only point-in-time observations
  history/            Derived longitudinal series
  reference/          Slow-moving reference data (FX, geography, codes)
  property-listings/  Listing records and their full history
  transactions/       Confirmed and inferred sales
  infrastructure/     Development pipeline records
analysis/           Cross-cutting analysis outputs
  scorecards/  financial_models/  scenarios/  charts/
app/                Decision tool
  dashboard/          Filterable, re-weightable dashboard
  api/                Data access layer (if/when justified)
scripts/            Executable entry points
  ingestion/  monitoring/  analysis/  utilities/
workflows/          Scheduled monitoring definitions (GitHub Actions)
tests/              Tests for transformations and scoring logic
outputs/            Session continuity and top-level deliverables
  next-actions.md     ← always current; the handoff file
```

---

## Setup

The repository is deliberately **dependency-light**. Core code targets the Python 3 standard
library only (Python 3.9+), so any machine, agent or CI runner can use it immediately with no
install step.

```bash
git clone https://github.com/mymategusai-spec/market-intelligence-engine.git
cd market-intelligence-engine
python3 --version                              # 3.9+ required
python3 -m unittest discover -s tests -t . -v  # run from the repository root
```

Optional tooling for later phases (charting, JSON Schema validation, dashboard build) is listed
in `requirements-optional.txt` and is never required to read, validate or extend the data.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) §"Dependency policy" for the reasoning.

---

## Remote workflow

GitHub is the single source of truth. The repository must never depend on one local machine.

After every meaningful unit of work:

1. Update the relevant data and research files.
2. Update `SOURCES.md` with any new sources.
3. Update `ASSUMPTIONS.md` if an assumption was added, changed or invalidated.
4. Update `DECISIONS.md` if a decision was made.
5. Update `CHANGELOG.md`.
6. Update `outputs/next-actions.md`.
7. Commit with a descriptive message.
8. Push to `origin/main`.

Nothing important is left only on a local disk.

---

## Research methodology

**Source hierarchy.** Preference order, highest first: Japanese national government →
prefectural government → municipal government → official tourism organisations → official
land-price data → planning records → company filings → credible property data → reputable
agencies → accommodation data → industry research → reputable media → community/anecdotal.
Japanese-language sources are searched, not only English ones.

**Claim typing.** Every material claim is tagged:

| Tag | Meaning |
| --- | --- |
| `FACT` | Directly attested by a cited source |
| `CALCULATION` | Derived from cited facts by a stated method |
| `ESTIMATE` | Reasoned approximation where data is unavailable, with a stated basis and range |
| `ASSUMPTION` | Taken as given pending evidence; recorded in `ASSUMPTIONS.md` |
| `OPINION` | Subjective judgement, including third-party opinion |

Missing data is recorded as missing. It is never invented, and an `ESTIMATE` is never presented
as a `FACT`. Precision is not manufactured: a renovation figure inferred from listing photos is
a range with a confidence level, not a number.

**Adversarial stance.** For every cheap market the engine asks *why is this cheap?* For every
apparently emerging market it asks *why hasn't sophisticated capital already arbitraged this
away?* Counter-thesis research is a required phase, not an optional one.

---

## Data provenance

Every material data point is traceable to its origin. Observations carry a `source_id` into the
source register, the retrieval date, the original value and units as published, any
transformation applied, and a confidence rating.

This means any number in a final recommendation can be audited back to a URL and a date. See
[`ARCHITECTURE.md`](ARCHITECTURE.md) §"Provenance model" and the schemas in `schemas/core/`.

Historical records are **append-only**. Listings that leave the market are never deleted —
their full history is retained, because a delisted property with a known asking-price
trajectory is exactly the comparable evidence the engine needs later.

---

## How another agent continues the work

An agent opening this repository should be able to resume without any prior conversation.
Read in this order:

1. **`outputs/next-actions.md`** — current state, in-flight work, blockers, next actions.
   This is the handoff file and is always current.
2. **`prompts/master-prompt.md`** — the authoritative brief. It governs where documents conflict.
3. **`PROJECT_BRIEF.md`** — the thesis being tested and what would falsify it.
4. **`RESEARCH_PLAN.md`** — phases, their status, and what each must produce.
5. **`ASSUMPTIONS.md`**, **`DECISIONS.md`**, **`SOURCES.md`** — what is assumed, what was
   decided and why, and what evidence exists so far.
6. **`ARCHITECTURE.md`** — how to extend the system without breaking its contracts.

Then follow the operating rules:

- Work autonomously through anything determinable from the brief, the repo, existing data or
  standard practice. Do not stop to ask what to do next.
- If blocked on one source, document the blocker, identify alternatives, and continue with
  independent work elsewhere.
- Never delete historical observations. Append.
- Never present an estimate as a fact.
- Never let a proposed development score like a funded one.
- Commit and push to `origin/main` after every meaningful work unit.
- Stop only for genuine owner preference, credentials, cost, destructive external action, or
  irresolvable ambiguity — and update `outputs/next-actions.md` before doing so.

Actions requiring explicit owner approval — spending money, contacting agents, sellers,
inspectors or contractors, entering contracts, creating paid cloud resources — are listed in
`outputs/next-actions.md` under "Requires owner approval" and must never be taken autonomously.

---

## Status

Early. Phase 1–3 foundations are in place; research phases are in progress. Current phase
status is tracked in [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) and
[`outputs/next-actions.md`](outputs/next-actions.md).

No investment conclusion has been reached, and none should be inferred from the presence of
data in this repository.
