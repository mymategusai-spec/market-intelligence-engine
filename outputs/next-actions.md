# Next Actions

**Last updated:** 2026-08-20
**Branch:** `main`
**Status:** Evidence density substantially increased. **No investment conclusion reached, and none
should be inferred.**

Read this first, then `prompts/master-prompt.md`, `PROJECT_BRIEF.md`, `RESEARCH_PLAN.md`.

---

## Where the project stands

| Phase | Status |
| --- | --- |
| 1–3 Architecture, core engine, domain module | `DONE` — 119 tests |
| 4 Destination screening | `ACTIVE` — 4 markets ranked at 68–85% coverage, 3 withheld |
| 6 Town profiles / micro-location | `PARTIAL` — Myoko, Hakuba, Nozawa |
| 7 Historical property markets | `PARTIAL` — 2026 land prices, 30-year histories |
| 8 Tourism | `PARTIAL` — Hakuba 19-yr series, Myoko partial, occupancy by prefecture |
| 11 Infrastructure pipeline | `PARTIAL` — Myoko and Niseko only |
| 12 Regulation | `PARTIAL` — national resolved, municipal unchecked |
| 13 Property collection | `PARTIAL` — 203 records, 3 price events |
| 14 Renovation costs | `PARTIAL` — 3 of 6 layers evidenced |
| 17/47 Capital strategies | `PARTIAL` — cost side only |
| 18 Monitoring | `PROTOTYPE` — pipeline + tests, collection not enabled |
| 21 Risk / counter-thesis | `PARTIAL` — snow, depopulation, Yuzawa, Myoko bull/bear |
| 26 Guest capacity | `PARTIAL` — constraints identified, optimum blocked on ADR |
| 5, 9, 10, 15, 16, 19, 20, 22, 23 | `PENDING` |

```bash
python3 -m unittest discover -s tests -t . -v      # 119 tests, no install step
python3 scripts/analysis/screen_markets.py --all-profiles --explain
python3 scripts/analysis/property_costs.py --all
python3 scripts/analysis/capital_model.py --strategies
python3 scripts/monitoring/monitor.py --status
```

**Current ranking** (Hakuba/Myoko 17 of 20 dimensions, Nozawa/Kutchan 14, all `low` confidence):

> **Hakuba > Nozawa Onsen > Kutchan/Niseko > Myoko**
> Madarao, Furano and Yuzawa: `INSUFFICIENT DATA FOR RANKING`

---

## The findings that would change an owner's mind

**1. Prefecture data was misleading us, and the correction cost Myoko its best argument.**
Niigata's +55% foreign-stay growth is **not** Myoko — Myoko is ~23% of the prefecture and grew at
about half Hakuba's rate. Yuzawa sits inside the same figure. (D-0014)

**2. Hakuba's decoupling is now evidenced over 19 years.** 33,491 → 447,474 foreign overnight
stays, 15.5% CAGR, +172% against 2018. **Australians are 44.7%** and grew 117% in 2024.

**3. Nagano has the lowest hotel occupancy in Japan (39.6%, rank 47).** Read correctly: annual
figures penalise winter-only assets, and the revenue model must be seasonal (F7). Read
legitimately: Nagano and Niigata carry **existing** accommodation oversupply — the Yuzawa
mechanism at prefecture scale.

**4. Hokkaido separates on a third independent axis.** Ryokan occupancy 43.5% (rank 6) vs Nagano
27.9% and Niigata 26.6% — and Hokkaido has winter seasonality too, so this is not a seasonality
artefact.

**5. But Niseko's forward supply is ~16× Myoko's.** ~774 status-weighted committed rooms, into a
prefecture already half-empty annually. Hotel101 alone is 482 rooms with its structure complete.

**6. Yuzawa is quantified.** 152 apartments across 30 buildings, 5.1 sellers per building, 17 in
one tower, median A$22,250, cheapest A$3,100. The mechanism is **not cheapness — it is carry and
control**: negative-carry assets whose owners cannot fix them.

