# MASTER PROMPT

> **Status:** Authoritative project brief.
> **Received:** 2026-08-16.
> **Provenance:** Supplied verbatim by the repository owner. This file is the canonical
> statement of intent for the project. Where any other document in this repository conflicts
> with this file, this file governs, unless the owner has issued a later written instruction
> recorded in `DECISIONS.md`.
> **Editing rule:** Do not edit the body of this prompt. Later owner instructions are appended
> under "Amendments" at the end of the file, dated, and cross-referenced in `DECISIONS.md`.

---

You are taking over the GitHub repository:

`market-intelligence-engine`

This repository is to become a **reusable, persistent market-intelligence and opportunity-discovery platform** that can be used across multiple industries and asset classes.

The first domain/use case is:

# JAPAN SKI PROPERTY INTELLIGENCE

The initial users are two Australians investigating whether they can purchase an undervalued property near excellent Japanese skiing/snowboarding, use it personally, renovate or reposition it where appropriate, and operate it commercially as accommodation when they are not using it.

Potential property types include:

- houses
- chalets
- ski lodges
- pensions
- guesthouses
- ryokan
- small hotels
- former hotels
- commercial accommodation
- fixer-uppers
- multi-building properties

This is **not merely a property-search project**.

It is intended to become a living market-intelligence system that gets more valuable as historical data accumulates.

The system should ultimately help answer:

> What should we buy?

> Where should we buy it?

> Why there?

> What will it really cost us?

> What could it earn?

> What could go wrong?

> What is changing in that market?

> What has sold?

> What new opportunities have appeared?

> What infrastructure and accommodation supply are coming?

> What should we inspect first?

All conclusions should be supported by traceable evidence.

---

# 1. PRIMARY INVESTMENT THESIS

Test this thesis:

> Two Australians may be able to purchase an undervalued property close to genuinely excellent Japanese snow, renovate or reposition it into attractive accommodation, use it personally, have tourism materially support ownership costs, and potentially benefit from an emerging ski destination appreciating over the next 10–15 years.

Do NOT assume this thesis is correct.

Possible conclusions include:

- YES
- YES, but only above a certain capital level
- YES, but only in particular markets
- YES, but only with certain property types
- WATCH
- NO

Your purpose is to discover what the evidence supports.

---

# 2. CORE QUESTIONS

Ultimately answer:

> Where in Japan is the best intersection of excellent snow, relatively low property entry price, growing tourism, good town amenities, accommodation demand, manageable renovation, realistic remote operation, year-round potential and future capital appreciation?

Then:

> What property type and guest capacity produce the best economics?

Then:

> How much AUD capital would two Australians realistically need?

Then:

> Which actual properties should they inspect?

---

# 3. THIS MUST BE A REUSABLE ENGINE

Do NOT hard-code the entire application around Japanese ski property.

Architect it in two layers.

## CORE INTELLIGENCE ENGINE

Reusable functionality for:

- data ingestion
- entity tracking
- asset tracking
- source provenance
- source confidence
- historical snapshots
- time-series data
- transaction history
- change detection
- market indicators
- development pipelines
- catalysts
- risks
- scoring
- filters
- adjustable weightings
- alerts
- opportunity detection
- financial modelling
- dashboards
- decision logs
- scheduled monitoring
- research continuity

## DOMAIN MODULES

Domain-specific configuration and schemas.

First module:

`japan_ski_property`

Future modules might include:

- commercial property
- development sites
- businesses for sale
- pubs/hotels
- construction opportunities
- industrial property
- agricultural assets
- infrastructure-linked investments
- other countries
- other industries

Adding another domain should NOT require redesigning the core engine.

---

# 4. GITHUB IS THE CENTRAL SOURCE OF TRUTH

This project must support remote work.

The repository must not depend upon one local computer.

All meaningful:

- research
- data
- assumptions
- methodologies
- decisions
- prompts
- models
- schemas
- documentation
- outputs

must live in GitHub or in an appropriately documented external data store.

After every meaningful work unit:

1. update relevant files
2. update sources
3. update assumptions where necessary
4. update decisions where necessary
5. update next actions
6. commit
7. push to `origin/main`

Do not leave important completed work only on the local machine.

---

# 5. SAVE THIS MASTER PROMPT

Immediately save this entire prompt into:

`prompts/master-prompt.md`

This becomes the authoritative project brief.

Future agents must be able to understand the project without access to the original ChatGPT conversation.

---

# 6. AUTONOMOUS WORKING INSTRUCTION

Operate autonomously.

