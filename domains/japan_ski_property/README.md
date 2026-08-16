# Domain module: `japan_ski_property`

The first implementation of the engine. Everything here specialises the domain-agnostic
core; nothing here is imported by it.

## What this module adds to the core

| Core concept | This module's specialisation | Schema |
| --- | --- | --- |
| `asset` | Property — house, chalet, pension, lodge, ryokan, former hotel, multi-building | `schemas/domains/japan_ski_property/property.json` |
| `entity` (market) | Town, with a full amenity and vibe profile | `town_profile.json` |
| `entity` (submarket) | Neighbourhood, because a resort region is not one market | `neighbourhood.json` |
| `entity` (operator) | Ski area — terrain, lifts, and snow recorded twice over | `ski_area.json` |
| `value_add_project` | Renovation budget in three scenarios | `renovation_budget.json` |
| `market_catalyst` | Lifts, gondolas, hotels, rail, airports — status-laddered | core schema, domain `catalyst_type` |
| `entity` (person/org) | Managers, cleaners, inspectors, builders | `service_provider.json` |

## Configuration

| File | Contains |
| --- | --- |
| `config/domains/japan_ski_property/scoring_components.json` | The 20 scorecard dimensions, what each means and what it is derived from |
| `config/domains/japan_ski_property/weights.json` | Five weight profiles: balanced, pure investment, lifestyle, emerging upside, low risk |
| `config/domains/japan_ski_property/filters.json` | Price tiers, lift-proximity bands, capacity options, disqualification rules, opportunity signals |

Weights are config, never code. No profile represents the owners' stated preference — none
has been given, so `balanced` is a neutral default and is flagged as such.

## Domain-specific judgements encoded in the schemas

These are deliberate and worth knowing before extending anything here:

- **Snow is recorded twice.** `marketed_annual_snowfall_cm` and
  `measured_annual_snowfall_cm` are separate fields with separate sources. Resort marketing
  and meteorological records frequently disagree, and the measured station's elevation and
  distance are stored so the comparison stays honest — valley stations under-report mountain
  snowfall.
- **Licence status is a first-class field with `unknown` as a distinct value.** A property is
  never assumed to be lawfully operable as commercial accommodation. An existing
  *transferable* licence is one of the strongest value signals in this domain.
- **`condition_assessment_basis` is mandatory.** A renovation figure derived from listing
  photographs is labelled as such and cannot be presented as firm.
- **`inconvenient_cheap` is a nameable neighbourhood character.** The cheap-but-unviable
  submarket is the specific trap this analysis exists to avoid, so it has a name.
- **`why_cheap` is required for any submarket priced materially below its town.** Cheap
  usually means correctly priced for a reason not yet identified.
- **`pre_1981_seismic_standard`** is tracked because the 1981 seismic code revision divides
  the Japanese building stock into two materially different risk and cost profiles.
- **Owner and manager quarters are tracked separately**, because they determine whether owner
  use costs revenue at all.
- **`agent_contacted` and `contacted` default to false** and stay false. The engine never
  contacts agents, sellers, inspectors or contractors without explicit owner approval.
- **Off-season classification requires an `evidence_basis`.** A tourism board's strategy
  document is not demand.

## Gating criteria

Two components disqualify rather than merely score low (`scoring_components.json`):

1. **`regulation`** — if the intended operating model cannot be made lawful for that property
   type in that municipality, the candidate is out regardless of everything else.
2. **`management_availability`** — the owners remain in Australia. A town with no identified
   managers, cleaners or maintenance cannot be operated remotely.

Neither is applied as a *screening* filter. Absence of an English-language web presence is not
absence of providers, and filtering on it early would eliminate exactly the unfashionable
markets this project exists to find. They bite before any recommendation.

## Research content

Working research lives in the sibling directories — `research/`, `town_profiles/`,
`neighbourhoods/`, `tourism/`, `property_market/`, `business_activity/`, `infrastructure/`,
`regulation/`, `renovation/`, `management/`, `inspectors/`, `properties/`,
`financial_models/`, `outputs/`. Phase status is tracked in `RESEARCH_PLAN.md`.

## Adding another domain

Nothing in this module should need to be consulted to build the next one. Follow
`ARCHITECTURE.md` §11. If a second domain forces a change to `core/`, that is a leaked
abstraction to fix, not a special case to add.