**7. All three observed price changes were reductions**, mean −19.4%. Survivorship-biased toward
slow movers, so an upper bound on discounting, not an estimate.

**8. Costs are worse than modelled.** Construction +40–50% since 2015 and still rising;
snow-country roof/exterior 1.5–2.0×; compliance corrected up to ¥1–3m. Purchase price now
understates true investment by **148–310%** at the shoestring level.

**9. Hakuba's shuttle stops ~6pm**, making village choice decisive and the cheap fringes less
attractive than their price suggests. On guest experience for a car-free four:
**Nozawa ≥ Akakura > Hakuba.**

**10. Myoko is `WATCH`** — strong as an operating business, weak as a land-appreciation play.
Eight years of funded investment have not moved land prices, and the lag is already longer than
the Hakuba comparison it relies on. (D-0015)

---

## Immediate next actions

1. **Akakura-level land prices.** The single highest-value test in the project. If Akakura is
   rising while Myoko's municipal average falls, the Myoko bull case survives in the sub-market
   that matters. One data point could move D-0015 either way.
2. **The sprinkler threshold** — floor area, storeys and occupant capacity at which sprinklers
   become mandatory. Largest unresolved cost, and it constrains the guest-capacity question.
   Source: municipal fire authorities.
3. **ADR by market and season.** Blocks all revenue, NOI, yield and capacity optimisation. Nothing
   downstream can be finished without it.
4. **Existing room supply per town** — the missing denominator for the forward supply ratio.
   Without it, 774 Niseko rooms could be a 5% or a 50% increase.
5. **JMA station snowfall series** for each candidate (関山 54816 for Myoko, 野沢温泉 48031 at
   576 m). Ski quality is unscored for every market.
6. **Municipal minpaku ordinances** for Myoko, Hakuba, Nozawa, Madarao, Kutchan. Regulation
   currently does not discriminate between markets because it is unchecked everywhere.
7. **Hakuba's development pipeline** — absent, and Hakuba leads the ranking.
8. **Re-verify the 43 `AVAILABILITY UNVERIFIED` listings** — the first real test of the
   append-only history.
9. **Distance to lift for every candidate** — a core filter, currently empty on every record.
10. **Apply the value-trap checklist to Madarao** before its per-bedroom pricing is treated as
    opportunity.

---

## Requires owner approval

| Item | Why | Blocking? |
| --- | --- | --- |
| **MLIT API registration** | Free, but creates a government account in an owner's name and accepts terms. Would replace the asking-price discount guess with actual transaction prices back to 2005, and is the direct route to the Akakura question. **Recommendation: approve.** See [`outputs/mlit-api-access-decision.md`](mlit-api-access-decision.md) | No |
| Contacting agents, sellers, inspectors, contractors | External contact with real people | Not yet — Phase 15/16 |
| Enabling scheduled collection | Runs automated requests against live sites | No — workflow committed but deliberately disabled |

## Open questions for the owner

- **Capital ceiling.** Total project cost now spans A$544k–1.39m across priority candidates. A
  ceiling would materially focus the work.
- **Return vs lifestyle.** Ranking is stable across four of five weight profiles, so this is
  currently less decisive than expected — but it will matter more as evidence deepens.

---

## Standing rules

- Append, never delete. Never cite a `CANDIDATE` source. Never present an `ESTIMATE` as `FACT`.
- **Never use prefecture data to argue a town-level case** (D-0014).
- Never let a proposed development score like a funded one.
- Never score a market well because negative evidence is missing.
- Respect robots.txt and rate limits; stop rather than press.
- Commit and push after every meaningful unit.

---

## Session log

**2026-08-20 —** Municipality tourism (Hakuba 19-year series; Myoko partial), prefecture occupancy,
203 property records with 3 price events, layered renovation benchmarks, development pipeline,
Myoko bull/bear verdict, Yuzawa case study and `VALUE_TRAP_RISK_CHECKLIST`, town profiles and
micro-location, guest-capacity constraints, MLIT decision note and ingestion interface, monitoring
prototype, and scorecard coverage from 5 to 17 of 20 dimensions. Eight checkpoints pushed.
