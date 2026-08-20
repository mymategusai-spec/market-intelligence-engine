# Property-level financial models — the thesis, tested

**Phase:** 17 / 26 · **Status:** First defensible models. Occupancy remains assumed.
**Last updated:** 2026-08-20
**Run:** `python3 scripts/analysis/property_financials.py` · `python3 scripts/analysis/capacity_sweep.py`
**Full output:** [`analysis/financial_models/property-financial-models.md`](../../../analysis/financial_models/property-financial-models.md)

---

## 1. The headline number

**Yield on total project cost, across every property and every scenario modelled: 0.7% – 3.2%.**

| Scenario | High-season occupancy | Best yield | Property |
| --- | --- | --- | --- |
| Conservative | 40% | **1.05%** | Ski-in Ski-out Chalet Tsugaike, Hakuba |
| Base | 55% | **2.17%** | Ski-in Ski-out Chalet Tsugaike, Hakuba |
| Strong | 70% | **3.17%** | Ski-in Ski-out Chalet Tsugaike, Hakuba |

**No property, in any scenario, yields more than 3.2% on total project cost.**

For context, that is below a risk-free Australian term deposit — before Japanese income tax on
non-resident rental income, which is not modelled — while carrying the currency, snow,
depopulation, oversupply and liquidity risks already documented.

---

## 2. But this does not mean the thesis fails

The brief's thesis is not "beat a term deposit". It is:

> …purchase an undervalued property close to genuinely excellent Japanese snow, renovate or
> reposition it, **use it personally**, **have tourism materially support ownership costs**, and
> potentially benefit from appreciation.

Tested against that, the models say something quite different:

**Tourism does materially support ownership costs — for larger properties.** In the base case a
16–22 guest lodge generates **A$13,000–23,000 of NOI per year after all operating costs, and after
deducting three weeks of owner use at peak rates.** The property runs itself, pays its own
insurance, snow clearing, management and maintenance, and returns a surplus.

**What it does not do is produce an investment return that compensates for the capital at risk.**

So the honest verdict is:

> **This is a lifestyle asset that can largely pay for itself. It is not an investment.**

Whether that is attractive depends on how the owners value three weeks a year in a ski lodge they
own — a question the engine cannot answer for them, and should not pretend to.

---

## 3. Capacity: the economics say "as large as you can lawfully manage"

`CALCULATION` — identical property, capacity varied, base case, purchase price scaled with
capacity from the observed price-per-guest in the real candidate set:

| Guests | Hakuba yield | Myoko yield | Madarao yield | **Fixed costs as % of revenue** |
| --- | --- | --- | --- | --- |
| 6 | 1.21% | 0.04% | **−0.54%** | **26–44%** |
| 8 | 1.95% | 0.79% | 0.51% | 20–33% |
| 10 | 2.42% | 1.27% | 1.19% | 16–26% |
| 12 | 2.74% | 1.59% | 1.66% | 13–22% |
| 16 | 3.11% | 1.98% | 2.24% | 10–16% |
| 20 | 3.37% | 2.24% | 2.62% | 8–13% |
| 24 | **3.54%** | **2.42%** | **2.89%** | **7–11%** |

**Yield rises monotonically with capacity. There is no optimum inside the range tested.**

### The mechanism
Remote ownership carries an irreducible fixed cost base — insurance (~¥250k), snow clearing
(~¥400k) and the tax representative and compliance a non-resident legally requires (~¥300k). That
is roughly **A$8,450 a year before a single guest arrives.**

At 6 guests those fixed costs consume **26–44% of revenue**. At 24 guests, **7–11%**.

**Small properties cannot carry the cost of being owned from Australia.** A 6-guest property in
Madarao is NOI-negative in the base case.

### Breakeven capacity

| Market | Base case | **Conservative case** |
| --- | --- | --- |
| Kutchan/Niseko | 4 guests | 5 |
| Hakuba | 5 guests | 6 |
| Myoko | 6 guests | **8** |
| Madarao | 7 guests | **10** |
| Nozawa Onsen | 7 guests | **10** |

In the cheaper markets a property must sleep **8–10 guests just to break even** if occupancy
disappoints.

### The answer, and its caveat
**The economic answer is: as large as can lawfully and practically be managed.** The binding
constraints are **not economic** — they are:

1. **The sprinkler threshold.** The model proxies a 2.5× step in licensing cost at 16+ guests and
   yield *still* rises through it. The compliance step would have to be far larger than 2.5× to
   create an interior optimum. **This remains the largest single unresolved cost in the project.**
2. **Bathrooms.** A private bathroom commands a 22.6% rate premium (measured), and adding them in
   a snow-country building is among the most expensive renovation categories.
3. **Remote management.** Above roughly 10–12 guests, on-site presence becomes likely — and
   `ASSUMPTIONS.md` C2 (management procurable) is already low-confidence.

**This directly contradicts the earlier working hypothesis of a 10–16 guest sweet spot**, which was
inferred from where the available stock sits rather than from economics. The economics favour
larger. The stock, the regulation and the management constraint favour smaller. **That tension is
the real finding.**

---

## 4. What drives the result

Base case, Ski-in Ski-out Chalet Tsugaike (Hakuba, 16 guests) — the best performer:

| | A$ |
| --- | --- |
| Gross revenue, after owner use | 85,450 |
| Operating costs | (62,169) |
| **NOI** | **23,281** |
| Total project cost | 1,075,198 |
| **Yield on TPC** | **2.17%** |

Operating costs are **73% of gross**. The largest lines are management (20%) and platform
commission (15%) — **35% of revenue before anything is cleaned, heated or insured.** That is the
price of operating remotely through intermediaries, and it is the single biggest lever the owners
could pull. Self-managing is not available to them; negotiating either rate is.

**Owner use is expensive.** Three weeks at peak occupancy and peak rates costs roughly **A$25,000
of foregone revenue** for a 16-guest property in Hakuba. That is more than the NOI. A property with
separate owner quarters avoids this entirely, which is why `NOZ-001` (10-bed lodge **plus** a
separate 3-bed house) matters disproportionately.

---

## 5. Honest statement of what is assumed

| Input | Status | Why it matters |
| --- | --- | --- |
| **Occupancy** | **`ASSUMPTION`, low confidence** | Drives revenue linearly. No property-level occupancy exists for any candidate. Bracketed by measured anchors: Nagano simple lodging **14.2%** in January, Niigata resort hotels **64.9%**. The spread between scenarios is the honest measure of what is unknown. |
| Rates per guest | `ESTIMATE`, medium | From real rate cards and listings, but few markets and few properties |
| Operating cost rates | **`ASSUMPTION`, low** | **No Japanese operator has quoted anything.** Industry placeholders |
| Season structure | `FACT` | 76 high-season nights from a published rate card, corroborated by monthly visit data |
| Capital costs | `ESTIMATE` | Documented in the renovation benchmarks; understated in a known direction |
| Japanese income tax | **NOT MODELLED** | Would reduce every figure above |

**A 1-percentage-point error in occupancy moves yield by roughly 0.05pp.** The gap between
conservative and strong — 30 points of occupancy — is the difference between 1.05% and 3.17%.
**Occupancy is the whole ballgame, and it is the thing least known.**

---

## 6. What would change the conclusion

- **Management at 10% instead of 20%**, or direct booking replacing platform commission, would add
  roughly 1–1.5pp of yield. This is the largest controllable lever and is worth testing with real
  operators in Phase 16.
- **A property with separate owner quarters** removes ~A$25,000 of foregone revenue — adding over
  2pp of yield at a 16-guest Hakuba property. **This is the single highest-value property
  attribute identified anywhere in the project.**
- **An existing licensed operating business** with a trading history would replace the occupancy
  assumption with actual figures, collapsing the widest uncertainty in the model.
- **Capital appreciation is not in these numbers at all.** Hakuba land rose 26.9% in one year. If
  that continued, total return would be dominated by appreciation, not yield — but that is a
  different investment with a different risk profile, and the land-price analysis gives no reason
  to expect it to continue at that rate.

---

## 7. Next

1. **Real occupancy data** — the single highest-value input. An operating business with accounts
   would provide it directly.
2. **Real operator quotes** for management, cleaning and utilities (Phase 16).
3. **Resolve the sprinkler threshold** — it sets the capacity ceiling the economics want to reach.
4. Model Japanese income tax for non-residents.
5. Prioritise properties with **separate owner quarters** in the shortlist.