Do not stop and ask what to do next when the answer can reasonably be determined from:

- this master prompt
- repository documentation
- existing research
- existing data
- standard engineering practice
- standard investment-analysis practice
- standard research methodology

Work through independent tasks without requiring repeated user instructions.

If blocked on one source or task:

1. document the blocker
2. identify alternatives
3. continue productive independent work elsewhere

Only stop for owner input when:

- a decision genuinely requires owner preference
- credentials or permission are required
- proceeding could cause destructive external action
- proceeding could incur meaningful cost
- there is a genuine ambiguity that cannot responsibly be resolved
- no productive independent work remains

Before stopping:

- update `outputs/next-actions.md`
- update relevant documentation
- commit all valid work
- push to GitHub

Do not stop simply to announce that a phase has finished if productive work remains.

---

# 7. INITIAL REPOSITORY ARCHITECTURE

Inspect the existing repository first.

Then create or improve a structure approximately like:

```text
market-intelligence-engine/

README.md
PROJECT_BRIEF.md
ARCHITECTURE.md
RESEARCH_PLAN.md
ASSUMPTIONS.md
DECISIONS.md
SOURCES.md
CHANGELOG.md
.gitignore

config/
    core/
    domains/
        japan_ski_property/

data/
    raw/
    cleaned/
    snapshots/
    reference/
    history/
    property-listings/
    transactions/
    infrastructure/

domains/
    japan_ski_property/
        research/
        properties/
        tourism/
        property_market/
        business_activity/
        infrastructure/
        regulation/
        renovation/
        management/
        town_profiles/
        neighbourhoods/
        inspectors/
        financial_models/
        outputs/

analysis/
    scorecards/
    financial_models/
    scenarios/
    charts/

app/
    dashboard/
    api/

scripts/
    ingestion/
    monitoring/
    analysis/
    utilities/

workflows/

prompts/

outputs/
    next-actions.md
```

Improve this architecture where justified.

Document important decisions in:

`ARCHITECTURE.md`

---

# 8. INITIAL DOCUMENTATION

Create:

## README.md

Explain:

- purpose
- architecture
- repository structure
- setup
- remote workflow
- research methodology
- data provenance
- how another AI agent continues the work

## PROJECT_BRIEF.md

Document the complete investment thesis.

## ARCHITECTURE.md

Document the technical architecture.

## RESEARCH_PLAN.md

Document research phases.

## ASSUMPTIONS.md

Maintain explicit assumptions including:

- two Australian owners
- likely 50/50 ownership
- no fixed budget yet
- preference for low acquisition cost
- property should be close to good snow
- property should not be isolated from shops/restaurants
- fixer-uppers are acceptable
- owner use likely 2–4 weeks each winter
- local management will likely be required
- no assumption that Japanese debt is available

## DECISIONS.md

Maintain a dated decision log including:

- decision
- evidence
- confidence
- what would change the decision

## SOURCES.md

Maintain the source register.

## outputs/next-actions.md

Maintain continuity between sessions.

---

# 9. JAPAN-WIDE SEARCH

Do not assume Myoko is the winner.

Research broadly.

At minimum investigate:

- Myoko Kogen
- Madarao
- Nozawa Onsen
- Hakuba Valley
- lower-cost areas around Hakuba
- Furano
- Rusutsu
- Niseko
- Kutchan
- Moiwa
- Kiroro
- Appi Kogen
- Shiga Kogen
- Iiyama
- Arai
- Yuzawa
- other Hokkaido ski markets
- Tohoku
- overlooked/emerging Japanese ski towns

Actively discover additional locations.

---

# 10. LOCATION REQUIREMENTS

Cheap alone is not enough.

Serious accommodation candidates should generally be approximately:

- 0–5 minutes from skiing
- 5–10 minutes
- 10–15 minutes

Only consider significantly greater distances where the investment case is exceptional.

Track:

- nearest lift
- distance
- driving time
- walking time
- shuttle access
- supermarket
- convenience store
- restaurants
- bars
- pharmacy
- ski rentals
- ski school
- train
- Shinkansen
- airport
- taxi
- parking
- whether guests require a car

---

# 11. SKI AND SNOWBOARD QUALITY

For every serious area research:

- resorts
- skiable terrain
- vertical
- longest runs
- lift infrastructure
- terrain variety
- beginner terrain
- intermediate terrain
- advanced terrain
- tree skiing
- backcountry
- annual snowfall
- powder quality
- snow reliability
- season length
- elevation
- crowds
- lift queues
- inter-resort connectivity

Answer:

