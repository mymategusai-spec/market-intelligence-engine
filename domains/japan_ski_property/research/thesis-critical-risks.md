# Thesis-critical risks — snow and depopulation

**Phase:** 21 (risk / counter-thesis), brought forward · feeds Phase 5 (snow) and Phase 4
**Status:** First substantive pass. Two risks materially advanced; both remain open.
**Last updated:** 2026-08-16

> Brought forward deliberately. `ASSUMPTIONS.md` flags **E3** (snow viable over 10–15 years) as a
> gating assumption that can invalidate the entire thesis. Researching it *after* selecting a
> market would be researching to confirm a decision already made.

---

## 1. Snow: the risk is real, and it is elevation-specific

The headline is worse than expected, and the detail is more useful than the headline.

### The industry-level fact

`FACT` — The number of operational ski resorts in Japan fell in 2025 to a **record low, 40%
below the 1999 peak**, attributed to lack of snow driven by climate change [R1].

`FACT` — In Hakuba, snow is being **gathered and piled onto the highest course** to keep
operations going; at lower-elevation resorts, operating at all has become extremely difficult
[R1].

That second fact is worth pausing on. Hakuba is the **fastest-appreciating land market in
Japan** and is simultaneously managing snow scarcity on its own mountain. Land prices and snow
reliability are not measuring the same thing, and one is not evidence for the other.

### The detail that changes screening

`FACT` — Long-term trends 1961/62–2011/12: **marked snowfall reductions at Takada and Fukui**;
**no clear long-term reduction at Sapporo and Akita**. The decline appears to begin around 1990
[R2].

`FACT` — Over 1959–2020: significant **decreasing** trends in annual maximum snow depth and
maximum daily snowfall **at lower elevations** on the Japan Sea side of eastern and western
Japan — while **at higher elevations in eastern Japan** there is **no trend** in maximum snow
depth and a significant **increasing** trend in maximum daily snowfall [R3].

So the risk is not uniform. Three regimes:

| Regime | Snow trend | Implication |
| --- | --- | --- |
| Low elevation, Japan Sea side, Honshu | **Declining** | Structural risk to the asset's core product |
| High elevation, eastern Honshu | Stable depth, **heavier** snowfall events | Materially more defensible |
| Hokkaido | No clear long-term reduction | Most defensible of the three |

**Takada matters directly.** 高田 is in Jōetsu, Niigata — immediately adjacent to Myoko, on the
Japan Sea side. It is the nearest long-record station to the Myoko market and it is one of the
two stations named as showing marked decline. It is a **lowland valley station**, so it does not
measure the snow on Myoko's upper mountain — but it is the best long-run local signal available,
and it points down.

This is exactly why `ski_area.json` stores the measuring station's **distance and elevation**
alongside every measured snowfall figure. A valley station's decline is evidence about the
valley — where the village, the property and the road access are — even when the upper mountain
holds.

### Base elevations of the candidate markets

`FACT` [R4]:

| Resort | Base | Top | Vertical |
| --- | --- | --- | --- |
| Hakuba Happo-One | **760 m** | 1,831 m | 1,071 m |
| Myoko Akakura | ~730 m | — | — |
| Nozawa Onsen | **565 m** | 1,650 m | 1,085 m |
| Niseko Grand Hirafu | **260 m** | 1,200 m | 940 m |

Two observations:

- **Nozawa has the lowest base of the Honshu candidates** (565 m) despite the largest vertical.
  Its upper mountain is well protected; its **village and lower slopes are the most exposed** of
  the three. Since the village is where the property would be, this is a genuine caution against
  the market the land-price data just promoted.
- **Niseko's 260 m base looks alarming until regime is applied.** Hokkaido shows no clear
  long-term reduction, and Niseko's snow comes from a colder Siberian regime. Elevation cannot be
  compared across regions.

### A figure deliberately not recorded

One source reported Myoko Kogen with a top station of 2,454 m and **1,724 m vertical** [R4].
This is not credible and has been **rejected rather than stored**: 2,454 m is the summit of Mt
Myōkō, which the lifts do not reach, and the same search result states that only five Japanese
resorts exceed 1,000 m vertical — listing Nozawa (1,085 m) and Happo (1,071 m), but not Myoko.
A 1,724 m vertical would make Myoko comfortably Japan's largest, contradicting the source's own
data.

Recorded here as an example of the aggregation errors that propagate through ski-resort
statistics, and of why marketed figures are stored separately from measured ones.

### What this does to assumption E3

| | Before | After |
| --- | --- | --- |
| E3 — snow viable 10–15 years | `TESTING`, Low | `TESTING`, **Low–Medium, and now differentiated by market** |

Not resolved — but no longer a single yes/no question. The right question is *"is snow viable
**at this elevation, in this regional regime**, over 10–15 years?"*, and that is answerable per
candidate.

**Consequence for screening: base elevation and regional snow regime become first-class
criteria.** This creates direct tension with the affordability thesis, since the cheap Honshu
markets tend to be lower-elevation Japan Sea side. That tension is a finding, not a problem to
be smoothed over.

### Still required
- JMA station data for each candidate: 30+ year series, with station elevation and distance.
- Season-length trend, not just snowfall totals — season length drives revenue.
- Resort-level snowmaking capability and water rights.
- Which of the 40% of closed resorts closed *near* candidate markets — a closure next door is
  both a warning and a competitive change.

---

## 2. Depopulation: severe, and worst in the cheapest market

