# Tourism baseline (Phase 8 — first pass)

**Status:** Prefecture-level only. Municipality-level data located but not yet retrieved.
**Last updated:** 2026-08-16

---

## 1. The demand side is growing, and fastest where land prices are falling

`FACT` — National foreign overnight stays reached a record **177.86 million in 2025, +8%** [T1].

`FACT` (single-source, conflicted — see caveat) — Prefecture-level foreign overnight stays, 2025:

| Prefecture | Foreign overnight stays 2025 | Change | Contains |
| --- | --- | --- | --- |
| **Nagano** | **2.45 million** | **+5%** | Hakuba, Nozawa, Madarao, Shiga Kogen, Iiyama |
| **Niigata** | **0.82 million** | **+55%** | Myoko, Yuzawa, Arai |

January 2025: Nagano **430,000** (+25%); Niigata **180,000** (+58%) [T2].

Niigata posted the **second-highest growth rate of any prefecture in Japan**, behind only
Tottori [T2].

### This cuts against the land-price finding, and that matters

The [land-price analysis](../property_market/land-price-regimes.md) found Niigata's ski
municipalities flat or falling — Myoko −0.79%, Yuzawa −0.44% — while Nagano's surged.

The tourism data points the other way: **Niigata's foreign demand is growing eleven times faster
than Nagano's.**

Both can be true, and the reconciliation is the interesting part:

- **Demand leads, land lags.** Visitors arrive before capital does. Land prices reprice when
  buyers compete for stock, which follows demonstrated trading performance by a year or more.
  On this reading Niigata's land prices are where Nagano's were several years ago, and the
  Myoko "early-stage" case is strengthened materially.
- **Or growth is concentrated where the investment case is not.** Niigata's +55% is off a base
  one-third of Nagano's. A prefecture-level figure can be driven by Niigata City, by Yuzawa's
  day-trip and package market, or by a single large operator — none of which necessarily
  supports an independent lodge in Myoko.

**The engine cannot yet distinguish these**, and the distinction is decisive for the central
question. It is resolvable: the Japan Tourism Agency publishes a **130-municipality breakdown**
(§3), which would show whether the growth is in Myoko specifically.

This is the single highest-value outstanding retrieval in the project.

### Absolute scale is not a footnote

Nagano hosts **three times** Niigata's foreign overnight stays. Growth rates flatter small bases.
A market can grow 55% and still be a fraction of the size of one growing 5% — and for an owner
letting one property, the absolute depth of demand in their town matters more than their
prefecture's rank on a growth table.

---

## 2. What this does to the competing readings of Myoko

The Myoko question has been: is it early-stage, or a value trap?

| Evidence | Points toward |
| --- | --- |
| Land prices flat/negative, +5% off a 2022 low | Value trap, or very early |
| Population −46.7% by 2050 | Value trap |
| Adjacent Takada station shows long-term snow decline | Value trap |
| **Prefecture foreign demand +55%, 2nd fastest nationally** | **Early-stage** |
| ¥35bn raised toward a ¥70bn resort, first stage 2028 | Early-stage |
| Yuzawa — same prefecture — fell 85% over 33 years | Value trap |

The balance has shifted. Before the tourism data, the case rested almost entirely on
*anticipation*. There is now evidence of **realised demand growth** in the same prefecture, at a
national-outlier rate.

It is still prefecture-level, and Yuzawa sits inside the same figure — which is precisely why
municipal data is required before this changes any conclusion.

---

## 3. Data located but not yet retrieved

`FACT` — The Japan Tourism Agency's 宿泊旅行統計調査 publishes **2025 annual figures as 確定値
(final, not preliminary)**, including a **breakdown by 130 municipalities** as a downloadable
spreadsheet [T3].

This is the dataset Phase 8 needs. It would provide, per candidate town rather than per
prefecture:

- total and foreign overnight stays;
- year-on-year change;
- the split between the towns driving prefecture-level growth and those merely inside it.

`FACT` — From January 2026 the survey's stratification changed from **number of employees** to
**number of guest rooms** [T3]. **This is a methodology break.** Any series spanning it must
treat 2026-onward figures as not directly comparable with earlier years, and say so.

---

## 4. Caveats

- **The prefecture figures come from a single conflicted source.** [T2] is the brokerage
  identified in `DECISIONS.md` D-0009 as having a direct interest in Myoko. The figures are
  internally consistent and the national total corroborates independently, but **they are
  single-sourced from an interested party** and must be replaced with JTA primary data.
- Direct fetch of the JTA 2025 PDF returned **HTTP 404** (recorded in `SOURCES.md`); the index
  page was reached instead and confirms the data exists.
- Foreign overnight stays are not the whole market. Domestic visitors are the majority of
  Japanese ski demand and are not covered above.
- Overnight stays measure volume, not rate or yield. Growing visitor numbers at falling ADR
  would be a materially different investment case, and nothing here addresses ADR.
- None of this is seasonally decomposed beyond a single January reading.

---

## 5. Next

1. **Retrieve the 130-municipality JTA breakdown.** Highest-value outstanding retrieval in the
   project. It should resolve whether Niigata's +55% is a Myoko phenomenon or a Niigata City one.
2. Replace prefecture figures with JTA primary data, removing dependence on a conflicted source.
3. Build a ~10-year series per candidate town and classify each: accelerating / steadily growing
   / flat / declining, flagging the 2026 methodology break.
4. Retrieve ADR and occupancy, not just volume.
5. Separate domestic from international demand — a lodge dependent on Australians is a different
   risk profile from one with a domestic base.

---

## Sources

| Ref | Source | Tier | Accessed | Note |
| --- | --- | --- | --- | --- |
| T1 | National 2025 foreign overnight stays, multiple reports | 4 | 2026-08-16 | 177.86m, +8%, record |
| T2 | Patience Realty commentary on Niigata/Nagano winter tourism | 4 | 2026-08-16 | **Conflicted — brokerage with Myoko interest.** Sole source for the prefecture split |
| T3 | JTA 宿泊旅行統計調査 index page (`mlit.go.jp/kankocho/tokei_hakusyo/shukuhakutokei.html`) | 1 | 2026-08-16 | Confirms 2025 annual **確定値**, 130-municipality breakdown, and the Jan-2026 stratification change |