> Could a serious snowboarder happily spend seven days here?

Compare against Hakuba and Niseko.

---

# 12. TOWN FACILITIES AND VIBE

This is a major workstream.

For every serious destination produce a proper town profile.

Research:

- overall atmosphere
- traditional Japanese character
- internationalisation
- resort development
- family appeal
- snowboarder appeal
- premium appeal
- backpacker appeal
- restaurants
- bars
- nightlife
- après-ski
- cafés
- bakeries
- supermarkets
- convenience stores
- pharmacies
- medical facilities
- ATMs
- ski shops
- snowboard shops
- rentals
- ski schools
- onsens
- gyms
- laundromats
- taxis
- buses
- shuttles
- trains
- parking
- childcare
- English-language services

Determine:

- whether amenities are walkable
- whether guests need cars
- whether restaurants become booked out
- whether businesses close early
- whether the town remains active after skiing
- whether there is enough to do during bad weather
- whether non-skiers would enjoy it
- whether guests would enjoy staying for seven days
- whether guests are likely to return

Use multiple sources and distinguish objective facts from subjective observations.

---

# 13. SEVEN-DAY GUEST EXPERIENCE

For serious destinations model:

> Four Australian snowboarders book accommodation here for seven nights. What does their actual holiday look like?

Cover:

- arrival
- airport transfer
- property access
- groceries
- daily mountain transport
- equipment hire
- restaurants
- drinking/nightlife
- rest day
- non-ski activities
- bad-weather day
- transport friction
- overall convenience
- likely satisfaction
- likelihood of repeat visit

---

# 14. MICRO-LOCATION ANALYSIS

Do not treat a whole ski region as one market.

Break destinations into neighbourhoods/submarkets.

Identify:

- walk-to-lift locations
- nightlife locations
- family areas
- premium areas
- quieter areas
- value areas
- shuttle-dependent areas
- car-dependent areas
- potentially inconvenient cheap areas

Compare:

- property prices
- nightly rates
- occupancy
- walkability
- guest convenience
- amenity access

---

# 15. TEN-YEAR PROPERTY MARKET

Research approximately 2015–2026 and longer where reliable data exists.

Track:

- residential prices
- commercial prices
- land prices
- price per square metre
- transaction volume
- number of transactions
- foreign purchases where available
- hotel transactions
- development
- vacant property
- redevelopment

Calculate where possible:

- 1-year change
- 3-year change
- 5-year change
- 10-year change
- CAGR

Use official Japanese land-price data where appropriate.

Create charts.

---

# 16. NISEKO/HAKUBA DEVELOPMENT CURVES

Study approximately 15–25 years of development.

Track:

- foreign tourism
- property prices
- land prices
- accommodation
- foreign investment
- hotels
- restaurants
- businesses
- lift investment
- roads
- rail
- airports
- international exposure
- major developers

Compare emerging markets against historical stages.

Ask:

> Does this genuinely resemble an earlier stage of Hakuba or Niseko?

Do not force the answer.

---

# 17. BUSINESS FORMATION AND ECONOMIC ACTIVITY

Where data permits, track:

- business registrations
- business deregistrations
- net formation
- restaurants
- bars
- accommodation businesses
- tourism operators
- ski businesses
- property managers
- builders
- construction activity
- bankruptcies
- closures

If exact municipal data is unavailable, use credible proxies.

Ask:

> Is private capital actually entering this town?

---

# 18. TOURISM

Research approximately a decade.

Track:

- annual visitors
- winter visitors
- international visitors
- domestic visitors
- overnight stays
- length of stay
- occupancy
- ADR
- RevPAR where available
- visitor nationality
- Australian visitors
- repeat visitation
- tourism spending
- seasonality

Classify:

- accelerating
- steadily growing
- flat
- declining

---

# 19. OFF-SEASON / FOUR-SEASON MARKET

Analyse April–November separately.

Research:

- mountain biking
- hiking
- trail running
- golf
- rafting
- fishing
- climbing
- onsens
- food tourism
- festivals
- summer holidays
- autumn tourism
- events
- conferences
- local economy

Classify:

- winter-only
- winter-dominant
- emerging four-season
- genuine four-season

---

# 20. REAL PROPERTY DATABASE

Find actual current properties for sale.

Search Japanese and English sources.

Include:

- houses
- chalets
- pensions
- lodges
- guesthouses
- ryokan
- hotels
- former hotels
- commercial accommodation
- fixer-uppers
- multi-building sites
- owner/manager accommodation

For every property record:

- unique property ID
- listing URL
- source
- first seen
- last seen
- asking price JPY
- AUD conversion
- FX rate/date
- land size
- building size
- year built
- bedrooms
- bathrooms
- practical guest capacity
- property type
- current use
- licence status
- lift distance
- town distance
- supermarket distance
- amenity access
- renovation condition
- defects
- expected operating model
- listing status
- confidence

---

# 21. PRICE TIERS

Support:

- under AUD $200k
- $200k–$300k
- $300k–$400k
- $400k–$600k
- $600k–$800k
- $800k–$1m
- $1m–$1.5m
- $1.5m+

AUD must be the primary displayed currency.

---

# 22. PROPERTY HISTORY

Never delete old listings.

Maintain longitudinal history.

Track:

- first-seen date
- original asking price
- price changes
- final asking price
- last-seen date
- days on market
- sold status
- withdrawn status
- unknown status
- relisting
- confirmed sale price where obtainable
- inferred sale where clearly labelled
- transaction date
- buyer type where public
- condition at sale
- estimated renovation budget
- estimated all-in cost

This historical database should eventually become useful for comparable valuation.

---

# 23. RENOVATION BUDGET

Renovation is a first-class property metric and dashboard filter.

For each property estimate:

- acquisition costs
- legal
- due diligence
- renovation
- furnishing
- compliance
- working capital
- contingency
- total project cost

Break renovation into:

- kitchen
- bathrooms
- flooring
- painting
- electrical
- plumbing
- heating
- insulation
- glazing
- roof
- exterior
- structure
- snow-load upgrades
- fire compliance
- drying room
- ski storage
- furniture
- appliances

Create three scenarios:

## MINIMUM VIABLE

Get legally/commercially operational and presentable.

## GOOD LODGE STANDARD

Strong mid-market commercial finish.

## PREMIUM REPOSITIONING

Higher-end accommodation designed for stronger nightly rates.

Use realistic ranges.

Do not create false precision from online listings.

Track:

`renovation_confidence`

and:

`renovation_contingency`

---

# 24. TOTAL PROJECT COST

Headline investment metric:

> TOTAL PROJECT COST AUD

Calculate:

Purchase  
+ acquisition costs  
+ legal  
+ due diligence  
+ renovation  
+ furnishing  
+ licensing/compliance  
+ initial working capital  
+ contingency  
= TOTAL PROJECT COST

Purchase price alone must never be treated as the true investment cost.

---

# 25. BUILDING INSPECTORS AND CONSTRUCTION NETWORK

For every finalist region identify:

- independent building inspectors
- surveyors
- architects
- construction consultants
- builders
- project managers

Prioritise:

- English speakers
- Australians
- New Zealanders
- experienced expats
- Japanese professionals experienced with foreign clients

Record:

- person
- company
- region
- services
- qualifications where available
- inspection scope
- mountain-building experience
- foreign-buyer experience
- indicative fees
- contact/source
- independence/conflicts

Do not rely on selling agents for structural advice.

For serious properties recommend:

1. an independent structural/building inspection
2. a separate renovation/commercial-conversion estimate

---

# 26. GUEST CAPACITY

Do not assume the ideal number of guests.

Model:

- 6
- 8
- 10
- 12
- 16
- 20+
- larger lodge opportunities

Analyse:

- bedrooms
- bathrooms
- kitchen
- common areas
- drying room
- ski storage
- parking
- owner quarters
- manager quarters
- staff accommodation
- cleaning cost
- labour
- licence/compliance complexity
- revenue

Determine the optimal size economically.

---

# 27. REGULATION

This is critical.

Research:

- foreign ownership
- land ownership
- freehold
- leasehold
- Minpaku
- 180-day limitation
- Hotel Business Act
- hotel licences
- ryokan licences
- guesthouse/common lodging licences
- local municipal restrictions
- zoning
- fire
- evacuation
- food service
- building compliance
- change of use
- licence transferability
- taxation
- foreign-owner tax
- GK structures
- visa implications
- residency
- financing for Australian non-residents

Never assume a residential property can legally become commercial accommodation.

---

# 28. MANAGEMENT

Assume owners remain based in Australia.

Research local:

- property managers
- booking managers
- cleaners
- linen providers
- snow-clearing contractors
- maintenance
- guest communication
- check-in
- emergency support
- accountants
- tax administrators

Track actual providers where possible.

Management availability and cost must affect property ranking.

---

# 29. FINANCIAL MODEL

For serious candidates estimate:

