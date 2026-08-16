# Japanese ski-market land prices — three regimes, not one market

**Phase:** 7 (historical property markets), serving Phase 4 screening
**Status:** First substantive analysis. Figures corroborated across two independent secondary
sources; direct MLIT retrieval still outstanding.
**Last updated:** 2026-08-16
**Data:** [`data/reference/land-prices-2026.json`](../../../data/reference/land-prices-2026.json)

---

## 1. The headline

Japanese ski-resort land is **not one market**. The 2026 official land prices separate the
longlist into three regimes that behave completely differently:

| Regime | Markets | 2026 change |
| --- | --- | --- |
| **Recovering strongly** | Hakuba **+26.9%** (national #1), Nozawa Onsen **+21.7%** (#2) | Sharp, sustained |
| **Established, still rising** | Kutchan/Niseko **+12.3%**, Furano **+6.7%** | Moderate, from a high base |
| **Flat or still falling** | Myoko **−0.79%**, Yuzawa **−0.44%** | Negative |

`FACT` — all figures from 2026 公示地価, published by MLIT 2026-03-18, retrieved via an
aggregator of official data and corroborated by a second independent secondary source to within
0.02 percentage points.

**The markets rising are the ones foreign buyers have already found.** MLIT's own commentary on
Hakuba attributes the increase to overseas demand — foreign buyers purchasing residences and
**opening accommodation businesses such as pensions**. That is precisely this project's strategy,
already being executed at scale by others.

---

## 2. Myoko: the promoted market is the one not moving

| Myoko 妙高市 | Value |
| --- | --- |
| 2026 公示地価 average | **¥19,904/m²** |
| 2026 change | **−0.79%** |
| 2025 基準地価 | ¥11,777/m², −0.77% |
| 1993 peak | ¥54,033/m² |
| 2022 low | ¥18,911/m² |
| **Still below peak** | **−63%** |
| Recovery from low | **+5.3%** over four years |

Myoko bottomed in 2022 and has recovered about five percent in four years — and is *still
falling* year-on-year — while being marketed as the emerging destination of choice for exactly
the Australian buyer this project describes.

**This does not mean Myoko is a bad investment.** Two readings are consistent with the evidence:

1. **Early-stage.** Capital has been committed (the ¥35bn Patience Capital raise is real) but
   has not yet flowed into transactions. Land values lag. Buying before the repricing is the
   entire point.
2. **The repricing may not come, or may be narrow.** Announced resort developments frequently
   fail to lift a whole municipality; the benefit may be confined to a few parcels beside the
   new resort while the rest of the town continues its 30-year decline.

The evidence cannot yet distinguish these. What it does establish is that **the Myoko case rests
on anticipation, not on realised appreciation** — and anyone presenting Myoko land as already
appreciating is not describing the official data.

The falsifiable test: if reading 1 is right, Myoko's land prices should turn positive as the
2028 first stage approaches. **That is a monitorable prediction**, and it is exactly what this
engine is built to watch.

---

## 3. Yuzawa: the value trap, documented

Yuzawa is the most instructive market on the longlist, and nobody is promoting it.

| Yuzawa 湯沢町 | Value |
| --- | --- |
| 1993 peak | **¥190,062/m²** |
| 2026 | **¥28,100/m²** |
| Change from peak | **−85%** |
| 2026 change | **−0.44%**, still falling |

Yuzawa has direct Shinkansen access from Tokyo, extensive ski terrain, onsen, and famously cheap
resort apartments. On a naive screen — cheap, accessible, snowy, plenty of stock — it looks
outstanding.

It has fallen 85% over 33 years and is *still falling*.

**This is the answer to "why is this cheap?" in its clearest form.** Yuzawa is cheap because
bubble-era developers built an enormous surplus of resort apartments into a shrinking domestic
market, and that overhang has not cleared in three decades. Accessibility did not save it. Snow
did not save it. Cheapness was never the signal.

**Every cheap market on the longlist must be tested against Yuzawa.** The question is not "is it
cheap?" but "what is different here that was not true of Yuzawa?" A candidate market that cannot
answer that has not been distinguished from a documented 33-year decline.

---

## 4. Hakuba: 30 years of context that changes the framing

| Hakuba 白馬村 | Value |
| --- | --- |
| 1995 peak | ¥55,333/m² |
| 2018 low | **¥8,686/m²** (−84% from peak) |
| 2026 | ¥25,556/m² |
| From 2018 low | **+194%** |
| **Still below 1995 peak** | **−54%** |
| Benchmark 白馬-1 | ¥27,400/m², +33.0% (after +29.6% the prior year) |

Two facts sit together uncomfortably, and both matter:

- **Hakuba has nearly tripled since 2018** and is the fastest-appreciating residential land in
  Japan, two years running. The easy money has been made.
- **Hakuba is still 54% below its 1995 peak.** "Too expensive" is a claim about the last seven
  years, not about the last thirty.

The 1995→2018 collapse is the more important half. A resort market that fell 84% over 23 years
is not a safe asset class, and the same market is now compounding at ~30% a year. Both
observations describe Hakuba.

**Implication for the thesis:** the argument for a cheaper market is not that Hakuba is
overpriced in absolute terms. It is that Hakuba's re-rating has already happened, so a buyer
arriving now is paying for a discovery someone else made. Whether an undiscovered market exists
that will repeat it is the actual question.

---

## 5. The within-town spread dwarfs the between-town spread

The single most actionable finding here.

| Market | Highest point | Lowest point | Spread |
| --- | --- | --- | --- |
| Hakuba | ¥67,500/m² | ¥6,100/m² | **11.1×** |
| Myoko | ¥35,800/m² | ¥2,550/m² | **14.0×** |
| Yuzawa | ¥43,800/m² | ¥9,510/m² | 4.6× |

Between the cheapest and dearest *municipalities* the spread is about 6× (Kutchan ¥120,750 vs
Myoko ¥19,904). **Within** Hakuba and Myoko it is 11–14×.

Choosing the right neighbourhood matters roughly **twice as much** as choosing the right town.

This validates the decision to decompose destinations into submarkets (`ARCHITECTURE.md`,
`neighbourhood.json`) and carries a blunt warning: **the cheap end of an expensive town is
cheap for a reason.** Myoko's ¥2,550/m² parcels in rural Futamatsu are not a discount on Myoko
Kogen — they are a different, largely unrentable product. A screen that compares municipal
averages would treat them as the same market.

---

## 6. What this means for screening

1. **Cheapness has been eliminated as a signal on its own.** Yuzawa is the cheapest relative to
   its own history and the worst performer. Myoko is the cheapest in absolute terms and flat.
   The two most expensive — Kutchan and Nozawa — are both rising.
2. **The "emerging market" narrative is not visible in the data.** Nozawa Onsen, at national
   rank 2, materially outperforms Myoko while receiving a fraction of the promotion. It has been
   under-weighted in screening and should be promoted to serious research.
3. **Neighbourhood analysis is not optional.** It is where most of the variance lives.
4. **Land prices measure land, not buildings.** For a fixer-upper thesis the building is often
   worth little or nothing, and Japanese rural buildings frequently carry negative value once
   demolition is priced. Land direction is a market signal, not a proxy for what a property
   costs or returns.

---

## 7. Caveats

- These are **all-use municipal averages**, mixing residential, commercial and industrial land.
  Residential-only breakdowns are still to be retrieved.
- **公示地価 and 基準地価 are different series** with different points and reference dates. They
  are reported separately above and must never be compared to each other as a change over time.
- Figures came via an aggregator of official data, not from MLIT directly. Two independent
  secondary sources agree closely, but **direct retrieval is required before any final
  recommendation**.
- Official land valuations are not transaction prices. `JP-MLIT-TORIHIKI` publishes actual
  transaction prices from Q3 2005 and is the better source for what buyers really pay.
- Nothing here says anything about **rental demand or achievable yield**, which is a separate
  question from land value and may not correlate with it at all.

---

## 8. Next

1. Retrieve directly from MLIT and upgrade `verification_status` from `CORROBORATED_SECONDARY`.
2. Retrieve the missing municipalities: Niseko-cho, Shiga Kogen/Yamanouchi, Iiyama (which
   contains Madarao), Appi/Hachimantai, Rusutsu, Kiroro.
3. Build full year-by-year series for the surviving candidates and compute 1/3/5/10-year change
   and CAGR per the brief.
4. Pull actual transaction prices from `JP-MLIT-TORIHIKI` and compare against these valuations.
5. **Promote Nozawa Onsen to serious research** — a national #2 performer that the narrative
   overlooks is exactly what an evidence-led screen is supposed to surface.
6. Test every candidate market explicitly against the Yuzawa case.
