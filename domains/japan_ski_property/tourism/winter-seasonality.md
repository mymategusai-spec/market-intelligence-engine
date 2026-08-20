# Winter occupancy and seasonality — the answer is prefecture-specific

**Phase:** 8 · **Status:** Priority-2 question answered with Tier 1 data
**Last updated:** 2026-08-20
**Data:** [`data/cleaned/tourism/winter-occupancy-and-seasonality.json`](../../../data/cleaned/tourism/winter-occupancy-and-seasonality.json)

---

## 1. Does annual oversupply mask strong winter occupancy?

**For Niigata and Hokkaido, emphatically yes. For Nagano, barely — and not at all for the licence
class that matters.**

`FACT` — JTA resort-hotel occupancy, annual 2024 versus January 2025:

| Prefecture | Annual | Rank | **January** | **Rank** | Uplift |
| --- | --- | --- | --- | --- | --- |
| **Niigata** (Myoko, Yuzawa) | 34.0% | 45 | **64.9%** | **4** | **+30.9pp** |
| **Hokkaido** (Niseko, Furano) | 50.5% | 23 | **66.2%** | **3** | +15.7pp |
| **Nagano** (Hakuba, Nozawa) | 35.4% | 43 | **45.0%** | 20 | +9.6pp |
| National | 54.1% | — | 51.4% | — | −2.7pp |

**Niigata moves from 45th in Japan to 4th.** Its annual figure is a seasonality artefact almost
entirely — exactly the correction assumption F7 predicted. Hokkaido is strong on both measures.

**Nagano is the outlier, and not favourably.** Its resort hotels reach only 45.0% in the peak ski
month, ranking 20th — while Niigata, whose annual figure is *worse*, ranks 4th.

### The most adverse single datapoint found so far

`FACT` — **Nagano simple lodging (簡易宿所): 15.3% annual, 14.2% in January.**

It is **lower in the peak ski month than its own annual average**, against a national January
figure of 25.4% and Hokkaido's 34.2%.

This matters more than any other occupancy number in this project, because 簡易宿所 is the licence
class a small owner-operated lodge would most likely hold. In Nagano it shows **no winter uplift
whatsoever.**

Three readings, and they are not mutually exclusive:

1. **The category is dominated by marginal operators** — part-time minshuku, hobby pensions,
   hostels — that do not trade hard even in peak season. A well-run commercial lodge would beat
   the average substantially.
2. **Nagano genuinely has too many small lodges** chasing the same guests. The prefecture carries
   post-Olympic and bubble-era pension stock, and demand growth has not filled it.
3. **The strong performers are in hotels, not simple lodgings.** Nagano's business (62.5%) and
   city hotels (64.1%) do far better, suggesting demand exists but is not flowing to small
   independents.

`HYPOTHESIS`, medium confidence — reading 2 combined with 3 is most consistent with the wider
evidence: Nagano's land is appreciating fastest in Japan while its small-lodging occupancy is
flat, which is what you would expect if **capital is bidding up assets faster than demand is
filling them.**

**This is a direct caution on the Hakuba case**, which currently leads the ranking.

### What it does not say

Nagano is not Hakuba. The prefecture includes Matsumoto, Nagano City, Karuizawa and Shiga Kogen.
Hakuba's own visitation is growing strongly (below). **Municipal-level occupancy for Hakuba would
settle this and has not been obtained** — it is now the highest-value outstanding tourism task.

---

## 2. Hakuba's own numbers: growth, then a first decline

`FACT` — Hakuba Village ski visits across four seasons (four village resorts; excludes Tsugaike
and Cortina, which are other municipalities):

| Month | R04-05 | R05-06 | R06-07 | **R07-08** | Share |
| --- | --- | --- | --- | --- | --- |
| Dec | 136,401 | 151,051 | 174,352 | **184,040** | 15.9% |
| **Jan** | 267,778 | 325,660 | 369,840 | **372,981** | **32.3%** |
| **Feb** | 263,229 | 333,558 | 353,813 | **364,970** | **31.6%** |
| Mar | 169,280 | 182,940 | 210,566 | **199,039** | 17.2% |
| Apr | 38,977 | 43,821 | 50,229 | **30,881** | 2.7% |
| May | 4,263 | 3,774 | 11,158 | **1,929** | 0.2% |
| **Season** | 879,928 | 1,041,068 | 1,170,780 | **1,153,840** | |

**Growth of +31.1% over four seasons — but R07-08 is the first decline, −1.4%.**

### The shape of the season
**January and February alone are 63.9% of the year. December–March is 97.1%.**

This is tighter than the operator rate card implies (high season 22 Dec – 7 Mar, 76 days) and
confirms the revenue base is a **two-month core with two shoulder months either side**. Any model
spreading revenue across a longer season overstates it.

### The late season is collapsing — and this is the climate signal, measured

`FACT` — year on year, R06-07 → R07-08:

| Month | Change |
| --- | --- |
| March | **−5.5%** |
| April | **−38.5%** |
| May | **−82.7%** |

December (+5.6%) and January (+0.8%) held; February (+3.2%) grew. **The entire decline is
concentrated in the season tail.**

This is the first *directly measured* evidence in this project for the climate risk previously
established only from regional literature. It is one season, so it could be a single bad spring —
but it is precisely the pattern the elevation-dependent snow research predicts, and it is
happening at the market that leads the ranking.

**Implication for revenue models:** shoulder-season revenue assumptions should be treated as the
least reliable part of any projection, and stress-tested downward. A model relying on March–April
income is relying on the part of the season that is measurably shrinking.

---

## 3. What this changes

1. **Priority 2 is answered.** Annual occupancy does mask strong winter performance in Niigata and
   Hokkaido, but **not in Nagano**, and not at all for simple lodging.
2. **Niigata's winter resort-hotel occupancy at rank 4 is a genuine positive for Myoko** — the
   first clear one found on the demand side, and it partially offsets the weak annual figures used
   against it earlier.
3. **Nagano's simple-lodging figure is a red flag for the small-lodge model there**, needing
   municipal-level data to resolve.
4. **The revenue season is two core months plus two shoulders**, and the shoulders are shrinking.
5. **Hokkaido remains strongest on occupancy** on both annual and January measures.

---

## 4. Next

1. **Municipal occupancy for Hakuba, Myoko, Nozawa and Kutchan** — the prefecture figures are now
   pulling in different directions and only town-level data resolves it.
2. February prefecture occupancy — February is the true peak by visits, and only January was
   obtained. (Adjacent JTA content IDs returned 404.)
3. Whether Niigata's January resort-hotel strength is Myoko, Yuzawa or Naeba.
4. Monitor whether the late-season decline repeats in R08-09. One season is not a trend, but two
   would be.