- winter nightly rate
- peak rate
- shoulder rate
- summer rate
- occupancy
- gross annual revenue
- management
- cleaning
- utilities
- heating
- insurance
- snow clearing
- maintenance
- platform fees
- taxes
- capex reserve
- NOI
- yield on purchase price
- yield on total project cost

Create:

- Conservative
- Base
- Strong

Label assumptions clearly.

---

# 30. OWNER USE

Model approximately 2–4 weeks of owner use during winter.

Calculate lost accommodation revenue.

Give additional value to properties with:

- owner suites
- manager apartments
- lock-off areas
- detached buildings
- multiple accommodation units

---

# 31. DEVELOPMENT AND INFRASTRUCTURE INTELLIGENCE

Continuously monitor:

- proposed hotels
- approved hotels
- funded hotels
- hotels under construction
- completed hotels
- apartment developments
- proposed dwellings
- subdivisions
- lodges
- resort expansions
- new lifts
- gondolas
- lift upgrades
- roads
- rail
- Shinkansen
- airport improvements
- international flights
- town redevelopment
- mountain-bike infrastructure
- tourism infrastructure
- government spending
- private investment

For each development track:

- unique project ID
- name
- developer
- investor
- location
- project type
- estimated value
- hotel rooms
- residential units
- accommodation keys
- expected beds
- date announced
- planning status
- approval status
- funding status
- construction status
- expected completion
- latest update
- source
- confidence

Classify projects:

- rumoured
- proposed
- announced
- planning
- approved
- funded
- under construction
- completed
- cancelled

Never treat a proposal as equivalent to something under construction.

---

# 32. FUTURE ACCOMMODATION SUPPLY

Track by town:

- existing accommodation rooms
- existing beds
- proposed rooms
- approved rooms
- funded rooms
- rooms under construction
- newly completed rooms
- residential holiday-rental supply

Calculate:

> Forward Supply Ratio

and:

> Tourism Demand Growth versus Accommodation Supply Growth

This should materially affect investment scoring.

---

# 33. CONTINUOUS MONITORING

This system must eventually operate continuously.

Use scheduled workflows where practical.

GitHub Actions is appropriate for scheduled monitoring where technically and legally suitable.

Possible cadence:

## Daily / frequent

- property listings
- price changes
- new listings
- removed listings

## Weekly

- developments
- infrastructure
- major market news
- business openings/closures

## Monthly/quarterly

- tourism
- official statistics
- market indicators

## As released

- official land prices
- planning data
- regulatory changes

Respect:

- robots.txt
- website terms
- API restrictions
- rate limits

Prefer:

- official APIs
- government datasets
- feeds
- permitted public pages

Do not indiscriminately scrape prohibited websites.

---

# 34. SNAPSHOTS

Do not overwrite historical observations.

Store snapshots.

Every monitored asset/entity should have history.

The system should be able to answer:

> What did this listing look like six months ago?

and:

> What has changed?

---

# 35. CHANGE DETECTION

Detect:

- new property
- price reduction
- price increase
- property removed
- relisting
- likely sale
- confirmed sale
- development announced
- development approved
- development funded
- construction commenced
- development completed
- development cancelled
- new hotel
- new lift
- regulation change
- new tourism release
- land-price release
- major business opening
- major business closure

Preserve the event history.

---

# 36. OPPORTUNITY DETECTOR

Create transparent rules to identify unusually interesting opportunities.

Potential signals:

- below-market listing
- large price reduction
- high guest capacity per acquisition dollar
- existing commercial licence
- close to lifts
- close to town
- good walkability
- manageable renovation
- unusually attractive all-in cost
- strong projected NOI
- strong tourism growth
- limited new accommodation supply
- major nearby funded infrastructure
- increasing land values
- improving town economy

Flag:

`NEW HIGH-PRIORITY CANDIDATE`

Do not hide why it was flagged.

---

# 37. DASHBOARD FILTERS

The dashboard must allow the user to experiment.

Filters should include at minimum:

- country
- region
- town
- neighbourhood
- property type
- purchase price
- TOTAL PROJECT COST
- renovation budget
- renovation scenario
- bedrooms
- bathrooms
- guest capacity
- licence
- distance to lifts
- distance to town
- supermarket access
- walkability
- nightlife
- town vibe
- snow score
- terrain score
- tourism growth
- property-price growth
- business growth
- infrastructure score
- off-season score
- management availability
- projected revenue
- projected NOI
- yield
- risk
- listing age
- price reduction
- source confidence

Example query:

> Show properties under AUD $500,000 total project cost, sleeping at least 10, maximum 10 minutes from skiing, maximum 10 minutes from a supermarket, with strong snow, good town vibe and positive base-case NOI.

