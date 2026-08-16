# Research Plan

Phases, their status, what each must produce, and how each can fail.

**Status legend:** `DONE` · `ACTIVE` · `PARTIAL` · `PENDING` · `BLOCKED`

Phases are ordered but **not strictly sequential**. Independent research is parallelised, and no
phase waits unnecessarily on another if useful work can proceed (master prompt §51).

---

## Status summary

| # | Phase | Status | Output location |
| --- | --- | --- | --- |
| 1 | Architecture and foundational repository | `DONE` | repo root, `ARCHITECTURE.md` |
| 2 | Reusable core schemas | `DONE` | `schemas/core/`, `core/models/` |
| 3 | Japan ski-property domain schemas | `DONE` | `schemas/domains/japan_ski_property/` |
| 4 | Japan-wide destination screening | `ACTIVE` | `domains/japan_ski_property/research/` |
| 5 | Ski / snow analysis | `PENDING` | `domains/japan_ski_property/research/` |
| 6 | Town, vibe and micro-location analysis | `PENDING` | `town_profiles/`, `neighbourhoods/` |
| 7 | Historical property markets | `PARTIAL` | `property_market/` |
| 8 | Tourism | `PENDING` | `tourism/` |
| 9 | Business and economic activity | `PENDING` | `business_activity/` |
| 10 | Off-season economy | `PENDING` | `research/` |
| 11 | Infrastructure and development pipeline | `PENDING` | `infrastructure/` |
| 12 | Regulation | `PARTIAL` | `regulation/` |
| 13 | Property collection | `PENDING` | `properties/`, `data/property-listings/` |
| 14 | Renovation and construction costs | `PENDING` | `renovation/` |
| 15 | Inspector and contractor network | `PENDING` | `inspectors/` |
| 16 | Management | `PENDING` | `management/` |
| 17 | Financial modelling | `PENDING` | `financial_models/` |
| 18 | Continuous monitoring | `PENDING` | `workflows/`, `scripts/monitoring/` |
| 19 | Opportunity detection | `PENDING` | `core/scoring/` |
| 20 | Dashboard | `PENDING` | `app/dashboard/` |
| 21 | Risk and counter-thesis | `PARTIAL` | `research/` |
| 22 | Investment ranking | `PENDING` | `outputs/` |
| 23 | Investment Committee recommendation | `PENDING` | `outputs/` |

---

## Phase detail

### Phase 1 — Architecture and foundational repository · `DONE`
Two-layer architecture, directory structure, core documentation, dependency policy, git and
remote workflow established.
**Fails if:** the core/domain boundary is not enforceable, or the repo depends on one machine.

### Phase 2 — Reusable core schemas · `DONE`
Domain-agnostic contracts: `source`, `observation`, `entity`, `asset`, `snapshot`, `event`,
`market_catalyst`, `value_add_project`, `location_metric`, `market_indicator`, `risk_factor`,
`score`, `financial_model`. Provenance and confidence built in at record level.
**Fails if:** a domain concept leaks into core, or an observation can exist without a source.

### Phase 3 — Japan ski-property domain schemas · `DONE`
Specialisations: property listing (with full attribute set from master prompt §20), town
profile, neighbourhood, ski area, renovation budget, development project, management provider,
inspector.
**Fails if:** schemas cannot represent a real listing found in Phase 13 without modification.

### Phase 4 — Japan-wide destination screening · `ACTIVE`
Screen the longlist (Nagano/Niigata, Hokkaido, Tohoku) plus actively discovered overlooked
towns. Produce a first-pass comparison on snow, access, entry price, tourism trajectory, town
substance and supply pressure. Narrow to a serious set for deep research.
**Must not:** assume Myoko, or any location, is the answer.
**Fails if:** the screen is a list of famous resorts rather than a genuine search including
unfashionable markets.

### Phase 5 — Ski / snow analysis · `PENDING`
Per serious area: resorts, terrain, vertical, lifts, terrain mix, tree skiing, backcountry,
snowfall, powder quality, snow reliability, season length, elevation, crowds, connectivity.
Answer *could a serious snowboarder happily spend seven days here?* against Hakuba and Niseko.
**Fails if:** it reports marketing snowfall claims as fact, or ignores multi-year snow trend.

### Phase 6 — Town, vibe and micro-location analysis · `PENDING`
Full town profiles (amenities, dining, après, medical, transport, English services, bad-weather
options) and the seven-day guest experience model. Decompose each destination into
neighbourhoods with their own price and convenience characteristics.
**Fails if:** a whole resort region is treated as one market, or vibe claims are unsourced.

### Phase 7 — Historical property markets · `PARTIAL`
~2015–2026 and longer where reliable: residential, commercial and land prices, price/m²,
transaction volume, vacancy, redevelopment. Compute 1/3/5/10-year change and CAGR. Charts.
Use official Japanese land-price data (地価公示 / 都道府県地価調査).
**Fails if:** asking prices are conflated with transaction prices.

### Phase 8 — Tourism · `PENDING`
~10 years: total, winter, international and domestic visitors, overnight stays, length of stay,
occupancy, ADR, RevPAR, nationality mix, Australian share, repeat visitation, spend, seasonality.
Classify each market: accelerating / steadily growing / flat / declining.
**Fails if:** national trends are used as a proxy for a specific town without saying so.

### Phase 9 — Business and economic activity · `PENDING`
Registrations, deregistrations, net formation, hospitality and accommodation businesses,
construction activity, closures. Credible proxies where municipal data is unavailable.
Answer: *is private capital actually entering this town?*
**Fails if:** proxies are presented as direct measurement.

