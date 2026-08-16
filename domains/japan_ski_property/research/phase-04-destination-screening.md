# Phase 4 — Japan-wide destination screening

**Status:** In progress — first pass
**Started:** 2026-08-16
**Last updated:** 2026-08-16

> **Nothing here is a recommendation.** This is a first screening pass built on a small number
> of sources. Several headline figures are still `UNVERIFIED` against primary data and are
> marked as such. No destination has been selected or eliminated.

---

## 1. Method

The master prompt's named longlist is the **starting point, not the search space** (`DECISIONS.md`
D-0008). Screening proceeds on:

1. **Official land-price data** — direction and magnitude of the local property market.
2. **Population trajectory** — the constraint most often ignored in resort investment.
3. **Narrative provenance** — *who* is promoting each market, and what they stand to gain.
4. **Snow, town substance and access** — deferred to Phases 5–6 for the surviving set.

Step 3 is deliberate. In a market where much of the accessible English-language commentary is
published by agencies and developers, screening on sentiment alone would reliably select the
markets with the best marketing rather than the best fundamentals.

---

## 2. The headline tension

The single most useful finding of this pass is a **contradiction between narrative and official
data**.

| Market | Official land-price signal (2026) | Narrative in accessible commentary |
| --- | --- | --- |
| Hakuba | Strongest residential rise **in Japan** | "Beaten to it, already expensive" |
| Kutchan / Niseko | Strong continued rises | "Corporatised, priced out" |
| **Myoko** | **Flat to slightly negative** | **"The next big thing"** |

`FACT` — Hakuba Village recorded the largest residential land-price increase nationwide in the
2026 published land prices, at **+33.0%** [S1, S2].

`FACT` — Chitose recorded the largest commercial increase nationwide, at **+44.1%** [S2].

`FACT` (corroborated) — 2026 公示地価 municipal averages, now confirmed by a second independent
source [S10] agreeing with [S3] to within 0.02 percentage points:

| Market | Avg ¥/m² | Change | National rank | Regime |
| --- | --- | --- | --- | --- |
| Kutchan / Niseko | 120,750 | +12.33% | 21 | Established, still rising |
| **Hakuba** | 25,556 | **+26.93%** | **1** | Recovering strongly |
| **Nozawa Onsen** | 29,350 | **+21.69%** | **2** | Recovering strongly |
| Furano | 35,760 | +6.73% | 56 | Rising moderately |
| **Yuzawa** | 28,100 | **−0.44%** | — | Still declining |
| **Myoko** | 19,904 | **−0.79%** | — | Bottomed but flat |

Full analysis, including 30-year histories and the within-town spread, is in
[`../property_market/land-price-regimes.md`](../property_market/land-price-regimes.md). Three
findings from it change this screen materially:

1. **Nozawa Onsen is the national #2 performer** and was barely present in the promotional
   narrative that shaped the first pass. An evidence-led screen surfaces it; a sentiment-led one
   would not have.
2. **Yuzawa is a documented 33-year value trap** — down 85% from its 1993 peak and still falling,
   despite Shinkansen access, snow and cheap stock. It is now the benchmark every cheap candidate
   must be tested against.
3. **The within-town price spread (11–14×) is roughly double the between-town spread (~6×).**
   Choosing the right neighbourhood matters about twice as much as choosing the right town.

Direct MLIT retrieval is still outstanding and is required before these figures support a final
recommendation.

### Why this matters

Myoko is the market being marketed hardest to exactly the buyer this project describes —
Australians priced out of Niseko and Hakuba — while its official land values are, on the best
figures currently available, *not rising*. That is not automatically disqualifying. It is
plausibly what an early-stage market looks like before capital arrives. But it means the
Myoko thesis rests on **anticipated** rather than **realised** appreciation, and the entity
promoting it most loudly has a direct financial interest in that anticipation.

---

## 3. Narrative provenance — who is telling this story

`FACT` — The Myoko development is by **Patience Capital Group (PCG)**, a Singaporean investment
firm founded in 2019 by Ken Chan, formerly of GIC [S4, S5].

`FACT` — Reported scale: a **350-hectare** resort, ~**US$1.4bn / S$1.8bn**, first stage
targeted for completion in **2028**, first-stage investment up to **¥70bn**, with **¥35bn**
raised from investors including Mizuho Bank, Temasek's Pavilion Capital and a Singapore
university endowment [S4, S5].

`OPINION` / **conflict noted** — `patiencerealty.com`, which publishes land-price commentary
highlighting ski markets, is a **real estate brokerage** [S2]. It shares the "Patience" name
with PCG. Several other frequently-surfacing sources on "emerging" Japanese ski markets are
likewise agencies with transaction interests.

**Consequence for this project:** commentary promoting Myoko is registered at Tier 4–5 with an
explicit conflict note, and cannot support a material investment claim on its own. The PCG
development itself is a legitimate `market_catalyst` — but its status is what matters.