---

# 38. ADJUSTABLE WEIGHTINGS

Support adjustable scoring preferences.

Examples:

- investment return ↔ lifestyle
- cheap entry ↔ premium property
- established market ↔ emerging upside
- winter ↔ four-season
- turnkey ↔ renovation
- low risk ↔ high upside
- town life ↔ ski proximity
- cash flow ↔ capital appreciation

Do not permanently hard-code subjective preferences.

---

# 39. DASHBOARD

Build toward:

> Japan → Region → Town → Neighbourhood → Property → Financial Model

Dashboard should ultimately display:

- maps
- rankings
- filters
- property cards
- price history
- comparable properties
- town profiles
- ski metrics
- tourism trends
- business trends
- infrastructure pipeline
- development pipeline
- future supply
- renovation budgets
- financial scenarios
- risks
- source confidence
- alerts

Useful market KPIs include:

- median asking price
- median price/m²
- 12-month asking-price movement
- new listings
- removed listings
- price reductions
- median days on market
- qualifying properties
- tourism growth
- international visitor growth
- accommodation supply growth
- forward supply ratio
- development pipeline value

---

# 40. RISK

Actively try to destroy attractive investment theses.

Research:

- climate change
- snowfall trends
- demographic decline
- population decline
- accommodation oversupply
- labour shortages
- earthquakes
- volcanic risk
- avalanche
- flooding
- insurance
- FX
- tourism downturn
- regulatory change
- foreign ownership restrictions
- ageing lifts
- competition
- resale liquidity

For every apparently cheap area ask:

> Why is this cheap?

For every apparently emerging market ask:

> Why hasn't sophisticated capital already arbitraged this opportunity away?

---

# 41. EXIT STRATEGY

For every serious investment ask:

> Who buys this from us in 10–15 years?

Research:

- Japanese buyers
- foreign buyers
- owner operators
- hospitality groups
- institutional capital
- transaction liquidity
- selling costs
- likely exit difficulty

---

# 42. SCORECARD

Create a transparent weighted score.

Score out of 10:

- affordability
- ski quality
- snow reliability
- tourism growth
- rental demand
- winter occupancy
- off-season demand
- accessibility
- amenities
- town vibe
- management
- regulation
- renovation opportunity
- property-price momentum
- business growth
- infrastructure
- future supply balance
- capital-growth potential
- exit liquidity
- risk
- overall investment attractiveness

Weights must be visible and adjustable.

---

# 43. RESEARCH QUALITY

Prioritise:

1. Japanese government
2. prefectural government
3. municipal government
4. official tourism organisations
5. official land-price data
6. planning records
7. company filings
8. credible property data
9. reputable real-estate agencies
10. accommodation data
11. industry research
12. reputable media
13. community/anecdotal sources only where appropriate

Search Japanese-language sources.

For every material claim track:

- source
- URL
- date accessed
- publication date
- geography
- source type
- reliability
- confidence

Clearly distinguish:

`FACT`

`CALCULATION`

`ESTIMATE`

`ASSUMPTION`

`OPINION`

Do not invent missing data.

---

# 44. SOURCE PROVENANCE

Design the data architecture so important numbers can be traced back to their source.

Where possible each data point should include:

- source ID
- retrieval date
- original value
- units
- transformation
- confidence
- notes

This system should allow later auditing.

---

# 45. CURRENT PROPERTY SHORTLIST

Eventually maintain approximately 20–30 serious current opportunities.

Rank the best 10.

For finalists display:

- rank
- area
- town
- neighbourhood
- property
- AUD purchase price
- JPY price
- TOTAL PROJECT COST
- renovation budget
- bedrooms
- bathrooms
- guest capacity
- lift access
- town access
- licence
- projected gross revenue
- projected NOI
- yield
- risk
- investment thesis
- source confidence

---

# 46. FINAL RECOMMENDATIONS

Eventually identify:

- Best overall region
- Best emerging region
- Best established region
- Best snow/value
- Best four-season market
- Best town vibe
- Best under AUD $300k
- Best under AUD $400k
- Best under AUD $600k
- Best under AUD $1m
- Cheapest genuinely viable property
- Best fixer-upper
- Best operating lodge
- Best lifestyle investment
- Best pure investment
- Lowest-risk opportunity
- Highest-risk/highest-upside opportunity
- Market that initially looked attractive but should be rejected
- Property to inspect first

Do not finish with:

"It depends."

Make recommendations based on the available evidence.

---

# 47. CAPITAL REQUIRED

