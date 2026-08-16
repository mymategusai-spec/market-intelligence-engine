# Architecture

How the Market Intelligence Engine is built, and the reasoning behind the choices that are
expensive to reverse later.

---

## 1. Two layers, hard boundary

```
┌──────────────────────────────────────────────────────────────┐
│  DOMAIN MODULE            domains/japan_ski_property/         │
│  Vocabulary, specialisations, weights, thresholds, research   │
│  Knows about: lifts, powder, minpaku, ryokan, drying rooms    │
└───────────────────────────┬──────────────────────────────────┘
                            │ depends on (one direction only)
┌───────────────────────────▼──────────────────────────────────┐
│  CORE ENGINE              core/                               │
│  Knows about: asset, entity, observation, source, snapshot,   │
│  event, catalyst, value_add_project, score, filter, model     │
│  Knows NOTHING about skiing, Japan, or property               │
└──────────────────────────────────────────────────────────────┘
```

**The rule:** `core/` must never import from `domains/`, and must never contain a
domain-specific identifier. If the word "ski", "lift", "powder", "onsen" or "Japan" appears in
`core/`, the boundary has been violated.

Enforced by a test (`tests/test_core_is_domain_agnostic.py`) rather than by convention alone.

### Generic → specific mapping

| Core concept | Japan ski specialisation |
| --- | --- |
| `asset` | property (house, chalet, pension, lodge, ryokan, former hotel) |
| `location_metric` | distance to lift, to supermarket, to Shinkansen, walk time |
| `market_catalyst` | new gondola, hotel development, Shinkansen extension, airport route |
| `value_add_project` | renovation / repositioning scenario |
| `entity` | town, resort, operator, manager, inspector, developer |
| `observation` | a snowfall figure, a land price, an asking price, an occupancy rate |
| `market_indicator` | median price/m², forward supply ratio, visitor nights growth |
| `risk_factor` | snow reliability, oversupply, depopulation, seismic, FX |

---

## 2. Dependency policy

**Core code is Python 3.9+ standard library only. No third-party runtime dependencies.**

Reasoning:

- The project must run on any machine, any CI runner and any future agent's environment with
  zero setup. GitHub is the source of truth and the repo must not depend on one local machine's
  toolchain (master prompt §4).
- The available environment is Python 3.9.6 with no package manager (`uv`, `pipx`, `poetry` all
  absent) and no `pip` network access from the sandbox. A design requiring Pydantic v2 would
  have been dead on arrival here and fragile everywhere else.
- Dependency-light beats dependency-elegant for a system whose main risk is *never collecting
  data* (master prompt §54).

Optional tooling (charting, JSON Schema validation, dashboard build) lives in
`requirements-optional.txt`. Nothing in the optional set is ever required to **read, validate or
extend the data**. If an optional dependency is missing, scripts degrade with a clear message
rather than failing obscurely.

**Consequence:** canonical schemas are JSON Schema documents, not Python classes. See §3.

---

## 3. Schemas: JSON Schema is canonical

The contract for every record type is a JSON Schema document in `schemas/`.

```
schemas/core/                    source.json, observation.json, asset.json,
                                 entity.json, snapshot.json, event.json,
                                 catalyst.json, value_add_project.json,
                                 score.json, financial_model.json
schemas/domains/japan_ski_property/
                                 property.json, town_profile.json,
                                 neighbourhood.json, ski_area.json,
                                 renovation_budget.json, development_project.json
```

Python dataclasses in `core/models/` and `domains/*/models/` mirror these schemas for typed
construction. The schema is the source of truth; the dataclass is a convenience, and is added
when logic actually needs it rather than generated wholesale up front — unused mirror classes
drift out of sync with the schemas they claim to represent.

Why schema-first: the dashboard is JavaScript, the ingestion is Python, and future agents may
use neither. A language-agnostic contract survives all three.

---

## 4. Provenance model

Every material number is traceable to a URL and a date. This is the property that makes the
engine auditable, and it is designed in at the record level rather than bolted on.

```
Source                    Observation                     Claim
──────                    ───────────                     ─────
source_id      ◀──────── source_id                       claim_type:
url                       retrieved_at                     FACT | CALCULATION |
publisher                 original_value                   ESTIMATE | ASSUMPTION |
source_type               original_units                   OPINION
publication_date          normalised_value
reliability_tier          normalised_units
access_method             transformation                 confidence:
robots_ok                 confidence                       high | medium | low
terms_note                notes                          
                          supersedes ◀── prior observation
```

**Rules:**