`FACT` — Local residents have expressed concern about overdevelopment, inflation and loss of
traditional character [S6].

That local resistance is itself investment-relevant: it is a leading indicator of the
municipal lodging restrictions that Phase 12 must check.

---

## 4. The catalyst-status discipline, applied

The PCG project is the clearest test of the rule that a proposal must never score like a funded
project (`ARCHITECTURE.md` §6).

| Attribute | Value | Confidence |
| --- | --- | --- |
| Status | **funded** (partially — ¥35bn of up to ¥70bn raised) | Medium |
| Weight applied | 0.8 of nominal (per `config/core/engine.json`) | — |
| First stage completion | 2028 | Low — developer-stated |
| Accommodation capacity added | **Not yet established** | — |

Until the added room and bed count is established, this project **cannot** be entered into the
forward supply ratio. A 350-hectare resort could plausibly add enough accommodation to depress
the very nightly rates the investment thesis depends on. **A large nearby development is not
unambiguously good news for a small operator** — it raises the destination's profile and its
competing supply at the same time, and which effect dominates is an empirical question, not a
rhetorical one.

This is a priority Phase 11 task.

---

## 5. Population — the constraint the marketing omits

`UNVERIFIED` — Myoko's population is projected to fall **−24.7% between 2020 and 2035** [S3].

If confirmed against IPSS municipal projections, this is material to:

- **Labour** — the cleaners, managers and maintenance contractors that remote ownership
  requires (gating assumption C2);
- **Amenities** — the restaurants and services that make a town worth a seven-night stay;
- **Exit** — the domestic buyer pool in 10–15 years.

Severe depopulation is not unique to Myoko; it is the Japanese rural baseline, and it applies
in some degree to nearly every market on the longlist. That is precisely why it must be
measured per municipality rather than assumed away. **Verifying this for every longlist town is
a Phase 4 completion requirement.**

It also supplies the honest answer to *"why is this cheap?"* for much of rural Japan: a
shrinking population with a large surplus housing stock. The investment question is whether
tourism demand can decouple a specific town from that trend — which is testable, and is what
Phases 8–11 test.

---

## 6. Regulatory baseline — a gating question, partly resolved

Researched early because it can disqualify markets and property types outright. Full detail in
[`../regulation/regulatory-baseline.md`](../regulation/regulatory-baseline.md).

**Resolved favourably:**

`FACT` — Foreigners may own land and buildings in Japan freehold, with no nationality-based
restriction and no nationality-based tax surcharge [S7, S8].

**The real constraint is the licence, not the buyer.** Operating category determines the
business:

| Category | Annual operating limit | Practical implication |
| --- | --- | --- |
| 住宅宿泊事業法 minpaku | **180 nights** | Caps the year, not necessarily the season |
| 旅館業法 simple lodging (簡易宿所) | Unlimited | The category most likely to fit a small lodge |
| 旅館業法 ryokan / hotel | Unlimited | Higher fire, safety and management thresholds |

**A non-obvious point that materially affects screening:** the 180-night cap is severe for a
year-round urban rental, but a winter-dominant ski property has a sellable core season well
under 180 nights. **The cap may not bind at all on winter trading** — what it forecloses is the
four-season upside (§19 of the brief). So minpaku-only status is a constraint on the
*diversification* case rather than on the *core* case, and should be scored that way rather
than treated as fatal.

`FACT` — Municipalities may impose stricter local ordinances (条例), including zones where
minpaku may operate zero days [S9]. This is decided **locally**, which is why municipal sources
are registered per town rather than nationally.

`FACT` — Acquisition costs run approximately **6–8% above purchase price** — agent commission
~3.3% incl. consumption tax, registration/transfer tax 1.5% land and 2.0% buildings, and
acquisition tax ~3% of assessed value [S7, S8]. These now have an evidenced basis in the
capital stack rather than a placeholder.

`FACT` — Non-resident purchasers must file a report with the Ministry of Finance within **20
days** of purchase; failure carries penalties up to 6 months imprisonment or ¥500,000 [S7].

---

## 7. Preliminary tiering

**Provisional. Based on market-level signals only — no snow, town or property analysis yet.**

### Tier A — proven appreciation, highest entry cost
Niseko / Kutchan, Hakuba.
Deep infrastructure and demonstrated exit liquidity, which most of the longlist lacks. The
affordability thesis is hardest here — but note that Hakuba remains **54% below its 1995 peak**,
so "too expensive" is a claim about the last seven years, not the last thirty. **Hakuba's
lower-cost fringes (Otari, outer valley) are a specific priority**: a +33% benchmark point does
not describe an 11×-spread valley.

### Tier A− — promoted on evidence: Nozawa Onsen
**Moved up from Tier B.** National **#2** for land-price appreciation (+21.69%), with strong
traditional character and an established onsen town — and materially less promotional coverage
than Myoko. This is the clearest case in the screen of evidence and narrative pointing in
different directions. Requires full Phase 5–6 research.