### Phase 10 — Off-season economy · `PENDING`
April–November: biking, hiking, golf, rafting, onsen, food, festivals, events. Classify:
winter-only / winter-dominant / emerging four-season / genuine four-season.
**Fails if:** aspirational tourism-board plans are counted as existing demand.

### Phase 11 — Infrastructure and development pipeline · `PENDING`
Hotels, lodges, dwellings, subdivisions, resort expansions, lifts, gondolas, roads, rail,
Shinkansen, airports, air routes. Every project status-classified on the ladder and never
scored above its status. Forward accommodation supply by town.
**Fails if:** a rumour is counted like a funded project.

### Phase 12 — Regulation · `PARTIAL`
Foreign ownership, freehold/leasehold, minpaku and the 180-day limit, Hotel Business Act, hotel
/ ryokan / simple-lodging licences, municipal restrictions, zoning, fire, evacuation, food
service, change of use, licence transferability, taxation, GK structures, visas, and financing
for Australian non-residents.
**Gating:** a market where the operating model is not legal is disqualified regardless of score.
**Fails if:** it assumes a residential property can become commercial accommodation.

### Phase 13 — Property collection · `PENDING`
Real current listings from Japanese and English sources, full attribute set, provenance, and
append-only history from first sighting. Target ~20–30 serious opportunities.
**Fails if:** collection breaches site terms, or history is overwritten on re-crawl.

### Phase 14 — Renovation and construction costs · `PENDING`
Component-level costs; three scenarios (minimum viable / good lodge standard / premium
repositioning); mountain-specific items — snow load, insulation, glazing, heating, drying room,
ski storage, fire compliance. Ranges with `renovation_confidence` and `renovation_contingency`.
**Fails if:** it manufactures precision from listing photographs.

### Phase 15 — Inspector and contractor network · `PENDING`
Independent inspectors, surveyors, architects, builders and project managers per finalist
region, with foreign-client experience and indicative fees.
**Constraint:** research only. **No contact without owner approval.**
**Fails if:** selling agents are relied on for structural advice.

### Phase 16 — Management · `PENDING`
Property and booking managers, cleaners, linen, snow clearing, maintenance, guest comms,
emergency support, accountants. Availability and cost feed property ranking.
**Fails if:** remote operation is assumed feasible without identifying actual providers.

### Phase 17 — Financial modelling · `PENDING`
Per candidate: rates by season, occupancy, gross revenue, full operating costs, NOI, yield on
purchase price and on total project cost. Conservative / base / strong. Owner use as foregone
revenue. Capacity optimisation across 6/8/10/12/16/20+ guests.
**Fails if:** assumptions are not individually labelled and sourced.

### Phase 18 — Continuous monitoring · `PENDING`
GitHub Actions on the cadences in `ARCHITECTURE.md` §9, respecting robots.txt, terms and rate
limits. A simple pipeline that reliably collects beats a sophisticated one that never runs.
**Fails if:** it collects from prohibited sources, or silently stops without alerting.

### Phase 19 — Opportunity detection · `PENDING`
Declarative, explainable rules producing `NEW HIGH-PRIORITY CANDIDATE` flags with visible
reasons.
**Fails if:** a flag cannot be explained from committed data and config.

### Phase 20 — Dashboard · `PENDING`
Static, client-side-filterable decision tool with adjustable weights and full drill-down.
**Fails if:** changing a weight does not change the ranking, or provenance is not surfaced.

### Phase 21 — Risk and counter-thesis · `PARTIAL`
Structured attempt to destroy every attractive conclusion: climate and snow trend, depopulation,
oversupply, labour, seismic and volcanic, avalanche, flood, insurance, FX, tourism shock,
regulatory change, ageing lifts, competition, resale liquidity. Plus, per market: *why is this
cheap?* and *why hasn't sophisticated capital arbitraged this away?* Exit analysis: *who buys
this from us in 10–15 years?*
**Fails if:** it is written after the recommendation to justify it.

### Phase 22 — Investment ranking · `PENDING`
~20–30 opportunities scored, best 10 ranked, each with thesis, total project cost, projected
NOI, yield, risk and source confidence.
**Fails if:** ranking is not reproducible from committed data and config.

### Phase 23 — Investment Committee recommendation · `PENDING`
Named bests by category (region, emerging, established, snow/value, four-season, vibe, price
tiers, fixer-upper, operating lodge, lifestyle, pure investment, lowest risk, highest upside),
markets to **reject**, property to inspect first, and capital strategies (shoestring / sensible /
strong) with per-owner figures at 50/50.
**Must not** conclude "it depends". A `NO` or `WATCH` verdict is acceptable and must be stated
plainly if that is what the evidence supports.

---

## Cross-cutting requirements

Applied in every phase, not deferred to a review at the end:

- **Provenance.** Every material claim carries source, URL, access date, publication date and
  confidence. Claims are typed `FACT` / `CALCULATION` / `ESTIMATE` / `ASSUMPTION` / `OPINION`.
- **Japanese-language sources** are searched, not only English ones. English-only research
  systematically over-weights the internationalised markets — precisely the ones least likely to
  be undervalued.
- **Append-only history.** Nothing observed is deleted.
- **No invention.** Missing data is recorded as missing.
- **Continuity.** `outputs/next-actions.md`, `DECISIONS.md`, `ASSUMPTIONS.md`, `SOURCES.md` and
  `CHANGELOG.md` are updated as work proceeds, and committed and pushed to `origin/main`.