- An observation without a `source_id` is invalid and fails validation.
- `original_value` and `original_units` record the figure *as published*. Conversions (JPY→AUD,
  m²→m², 坪→m²) are recorded as an explicit `transformation`, never applied silently.
- FX conversions carry the **rate and the date of the rate**. An AUD figure without them is
  meaningless a year later.
- Observations are **superseded, never edited**. Correcting a number appends a new observation
  pointing at the old one.

### Reliability tiers

Sources are tiered per the master prompt's hierarchy (§43). Tier drives default confidence and
is visible in outputs, so a conclusion resting on a forum post is never presented like one
resting on official land-price data.

| Tier | Sources |
| --- | --- |
| 1 | Japanese national government, official statistics, official land-price data |
| 2 | Prefectural and municipal government, planning records |
| 3 | Official tourism organisations, company filings |
| 4 | Credible property data providers, reputable agencies, accommodation data |
| 5 | Industry research, reputable media |
| 6 | Community, forum, review and anecdotal sources |

Tier 6 is admissible — it is often the only source for "does the town feel dead at 8pm" — but
it is labelled `OPINION`, never aggregated into a `FACT`, and never used alone for a material
investment claim.

---

## 5. Data lives in git, append-only

Data is committed to the repository as JSON / JSONL / CSV rather than held in an external
database.

**Why:** the master prompt requires GitHub to be the source of truth and the system to survive
the loss of any local machine. Git also gives, for free, the two properties this project needs
most — full history of every change, and diffability of every observation.

**Why not a database:** a database would be a second source of truth needing hosting,
credentials and backup, and would put the evidence outside the artefact the owners actually
have. If data volume later justifies one, DuckDB over the committed files is the intended path —
as an *index*, not a replacement.

### Layout and mutability

| Path | Mutability | Content |
| --- | --- | --- |
| `data/raw/` | **immutable** | Captures exactly as retrieved, named with retrieval date |
| `data/snapshots/` | **append-only** | Point-in-time observations, JSONL, one line per observation |
| `data/cleaned/` | rewritable | Normalised, typed, unit-converted — derived, regenerable |
| `data/history/` | rewritable | Derived longitudinal series — regenerable from snapshots |
| `data/reference/` | rewritable | Slow-moving reference: FX, geography, codes |
| `data/property-listings/` | **append-only** | Listing records and their full observed history |
| `data/transactions/` | **append-only** | Confirmed and inferred sales |
| `data/infrastructure/` | **append-only** | Development pipeline records and status changes |

**Nothing in an append-only path is ever deleted or overwritten.** A property that leaves the
market keeps its full record — first seen, every price change, last seen, days on market,
outcome. That retained history is the proprietary comparable dataset the engine is being built
to accumulate (master prompt §55); deleting it destroys the asset.

Derived paths carry a header noting which script regenerates them.

---

## 6. Snapshots and change detection

```
   ingest ──▶ snapshot(t)  ──┐
                             ├──▶ diff ──▶ event ──▶ alert / opportunity signal
   ingest ──▶ snapshot(t-1) ─┘
```

A **snapshot** is what an asset or entity looked like at one moment. Snapshots are never
overwritten, so the system can always answer *"what did this listing look like six months ago?"*
and *"what changed?"*.

An **event** is a typed, dated, evidenced change: new listing, price reduction, price increase,
removal, relisting, likely sale, confirmed sale, development announced/approved/funded/commenced/
completed/cancelled, new lift, regulation change, statistical release, business opening/closure.

Events are the engine's memory of *change*, distinct from its memory of *state*. Both are kept.

### Development status is a ladder, never collapsed

```
rumoured → proposed → announced → planning → approved → funded →
under construction → completed
                                    └────────▶ cancelled (from any stage)
```

Each stage carries its own confidence weight in scoring. **A rumoured hotel must never
contribute to forward accommodation supply like a funded one** (master prompt §31, §56). This is
enforced in the scoring config, not left to the analyst's judgement.

---

## 7. Scoring, filters and weights

Scoring is transparent and re-runnable, never a black box.

- **Component scores** are 0–10 per dimension (affordability, ski quality, snow reliability,
  tourism growth, town vibe, regulation, infrastructure, future-supply balance, exit liquidity,
  risk, …), each with the evidence and confidence that produced it.
- **Weights live in config**, not code — `config/domains/japan_ski_property/weights.yaml`.
  Subjective preferences are never hard-coded (master prompt §38).
- **Preference axes** are exposed as sliders the owners can move: investment return ↔ lifestyle,
  cheap entry ↔ premium, established ↔ emerging, winter ↔ four-season, turnkey ↔ renovation,
  low risk ↔ high upside, town life ↔ ski proximity, cash flow ↔ capital appreciation.