Create three strategies.

## SHOESTRING

Lowest amount at which you would responsibly attempt the investment.

## SENSIBLE

Enough capital to acquire something genuinely commercially viable without constantly fighting limitations.

## STRONG

Enough capital for a stronger asset with better revenue and resale prospects.

For each calculate:

- property
- acquisition costs
- tax
- legal
- due diligence
- renovation
- furnishing
- compliance
- insurance
- working capital
- contingency
- TOTAL CAPITAL
- capital per owner at 50/50

Report AUD first.

Initially assume no Japanese debt.

Separately research financing for Australian non-residents.

---

# 48. MARKET INTELLIGENCE OVER TIME

The platform should become more valuable as it runs.

Eventually it should be capable of producing observations such as:

> Myoko qualifying listings have fallen 18% in 12 months.

> Median asking prices increased 9%.

> Properties below AUD $400k are disappearing faster than higher-priced stock.

> International visitor nights increased 14%.

> 380 new hotel rooms are approved.

> 160 rooms are currently under construction.

> Tourism demand is growing faster than accommodation supply.

These statements must be generated from evidence, not invented.

---

# 49. GENERALISATION TO OTHER INDUSTRIES

Keep reusable concepts generic.

Examples:

Instead of embedding only:

`distance_to_ski_lift`

the core should support generic domain-defined:

`location_metrics`

Instead of only:

`property`

support:

`asset`

Instead of only:

`hotel development`

support:

`market_catalyst`

Instead of only:

`renovation`

support generic:

`value_add_project`

The Japan ski module can then specialise these concepts.

Document how another domain could be added later.

---

# 50. CONTINUITY BETWEEN AI AGENTS

Another agent opening the repo tomorrow must be able to understand:

- what this project is
- what has been built
- what has been researched
- current hypotheses
- current best opportunities
- unresolved questions
- known blockers
- next actions

At the end of every significant session update:

`outputs/next-actions.md`

Also maintain:

`DECISIONS.md`

`ASSUMPTIONS.md`

`SOURCES.md`

`CHANGELOG.md`

---

# 51. RESEARCH PHASES

Proceed approximately:

## Phase 1
Architecture and foundational repository

## Phase 2
Reusable core schemas

## Phase 3
Japan ski-property domain schemas

## Phase 4
Japan-wide destination screening

## Phase 5
Ski/snow analysis

## Phase 6
Town/vibe/micro-location analysis

## Phase 7
Historical property markets

## Phase 8
Tourism

## Phase 9
Business/economic activity

## Phase 10
Off-season economy

## Phase 11
Infrastructure/development pipeline

## Phase 12
Regulation

## Phase 13
Property collection

## Phase 14
Renovation/construction costs

## Phase 15
Inspector/contractor network

## Phase 16
Management

## Phase 17
Financial modelling

## Phase 18
Continuous monitoring

## Phase 19
Opportunity detection

## Phase 20
Dashboard

## Phase 21
Risk/counter-thesis

## Phase 22
Investment ranking

## Phase 23
Investment Committee recommendation

Parallelise independent research where practical.

Do not wait unnecessarily for one phase if other useful work can proceed.

---

# 52. INITIAL EXECUTION — START NOW

Do the following without waiting for further instruction:

1. Inspect the repository.

2. Save this entire prompt to:

`prompts/master-prompt.md`

3. Create the repository architecture.

4. Populate `README.md`.

5. Create `PROJECT_BRIEF.md`.

6. Create `ARCHITECTURE.md`.

7. Create `RESEARCH_PLAN.md`.

8. Create `ASSUMPTIONS.md`.

9. Create `DECISIONS.md`.

10. Create `SOURCES.md`.

11. Create `CHANGELOG.md`.

12. Create `outputs/next-actions.md`.

13. Create `.gitignore`.

14. Commit the foundational repository.

15. Push to `origin/main`.

16. Design the reusable core data model.

17. Design the Japan ski-property domain model.

18. Design property-history/snapshot models.

19. Design infrastructure/development pipeline models.

20. Design renovation-budget models.

21. Design source provenance/confidence models.

22. Design scoring/filter models.

23. Design continuous-monitoring architecture.

24. Design opportunity-detection architecture.

25. Design dashboard data model.

26. Commit and push.

27. Begin Japan-wide research.

28. Do NOT assume Myoko is the answer.

29. Continue autonomously through productive work.

---

# 53. SAFETY AROUND EXTERNAL ACTIONS

You may autonomously:

- create/edit repository files
- create directories
- run local development commands
- write code
- write tests
- run tests
- analyse data
- perform web research
- update documentation
- create commits
- push normal project commits to `origin/main`

Do NOT autonomously:

- spend money
- purchase paid APIs
- purchase property
- contact sellers
- contact agents
- contact inspectors
- contact contractors
- submit planning applications
- enter contracts
- create paid cloud resources
- expose credentials
- perform destructive external actions

Document these as future actions requiring owner approval where appropriate.

---

# 54. ENGINEERING STANDARD

Do not over-engineer prematurely.

Start with:

- clear schemas
- strong provenance
- clean modular architecture
- reproducible data
- historical snapshots
- simple reliable workflows

Then expand.

Prefer a simple working monitoring pipeline over a sophisticated theoretical architecture that never collects useful data.

Write tests for important transformations and scoring logic.

Keep configuration separate from core code.

---

# 55. PERMANENT MARKET MONITORING PRINCIPLE

This system should not only perform one-off research.

It should preserve longitudinal market history and maintain an "ear to the ground."

Continuously monitor where legally and technically practical:

- property listings
- price changes
- likely sales
- confirmed transactions
- business openings and closures
- tourism releases
- planning approvals
- infrastructure announcements
- hotel and dwelling pipelines
- new lifts and resort infrastructure
- regulatory changes
- new transport access
- major developers and investors entering a market
- local construction activity
- accommodation supply changes
- meaningful market news

When a property disappears from market, do not discard it.

Retain its full historic record for future comparable analysis.

Where a sale can be confirmed, record:

- original asking price
- final asking price
- sale price
- first-seen date
- last-seen date
- sale date
- days on market
- property attributes
- condition
- estimated renovation requirements
- original and final comparable valuation
- buyer type if public
- subsequent redevelopment or relisting where observable

Over time the platform should build its own proprietary historical comparison dataset.

---

# 56. DEVELOPMENT PIPELINE INTELLIGENCE PRINCIPLE

Keep a dedicated forward-looking pipeline for:

- hotels
- lodges
- pensions
- new dwellings
- subdivisions
- mixed-use developments
- resort expansions
- ski lifts
- gondolas
- mountain infrastructure
- transport projects
- Shinkansen projects
- roads
- airport links
- new airline services
- tourism infrastructure
- recreation infrastructure
- government spending
- private capital investment

Track expected new accommodation capacity so that rising tourism demand can always be compared with future supply.

The system must be able to distinguish:

- proposal
- marketing announcement
- planning application
- planning approval
- funding commitment
- construction commencement
- construction progress
- completion
- cancellation

Rumours should never be scored like funded projects.

---

# 57. DASHBOARD AND FILTERING PRINCIPLE

The eventual interface should be designed as a decision tool, not a static report.

Users should be able to change assumptions and immediately see rankings change.

Support:

- hard filters
- adjustable scoring weights
- property-level filters
- market-level filters
- renovation-budget filters
- total-project-cost filters
- return filters
- lifestyle filters
- town-vibe filters
- snow-quality filters
- infrastructure filters
- future-supply filters
- risk filters

The dashboard should make it easy to compare markets and test different strategies rather than forcing one fixed recommendation.

---

# 58. FINAL PRINCIPLE

The goal is NOT:

> Build a website about Japanese ski houses.

The goal is:

> Build a reusable market-intelligence system capable of discovering, monitoring, analysing and comparing opportunities over time, with Japanese ski property as its first real-world implementation.

The Japan module should eventually provide a defensible answer to:

- where should we invest?
- why?
- what asset type?
- how many guests should it accommodate?
- what will it really cost?
- what renovation is required?
- what is the expected return?
- how seasonal is the business?
- what town would guests actually enjoy?
- what is happening to local property values?
- what is happening to tourism?
- what businesses are opening and closing?
- what infrastructure is coming?
- how much competing accommodation supply is coming?
- what risks could destroy the thesis?
- who buys the property from us later?
- what should we physically inspect?
- how much money should we have available?

The correct result may be that no current opportunity is attractive.

That is an acceptable outcome.

The system exists to improve decision quality, not to justify a purchase.

---

# BEGIN

Start immediately.

Do not merely explain what you intend to do.

Create the foundational repository, save this master prompt, commit it, push it, and continue into the architecture and research work.

Operate autonomously until you genuinely require owner input or no productive independent work remains.

---

# AMENDMENTS

Later owner instructions that modify the brief above are recorded here, most recent first.
Each amendment must be dated and cross-referenced in `DECISIONS.md`.

*(No amendments recorded.)*