`FACT` — **Myoko City is projected to fall 46.7% between 2020 and 2050**, to roughly 16,200
people [R5], from IPSS's 2023 municipal projections.

Nearly half the resident population, over a period that spans and outlasts the owners' 10–15
year horizon.

`FACT` — In Hokkaido, by 2050 **more than two-thirds of municipalities (129)** are projected to
fall to 60% or less of current population, and **67 municipalities to 50% or less** [R6].

This is the Japanese rural baseline, not a Myoko peculiarity. But its severity in Myoko is
directly relevant, because Myoko is the market whose investment case rests on **anticipated**
appreciation.

### Why this bites on this specific thesis

The owners intend to live in Australia and operate remotely. That model consumes local labour:

- **Management** — `ASSUMPTIONS.md` C2, already a low-confidence gating assumption.
- **Cleaning and turnover** — the highest-frequency operational dependency.
- **Maintenance, snow clearing, emergency response** — the 24/7 contact that minpaku
  registration *legally requires* (see [regulatory baseline](../regulation/regulatory-baseline.md)).
- **The town itself** — restaurants, shops and services are what make a seven-night stay
  saleable. They are staffed by residents.
- **Exit** — a shrinking population shrinks the domestic buyer pool.

### The honest counter-argument

Resident population and tourism demand can decouple, and in resort towns they routinely do:
Niseko's economy is not built on Kutchan's residents. Foreign and domestic visitors, seasonal
workers and non-resident owners can sustain a local economy while the census falls.

**But decoupling has to be evidenced, not assumed** — and it is precisely what distinguishes
Hakuba (rising land, rising tourism, foreign operators arriving) from Yuzawa (falling for 33
years despite Shinkansen access). Both are depopulating. Only one has decoupled.

**This gives the screen a sharper question than "is the town shrinking?":** *has tourism demand
demonstrably decoupled from resident decline here, or is that still a hope?* On current evidence
Hakuba and Kutchan have; Myoko has not yet; Yuzawa did not.

### Still required
- IPSS projections for **Hakuba, Nozawa Onsen, Kutchan, Iiyama, Yuzawa, Furano** — currently
  **not retrieved**, so no cross-market comparison is possible. **Highest-priority gap.**
- Working-age population specifically, which drives labour availability more than headline
  population.
- Whether Hakuba and Kutchan are net in-migration exceptions, which would be a strong signal.

---

## 3. How these two risks interact

They are not independent, and the interaction is the sharpest point in this document.

The cheap Honshu markets tend to be **lower elevation on the Japan Sea side** (higher snow risk)
*and* **more severely depopulating** (higher labour and exit risk). The markets that are
demonstrably appreciating are those where foreign capital and operators have already arrived —
which is what makes them expensive.

That is not a coincidence. It is a reasonable partial answer to the master prompt's standing
question, *why hasn't sophisticated capital already arbitraged this opportunity away?*

**Possible answer: it has not been arbitraged away because the discount is compensation for real
risk** — snow, labour and liquidity — rather than an oversight.

That is a hypothesis, not a conclusion. It is testable, and testing it is now the central task of
Phases 5–11. But it is the most plausible reading of the evidence gathered so far, and it should
be stated plainly rather than discovered late.

---

## 4. Risk records to create

To be entered against `schemas/core/risk_factor.json` once market-level data supports scoring:

| `risk_key` | Scope | Thesis-critical | Status |
| --- | --- | --- | --- |
| `snow_reliability` | market | **yes** | Evidenced, elevation-dependent |
| `depopulation` | market | **yes** | Evidenced for Myoko and Hokkaido; comparators missing |
| `labour_shortage` | market | yes | Implied by depopulation; not directly evidenced |
| `resort_operator_failure` | market | no | Implied by the 40% resort closure rate |
| `exit_illiquidity` | market | **yes** | Not yet researched |
| `oversupply` | market | yes | Yuzawa evidences the mechanism; not yet assessed per market |

---

## Sources

| Ref | Source | Tier | Accessed | Note |
| --- | --- | --- | --- | --- |
| R1 | Japan Today / Nippon Foundation reporting on ski resort closures | 5 | 2026-08-16 | 40% decline from 1999 peak; Hakuba snow management |
| R2 | Takahashi et al., *International Journal of Climatology* (2021), "Long-term trends in snowfall characteristics and extremes in Japan from 1961 to 2012" | 5 (peer-reviewed) | 2026-08-16 | Station-level long-term trends |
| R3 | *Progress in Earth and Planetary Science* (Springer), 5-km regional climate model study, 1959–2020 | 5 (peer-reviewed) | 2026-08-16 | Elevation-dependent trends — the key finding |
| R4 | Wikipedia / Ski Asia resort statistics | 5 | 2026-08-16 | Base and summit elevations. **One Myoko figure rejected as not credible** — see §1 |
| R5 | IPSS 日本の地域別将来推計人口 (令和5年推計), via secondary | 1 (via 5) | 2026-08-16 | Myoko −46.7% to 2050. **Verify directly against IPSS** |
| R6 | Hokkaido Prefecture summary of IPSS 令和5年推計 | 2 | 2026-08-16 | 129 municipalities to ≤60%, 67 to ≤50% by 2050 |

**Caveat.** R2 and R3 are peer-reviewed and are the strongest evidence in this repository so
far, but both were accessed via search summaries rather than full text. The elevation-dependent
finding in R3 is load-bearing for screening and **should be read in full** before it drives a
recommendation.
