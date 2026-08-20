# `DEMAND_SUPPLY_BALANCE_SCORE`

**Phase:** 11 / 32 · **Status:** Scored where data permits. The denominator is still missing.
**Last updated:** 2026-08-20

> The brief: compare future accommodation supply against demand growth, and **do not assume
> development is bullish.**

---

## 1. The scores

Scored 0–10 where **10 = demand growing far faster than committed supply**.

| Market | Committed supply (weighted rooms) | Demand signal | **Score** | Confidence |
| --- | --- | --- | --- | --- |
| **Myoko** | **~47** (Six Senses 57 approved; MGallery 38 refurb ≈ zero net) | Foreign stays doubled 2018→FY2023; Niigata resort hotels **64.9% January, rank 4** | **7.5** | Medium |
| **Nozawa Onsen** | **None identified** | Land **+21.69%**, national #2; four-season village demand | **7.0** | **Low** — pipeline unresearched, so absence is not evidence of absence |
| **Hakuba** | **None identified** | Foreign stays **+172% vs 2018**, 15.5% CAGR; ski visits **+31.1% over 4 seasons** | **6.0** | **Low** — pipeline unresearched, and Nagano occupancy is the worst in Japan |
| **Kutchan/Niseko** | **~774** (Hotel101 482 under construction, Moxy 310, Aman 61, Capella, plus 22 announced) | Hokkaido stays **+20.7% vs 2019**; January resort occupancy **66.2%, rank 3** | **3.0** | Medium |
| Yuzawa | None | 33-year decline; 152 apartments for sale across 30 buildings | **2.0** | Medium |

---

## 2. Niseko is the finding

**Niseko carries ~774 status-weighted committed rooms against Myoko's ~47 — roughly 16×.**
Hotel101 alone (482 rooms, structure complete) exceeds Myoko's entire pipeline tenfold.

That supply arrives into a prefecture already running **59.8% annual occupancy** with resort hotels
at **50.5%**. Even Hokkaido's strong January figure (66.2%) is not a market with no room to fill.

`HYPOTHESIS`, medium confidence — **Niseko is closer to the top of its supply cycle than the
bottom.** This is the clearest case in the project of the brief's warning: Niseko scores best or
near-best on snow resilience, occupancy, management depth and exit liquidity, and its enormous
development pipeline reads as investor confidence — but for a **small independent lodge competing
for the same guests**, 774 new rooms is a threat, not a tailwind.

**Development is not bullish for everyone.** It is bullish for landowners and bearish for
operators, and these owners would be both.

---

## 3. Myoko is the inverse, and that is genuinely valuable

Myoko has the **lowest committed supply of any candidate** (~47 weighted rooms, and the MGallery is
a refurbishment adding near-zero net capacity) alongside demand that doubled in five years and a
prefecture whose resort hotels rank 4th nationally in January.

**This is Myoko's strongest quantitative advantage**, and it is the mirror image of Niseko's
weakness. It also cuts against the earlier reading that Myoko's luxury pipeline was a threat: 95
rooms — of which perhaps 57 are genuinely new — is not a supply shock. It is a brand signal.

The bear reading in the earlier pipeline analysis (that Six Senses repositions the market upmarket
and raises the renovation bar) still stands. But it is a **competitive-positioning** risk, not a
**supply-glut** risk, and those need different responses.

---

## 4. What the score cannot yet do

**The denominator is still missing.** Existing room supply per town has not been obtained, so
"774 rooms" cannot be expressed as a percentage increase. That difference — 5% or 50% — is the
whole question, and it remains the highest-priority gap in this phase.

**Absence of a pipeline is not absence of supply.** Hakuba and Nozawa score 6.0 and 7.0 on
*unresearched* pipelines. Those scores carry `low` confidence for exactly that reason and **must
not be read as "no supply is coming"** — only as "none was found". Hakuba in particular is
suspicious: it is the fastest-appreciating land market in Japan, and it would be surprising if
nothing were being built there.

**Peak-season demand is not separated from annual demand.** The brief asks for both. Only annual
and January figures exist.

---

## 5. Method

```
supply side  = Σ (rooms × status weight from config/core/engine.json)
               rumoured 0.0 · proposed 0.1 · announced 0.2 · planning 0.35
               approved 0.6 · funded 0.8 · under construction 0.95 · completed 1.0
demand side  = foreign overnight-stay growth + January occupancy rank
score        = judgement over both, with confidence reflecting pipeline research completeness
```

No unweighted room total is used anywhere. A refurbishment is credited near-zero net new supply.

---

## 6. Next

1. **Existing room supply per town** — unblocks the ratio and turns this from a judgement into a
   calculation.
2. **Research the Hakuba and Nozawa pipelines.** Two of the four ranked markets are scored on
   absence of evidence.
3. Separate peak-season from annual demand.
4. Confirm whether Six Senses construction has actually started — still recorded as `approved`,
   not `under construction`, because the announced April 2026 start was never confirmed.
