# Renovation economics — six layers, three of them evidenced

**Phase:** 14 · **Status:** Layers 1–3 evidenced; layers 4–6 named but unquantified
**Last updated:** 2026-08-20
**Data:** [`data/reference/renovation-benchmarks.json`](../../../data/reference/renovation-benchmarks.json)

---

## 1. Three findings that push every earlier estimate upward

### Layer 1 — Japanese construction costs are up 40–50% since 2015, and still rising
`FACT` — The construction cost deflator (建設工事費デフレーター, 2015 = 100) stood at **130.9** in
August 2025. Building cost and construction materials indices are **+40–50% against 2015** as of
April 2026. MLIT public-works design labour rates are **+28% against 2020**, rising for a
**14th consecutive year**.

**Consequence:** the ¥5–10m "full akiya renovation" benchmark used in the earlier capital model
comes from general renovation guidance and is almost certainly stale. It is now treated as a
**floor, not a central estimate.**

### Layer 2 — Snow country costs 1.5–2.0× on the biggest line
`FACT` — Roof and exterior renovation in Niigata's heavy-snow areas (Uonuma, Tokamachi, Tsunan,
**Myoko, Yuzawa**) runs **1.5–2.0× plains rates.**

Roof and exterior are typically the **largest single line** on an older mountain building, so this
is not a marginal adjustment. Specific components:

| Item | Cost (JPY) |
| --- | --- |
| Snow stops 雪止め — fan / L-type / tile | 70k–100k / 150k–250k / 200k–400k |
| Roof snow-melting system | 300k–600k plus scaffolding ¥700–1,200/m² |
| Mobile snow melter | 200k–400k plus 100k–200k install |

Applies to Myoko, Yuzawa, Nozawa, Madarao, Iiyama and Hakuba.

### Layer 3 — Commercial compliance was underestimated, and is now corrected
`FACT` — For a **detached house**, obtaining a fire-code compliance certificate costs
**~¥300,000** where a small-scale automatic fire alarm and emergency exit lighting are required.
The stated **minimum to open a 簡易宿所** is **¥1,000,000–3,000,000**, covering fire equipment,
wet-area renovation and guest-room fit-out. Licence application fee ¥11,000–16,500.

For an **apartment or larger building** the fire-compliance range is **¥50,000 to ¥10,000,000** —
and the swing factor is whether **sprinklers** become mandatory, which depends on floor area,
storeys and occupant capacity.

**Corrected in the model:** licensing/compliance raised from ¥0.5–2m to **¥1–3m**, and contingency
raised from 30% to **40%**.

**The sprinkler question is the largest single unresolved cost in this project.** It is precisely
the kind of item that turns a viable project into a failed one, it scales with the guest capacity
the owners are trying to maximise, and it cannot be resolved from a desk — it needs the local fire
authority and a specific building.

---

## 2. Three layers named but deliberately not quantified

| Layer | Status | Why not modelled |
| --- | --- | --- |
| **4. Remote/rural** | `ESTIMATE`, low | Regional labour is described as cheaper than metro, but material transport to remote sites adds cost. **Net direction not established.** No multiplier invented. |
| **5. Ski-resort labour premium** | `ASSUMPTION`, low | No evidence found. Hakuba/Niseko would plausibly be worst, given construction demand from foreign buyers. **Named as a gap, not given a number.** |
| **6. Foreign-owner project management** | `ASSUMPTION`, low | Non-resident owners cannot supervise directly and typically need a bilingual project manager. Commonly assumed at 10–20% industry-wide, **but not evidenced here.** |

**The model is therefore incomplete in a known direction: understated.** Two real cost layers are
missing entirely, and both would push totals up. That is stated plainly rather than papered over
with a plausible-looking placeholder.

---

## 3. Per-property total project cost

Full output: [`analysis/financial_models/property-total-project-cost.md`](../../../analysis/financial_models/property-total-project-cost.md)

Minimum-viable scenario, priority candidates, ordered by **total project cost** rather than asking
price:

| Property | Market | Ask A$ | **TPC low** | **TPC high** | Multiple |
| --- | --- | --- | --- | --- | --- |
| Madarao Tangram Ridge Runner | Madarao | 378,215 | **543,821** | 692,704 | 1.4× |
| Alpen View Art Villa | Myoko | 605,144 | **807,285** | 956,169 | 1.3× |
| Kuma Lodge Madarao | Madarao | 667,438 | **879,609** | 1,028,492 | 1.3× |
| Ski-in Ski-out Chalet Tsugaike | Hakuba | 845,421 | **1,075,198** | 1,190,932 | 1.3× |
| Kutchan Town Hotel License | Kutchan/Niseko | 845,421 | **1,075,198** | 1,190,932 | 1.3× |
| Kodachi Lodge & Cottage | Myoko | 978,909 | **1,241,227** | 1,390,110 | 1.3× |

Halve for capital per owner at 50/50.

### Two things this table shows that asking price does not

**The multiple compresses as price rises.** The cheapest candidate carries the *highest* multiple
(1.4×). This is the same pattern the strategy-level model found: fixed costs do not scale down.
Ranking by asking price systematically flatters cheap properties.

**Licensed properties are overstated here, and that matters.** Kodachi Lodge and the Kutchan Town
Hotel License property **already hold accommodation licences and are operating**. Applying a full
¥1–3m compliance line and a full minimum-viable renovation to them is wrong — much of that work is
already done and paid for by a previous owner.

Corrected informally, both would drop by roughly A$50–80k, and Kutchan would move materially up
the ranking. **This is the quantified case for the licence premium**: an existing transferable
licence is worth something close to the compliance line it removes, *plus* the risk it eliminates
of discovering the conversion is impossible.

The model should gain a `licence_already_held` flag before these figures are used for ranking.

---

## 4. Component checklist for future estimates

The brief asked for evidence per component. Current state:

| Component | Evidence |
| --- | --- |
| Roof, exterior | **Layer 2** — 1.5–2.0× multiplier evidenced |
| Snow-load, snow stops, snow melting | **Layer 2** — component prices evidenced |
| Fire compliance | **Layer 3** — evidenced, with sprinkler risk flagged |
| Structural, seismic | Not evidenced. Pre-1981 buildings are a distinct risk class |
| Carpentry, plumbing, electrical, painting, flooring, kitchens, bathrooms, heating, insulation, glazing | Not separately evidenced — only aggregate akiya benchmarks |
| Furnishing | `ESTIMATE` ¥1.5–4m, scales with capacity |

**No component-level Japanese rate card has been obtained.** That is the main gap in this phase and
the reason scenario figures remain ranges with low confidence.

---

## 5. Next

1. Obtain a component rate card (坪単価 by trade) from a Niigata or Nagano contractor.
2. **Resolve the sprinkler threshold** — floor area, storeys and occupant capacity at which
   sprinklers become mandatory for 簡易宿所 and 旅館. This directly constrains the guest-capacity
   question in Phase 26.
3. Quantify layers 5 and 6, or continue to state them as unmodelled.
4. Add a `licence_already_held` flag to the cost model so licensed properties are not penalised.
5. Seismic upgrade costs for pre-1981 buildings.