### Tier B — the "emerging" candidate, requiring the most sceptical treatment
Myoko Kogen, Madarao.
Myoko carries a genuine funded catalyst (PCG) and a genuine land-price contradiction
simultaneously: bottomed in 2022, up only ~5% since, still negative year-on-year. The case rests
on **anticipated** repricing. That is a legitimate investment posture, but it must be stated as
such — and it produces a falsifiable, monitorable prediction (land prices should turn positive as
2028 approaches).

### Tier C — cautionary benchmark: Yuzawa
**Moved out of "under-researched".** Down **85% from its 1993 peak** and still falling, with
Shinkansen access and abundant cheap stock. Not a candidate, but the most useful market on the
list: **every cheap candidate must answer "what is different here that was not true of
Yuzawa?"** A market that cannot has not been distinguished from a documented 33-year decline.

### Tier D — under-researched, no position taken
Furano (+6.73%, moderate riser), Rusutsu, Kiroro, Moiwa, Appi Kogen, Shiga Kogen, Iiyama (which
contains Madarao), Arai, other Hokkaido and Tohoku markets.
Absence reflects **research not yet done**, not adverse findings.

### Not yet searched — required before Phase 4 closes
Actively discovered towns beyond the named longlist, per master prompt §9. **The screen is not
complete until it has looked where the marketing does not.**

---

## 8. What this pass does not establish

Recorded explicitly so that later readers do not over-read this document:

- No snowfall data has been gathered. No claim about snow quality is made anywhere above.
- No property listings have been collected. No price point is evidenced.
- No town amenity, vibe or guest-experience research has been done.
- No tourism series has been retrieved.
- No management or inspector availability has been established for any town.
- Land-price figures for individual markets remain `UNVERIFIED` against primary MLIT data.
- Population projections remain `UNVERIFIED` against IPSS.

---

## 9. Next actions for this phase

1. Retrieve per-municipality 2026 land prices directly from `JP-MLIT-CHIKA` and replace every
   `UNVERIFIED` figure above. **Highest priority** — the tension in §2 is the pass's main
   finding and currently rests on secondary reporting.
2. Retrieve IPSS municipal population projections for every longlist town.
3. Establish the PCG development's accommodation capacity, for forward supply.
4. Retrieve JMA measured snowfall for candidate towns and compare against marketed figures.
5. Pull `JP-JTA-SHUKUHAKU` accommodation data for Niigata, Nagano and Hokkaido.
6. Actively discover overlooked towns outside the named longlist.
7. Check municipal minpaku ordinances for Myoko, Hakuba, Nozawa, Madarao and Kutchan.

---

## Sources cited

| Ref | Source | Tier | Accessed | Note |
| --- | --- | --- | --- | --- |
| S1 | MLIT 令和8年地価公示 press release | 1 | 2026-08-16 | Confirms 2026-03-17 publication, 26,000 points, 5th consecutive year of rises. Does **not** contain per-town figures. |
| S2 | Patience Realty commentary | 4 | 2026-08-16 | **Conflict: brokerage.** Source of the +33.0% Hakuba and +44.1% Chitose national-ranking figures. |
| S3 | Aggregated secondary property commentary | 5 | 2026-08-16 | Source of per-market averages and the Myoko population projection. All `UNVERIFIED`. |
| S4 | Mothership.SG | 5 | 2026-08-16 | PCG development scale and funding. |
| S5 | Bloomberg reporting, via secondary | 5 | 2026-08-16 | PCG founder, ambition, timeline. |
| S6 | Japan Today / Financial Express | 5 | 2026-08-16 | Local concern about foreign investment. Japan Today direct fetch returned **HTTP 403**; recorded in `SOURCES.md`. |
| S7 | Japanese property tax and ownership guides | 4 | 2026-08-16 | Foreign ownership rights, acquisition costs, MoF reporting. |
| S8 | Multiple independent property guides | 4 | 2026-08-16 | Corroborates S7 on ownership and costs. |
| S9 | Minpaku regulation commentary | 4 | 2026-08-16 | 180-day cap, licence categories, municipal ordinance powers. |
| S10 | tochidai.info — aggregator of official MLIT land-price data | 4 | 2026-08-16 | Municipal 公示地価 averages, change rates, national rankings, 30-year histories, highest/lowest points. Independently corroborates S3. |
| S11 | MLIT 令和8年地価公示 portal page + Nagano regional reporting | 1–5 | 2026-08-16 | Publication date 令和8年3月18日; benchmark points 白馬-1 (¥27,400/m², +33.0%, prior year +29.6%) and 白馬5-1 (¥40,300/m², +35.2%); MLIT commentary attributing Hakuba's rise to foreign buyers **opening accommodation businesses**. |

**Source-quality caveat.** This pass leans on Tier 4–5 commercial commentary because it was the
fastest route to a first orientation. Every material figure is flagged accordingly, and Phase 4
cannot close until the Tier 1 sources in §9 have replaced them. Several sources have direct
transactional interests in the markets they describe.
