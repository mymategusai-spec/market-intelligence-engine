# Inspector and contractor network

**Phase:** 15 · **Status:** First pass. National providers identified; region-specific coverage thin.
**Last updated:** 2026-08-20

> **Research only. No provider has been contacted, and none will be without owner approval.**

---

## 1. The regulatory frame

`FACT` — A home inspection in Japan is formally a **建物状況調査 (Building Condition Survey)**. Since
the **2018 revision to the Real Estate Brokerage Act**, agents must inform buyers about the option
of a third-party building condition survey by a certified inspector.

**This matters for these buyers.** It establishes an accepted, named process a foreign buyer can
request without it appearing unusual — and it means the survey is a recognised professional
product, not an ad-hoc favour.

`FACT` — Any registered architect (**一級建築士** first-class / **二級建築士** second-class) can
conduct a building condition survey. This widens the pool considerably beyond dedicated inspection
firms, and matters in rural ski towns where dedicated inspectors may not operate.

---

## 2. Providers identified

| Provider | Type | Coverage | English | Independence |
| --- | --- | --- | --- | --- |
| **さくら事務所 Sakura Jimusho** | Independent inspection firm | Nationwide | **English-capable staff for some services** | Independent of agencies |
| **日本検査機構 Japan Inspection Organization** | Registered certification & inspection agency | Nationwide | Not established | Registered agency |
| **Kamakura Zaimoku** | Full-service home builder | **Nagano, with a dedicated Hakuba presence** | **English-speaking** | **Builder, not inspector — conflicted for inspection** |
| Licensed architects (一級/二級建築士) | Individual professionals | Local, per region | Varies | Independent if separately engaged |

`FACT` — Some inspection companies provide reports in English or Chinese; **not all do**.

---

## 3. Against the brief's target, this is short

The brief asks, per serious region, for **2 independent inspectors, 2 builders, 1 architect or
compliance adviser, 1 property-management option**.

| Region | Inspectors | Builders | Architect/compliance | Management |
| --- | --- | --- | --- | --- |
| Hakuba | 0 named locally (2 national) | **1 (Kamakura Zaimoku)** | 0 | 0 named |
| Myoko | 0 | 0 | 0 | 0 named |
| Nozawa | 0 | 0 | 0 | 1 implied (rental-managed apartment observed) |
| Niseko/Kutchan | 0 named locally | 0 | 0 | Implied — most developed operator market |

**Only one region-specific provider has been identified anywhere**, and it is a **builder**, which
disqualifies it from inspecting a property it might then quote to renovate.

---

## 4. The independence rule, restated

The master prompt is explicit: **selling agents must never be relied on for structural advice**,
and serious properties need **two separate engagements** —

1. an **independent structural/building inspection**, and
2. a **separate renovation/commercial-conversion estimate**.

Kamakura Zaimoku illustrates why. It is English-speaking, Hakuba-based and full-service — genuinely
useful for **(2)**. Using it for **(1)** would mean asking a builder to assess how much building
work a property needs. That is a conflict, however reputable the firm.

**The capital model already provisions for both** (`due_diligence` covers inspection; renovation
estimating is separate), so this is budgeted, not an afterthought.

---

## 5. Why this gap is more serious than it looks

Three findings converge on inspection being the highest-value due diligence in this project:

1. **Renovation is the largest and least certain cost** — 35% of a shoestring project, `ESTIMATE`
   class, and known to be understated because ski-resort labour and foreign-owner premiums are
   unquantified.
2. **Snow-country buildings carry specific failure modes** — roof snow load, ice damming,
   insulation, and the 1.5–2.0× cost premium on roof and exterior work.
3. **Pre-1981 seismic standard** divides the Japanese building stock into two materially different
   risk classes, and **year built is known for only 8 of 51 candidates.**

**A buyer who skips inspection is not saving A$2,000–5,000; they are gambling the largest and
least predictable line in the budget.**

---

## 6. Next

1. **Confirm さくら事務所's English service and coverage in Nagano and Niigata**, and get an
   indicative fee. The most promising lead — independent, national, English-capable.
2. **Find 建築士 in Myoko/Jōetsu and Nozawa/Iiyama.** Prefectural architect association registers
   are the route; municipal offices also maintain lists.
3. **Ask specifically about hospitality conversion experience** — the 旅館業法 fire and evacuation
   requirements are specialist, and the sprinkler threshold is the largest unresolved cost.
4. **Property management is the biggest gap** — no named provider in any market, and
   `ASSUMPTIONS.md` C2 (management procurable) remains a low-confidence **gating** assumption.
5. Search Japanese-language directories. This pass was English-biased, which systematically finds
   foreign-facing firms and misses local ones.

**All contact requires owner approval and is queued in `outputs/next-actions.md`.**