- **Hard filters** (price ceiling, minimum sleeps, maximum minutes to lift) are separate from
  **soft scores**. Filters exclude; scores rank. Conflating them hides why something vanished.
- **Confidence propagates.** A score built on low-confidence inputs is reported as low
  confidence, not silently averaged into apparent certainty.

Every score is reproducible from committed data plus committed config. Changing a weight and
re-running must change the ranking — that is the point of the dashboard as a decision tool.

### Opportunity detection

Rules are declarative and their firing is always explained. A flagged candidate shows *which*
signals fired — below-market pricing, large reduction, high capacity per dollar, existing
commercial licence, proximity, manageable renovation, strong projected NOI, favourable supply
balance, nearby funded infrastructure. `NEW HIGH-PRIORITY CANDIDATE` is never opaque.

---

## 8. Financial modelling

Per-asset models produce conservative / base / strong scenarios from explicit, labelled
assumptions. Every assumption is a named, sourced input — not a number embedded in a formula.

Headline output is **TOTAL PROJECT COST (AUD)**; purchase price is never treated as the
investment. Yield is reported on both purchase price and total project cost, and the gap between
them is itself a reported metric.

Owner use (2–4 weeks winter) is modelled as foregone revenue at peak rates, so its true cost is
visible rather than hidden. Assets with owner suites, manager apartments, lock-offs or separate
buildings are credited for reducing that cost.

Renovation is a first-class modelled quantity with three scenarios (minimum viable / good lodge
standard / premium repositioning), a `renovation_confidence` rating and an explicit
`renovation_contingency`. Estimates from listing photographs are ranges, never point figures.

---

## 9. Monitoring

Scheduled monitoring runs as GitHub Actions in `workflows/`, so continuity does not depend on a
local machine being awake.

| Cadence | Watches |
| --- | --- |
| Daily/frequent | Property listings, price changes, new and removed listings |
| Weekly | Developments, infrastructure, market news, business openings/closures |
| Monthly/quarterly | Tourism statistics, official market indicators |
| On release | Official land prices, planning data, regulatory changes |

**Collection ethics are a hard constraint, not a preference.** robots.txt, site terms, API
restrictions and rate limits are respected. Official APIs, government datasets and permitted
feeds are preferred over scraping. Sites that prohibit automated access are not scraped — where
that blocks a source, the blocker is documented in `SOURCES.md` and an alternative is sought.
Each source in the register records its `access_method`, `robots_ok` status and any terms note.

---

## 10. Dashboard

A decision tool, not a static report. Drill-down is
`Japan → Region → Town → Neighbourhood → Property → Financial Model`, with maps, rankings,
property cards, price history, comparables, town profiles, pipelines, supply, scenarios, risks,
source confidence and alerts.

Intended implementation: a **static site generated from the committed data**, deployable to
GitHub Pages at no cost, with filtering and re-weighting performed client-side. This keeps the
dashboard consistent with the no-paid-resources constraint and avoids a server that could drift
from the repository. Revisit only if client-side data volume makes it impractical.

---

## 11. Adding a new domain

1. Create `domains/<name>/` and `config/domains/<name>/`.
2. Define the domain's specialisations of the core generics — which `location_metric`s matter,
   what counts as a `market_catalyst`, what a `value_add_project` looks like.
3. Add domain schemas in `schemas/domains/<name>/` that extend the core schemas by
   `$ref`, adding domain fields without redefining core ones.
4. Add `weights.yaml`, thresholds and vocabularies to config.
5. Register ingestion sources in the source register with their tiers and access methods.

No change to `core/` should be required. **If adding a domain forces a change to `core/`, that
is a signal the core has leaked domain assumptions** — fix the leak rather than special-casing
the new domain.

---

## 12. Testing

Tests cover what is expensive to get silently wrong (master prompt §54):

- unit conversions and FX handling, including rate-date correctness;
- scoring maths, weight application and confidence propagation;
- filter semantics (a filter must never silently drop records for the wrong reason);
- snapshot diffing and event derivation;
- development-status weighting (a rumour must not score as a funded project);
- append-only invariants (no test may delete historical records);
- the core/domain boundary.

Run with `python3 -m unittest discover -s tests -v` — no install step.

---

## 13. Architectural decisions

Recorded with evidence, confidence and reversal triggers in [`DECISIONS.md`](DECISIONS.md).
The significant ones so far: two-layer split with an enforced boundary; JSON Schema as canonical
contract; stdlib-only core; data committed to git rather than a database; append-only history;
static dashboard; GitHub Actions for monitoring.
