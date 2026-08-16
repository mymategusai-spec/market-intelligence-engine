# How much capital would this actually take?

**Phase:** 47 / 17 (capital strategies), brought forward
**Status:** Illustrative. Cost side modelled from sourced benchmarks; **revenue side not
modelled at all.**
**Last updated:** 2026-08-16
**Model:** [`scripts/analysis/capital_model.py`](../../../scripts/analysis/capital_model.py) ·
**Inputs:** [`data/reference/cost-assumptions.json`](../../../data/reference/cost-assumptions.json) ·
**Output:** [`analysis/financial_models/capital-requirement.md`](../../../analysis/financial_models/capital-requirement.md)

---

## 1. The headline

**Purchase price understates the real investment by between 93% and 284%.**

| Strategy | Purchase (A$) | **Total project cost (A$)** | Per owner at 50/50 | Multiple |
| --- | --- | --- | --- | --- |
| **Shoestring** | 71,000 | **167,000 – 273,000** | 84,000 – 137,000 | 2.35× – 3.84× |
| **Sensible** | 222,000 | **429,000 – 635,000** | 215,000 – 317,000 | 1.93× – 2.85× |
| **Strong** | 534,000 | **1,014,000 – 1,429,000** | 507,000 – 715,000 | 1.90× – 2.68× |

At FX of 112.37 JPY/AUD (2026-08-16). Purchase prices are **round illustrative figures**
spanning a plausible range — Phase 13 has not yet collected real listings.

### Why this matters more than any market ranking

The "¥5 million Japanese ski house" framing that draws Australian buyers to this market is
describing the **smallest line item** in the project. On the shoestring case, an A$71,000 house
is an A$167,000–273,000 commitment before it can lawfully take a paying guest.

**The cheaper the property, the worse the ratio.** Fixed costs — inspection, legal, licensing,
compliance, furnishing — do not scale down with purchase price, while a cheap building usually
needs *more* renovation, not less. That is why the shoestring case has the **highest** multiple
(up to 3.84×) and the strong case the lowest (1.90×).

This inverts the intuition the whole thesis rests on. **Buying cheaper does not reduce risk
proportionally; it concentrates the budget into the least predictable line — renovation — while
the fixed costs stay fixed.**

---

## 2. Where the money actually goes

Shoestring case, low estimate (A$167,000 total):

| | A$ | Share |
| --- | --- | --- |
| Purchase | 71,193 | 43% |
| **Renovation + contingency** | **57,845** | **35%** |
| Furnishing | 13,349 | 8% |
| Working capital | 12,014 | 7% |
| Licensing / compliance | 4,450 | 3% |
| Taxes, commission, legal, diligence | 8,169 | 5% |

Renovation plus its contingency is **the second largest cost and by far the least certain**.
It is also the only major line the owners partly control — through property selection, not
through negotiation.

---

## 3. What is NOT in these numbers

Stated prominently because a capital model that looks complete is more dangerous than one that
obviously isn't.

**No revenue.** No nightly rates, no occupancy, no NOI, no yield. Rates and occupancy data were
not obtained. Inventing them would produce exactly the false precision the brief warns against.
**These figures show what it costs to start, not whether it works.**

Also excluded: ongoing Japanese tax on non-resident rental income; tax representative
(納税管理人) fees, which are mandatory for non-residents; owner travel and inspection trips;
currency transfer costs; and any debt, since none is assumed available.

---

## 4. The FX point, which is larger than it looks

`FACT` — AUD has risen from roughly **84 JPY in 2021** to about **112 in 2026**, up ~17.5% in the
past year, driven mainly by the Australia–Japan interest rate gap.

A ¥30,000,000 property cost about **A$357,000 at 84** and about **A$267,000 at 112.37** — a **25%
fall in AUD terms with no change in the Japanese price.**

**A material part of the "Japan is cheap" story for Australian buyers is AUD strength, not
Japanese cheapness.** That has two consequences:

1. Entry today is genuinely cheaper in AUD than it was — a real, current advantage.
2. It is **reversible**. Over a 10–15 year hold, a reversion toward 84 would cut the AUD value of
   both the asset and its income by roughly a quarter, independently of anything happening in
   Japan. For owners earning JPY and spending AUD, that is an unhedged structural exposure.

FX belongs in the risk register as a first-class item, not a footnote.

---

## 5. Reliability of these figures

| Line | Claim type | Confidence |
| --- | --- | --- |
| Agent commission (3.3%) | `FACT` | High |
| Registration / transfer tax | `ESTIMATE` | Medium |
| Acquisition tax (effective 2%) | `ESTIMATE` | **Low** — charged on assessed value, not price |
| Renovation benchmarks | `ESTIMATE` | **Low** — and residential, not commercial |
| Licensing / compliance | `ESTIMATE` | **Lowest in the model** |
| Working capital | `ASSUMPTION` | Low — proxied from build cost |
| Contingency (30%) | `ESTIMATE` | Medium — lower end of advised 30–50% |
| FX rate | `FACT` | Medium — volatile, ~110–114 |

**The single biggest weakness:** renovation benchmarks are for **residential** akiya work.
Converting a building to lawful **commercial** accommodation adds fire compliance, evacuation
requirements and possibly structural and seismic upgrades that residential benchmarks exclude.
Commercial conversion should be assumed to cost materially more than shown, and the true figure
depends on Phase 12 licensing research that has not been done.

**No contractor has quoted. No inspector has been engaged. No property has been priced.**

---

## 6. What this changes

1. **Screening must run on total project cost, not asking price.** A market with cheap stock and
   expensive compliance can be worse than a dearer market with lower conversion costs. The
   filters already support this (`filters.json` supports `TOTAL PROJECT COST`); the data does not
   exist yet to apply it.
2. **The shoestring strategy deserves scepticism.** Its 2.35–3.84× multiple means the budget is
   dominated by the least predictable cost, with the least margin for error. It is the strategy
   most likely to run out of money mid-renovation — the worst possible failure mode, leaving an
   unlettable building and no capital.
3. **An existing licensed operating property may be cheaper overall than a cheaper unlicensed
   one.** It removes the licensing line, much of the compliance renovation, and the risk of
   discovering the conversion is impossible. This strengthens the existing decision to treat a
   transferable 旅館業法 licence as a major value signal.
4. **Working capital is not optional.** Winter-dominant revenue means a property completed in
   spring waits most of a year for meaningful income, while the acquisition tax bill arrives in
   the interim.

---

## 7. Next

1. Collect real listings (Phase 13) and replace illustrative purchase prices.
2. Get **commercial** conversion cost benchmarks, not residential akiya figures.
3. Establish fire and evacuation requirements per licence class (Phase 12) — this is the
   least reliable line in the model.
4. Obtain nightly rates and occupancy so revenue can be modelled and the capital figures can
   finally be tested against a return.
5. Identify inspectors and get indicative fees (Phase 15) — **research only, no contact without
   owner approval**.
6. Add FX to the risk register as a first-class, unhedged exposure.
