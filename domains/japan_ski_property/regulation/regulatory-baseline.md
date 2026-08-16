# Regulatory baseline (Phase 12 — early findings)

**Status:** Partial. National framework established; municipal layer outstanding.
**Last updated:** 2026-08-16

> Researched ahead of schedule because regulation is **gating**: a market where the intended
> operating model cannot be made lawful is disqualified regardless of every other score
> (`config/domains/japan_ski_property/scoring_components.json`).

---

## 1. Can the owners buy at all? — Yes

`FACT` — Foreigners may own **land and buildings freehold** in Japan. There is no
nationality-based restriction on ownership, and no nationality-based tax surcharge. Non-residents
hold the same ownership rights as citizens. [S7, S8]

This removes a commonly assumed blocker. It also means **`ASSUMPTIONS.md` C3 is only half
resolved**: buying is unrestricted, but *operating commercial accommodation* is a separate
question answered by licensing, below.

### Obligations specific to non-resident buyers

`FACT` — A report must be filed with the **Ministry of Finance within 20 days** of purchase.
Non-compliance carries penalties of up to 6 months imprisonment or a ¥500,000 fine. [S7]

`FACT` — Non-residents have additional reporting obligations and appoint a **tax
representative** (納税管理人) in Japan. [S7]

**Implication for modelling:** the tax representative is a recurring operating cost and a
required service provider. It belongs in `service_provider` records and in the operating cost
model, not as an afterthought.

---

## 2. Acquisition costs — evidenced, not assumed

`FACT` — Transaction costs run approximately **6–8% above the purchase price**: [S7, S8]

| Item | Rate |
| --- | --- |
| Agent commission | 3% + ¥60,000, plus 10% consumption tax (≈3.3%) |
| Registration / transfer tax | 1.5% land, 2.0% buildings (reductions may apply) |
| Real estate acquisition tax | ≈3% of **assessed** value, one-off, billed after purchase |
| Judicial scrivener / legal | Variable |

Two modelling notes:

- Acquisition tax is levied on **assessed** value, not purchase price. For a cheap building on
  a larger land parcel the two can diverge substantially — this cannot be modelled as a flat
  percentage of the purchase price without saying so.
- The acquisition tax arrives **months after settlement**. A buyer who has spent their entire
  capital at closing meets an unexpected bill. This belongs in working capital.

---

## 3. The real constraint: the operating licence

**Buying is easy; operating lawfully is the question.** Three distinct legal regimes: [S9]

| Regime | Statute | Annual limit | Threshold |
| --- | --- | --- | --- |
| Minpaku | 住宅宿泊事業法 (Private Lodging Business Act) | **180 nights** | Notification (届出) |
| Simple lodging 簡易宿所 | 旅館業法 (Hotel Business Act) | Unlimited | Licence (許可) |
| Ryokan / hotel | 旅館業法 | Unlimited | Licence, higher fire/safety/management thresholds |

### Minpaku requirements for foreign owners
`FACT` — Facility plans, fire-safety compliance confirmation, advance neighbour notification
(近隣説明), and a designated management contact **reachable 24/7**. [S9]

The 24/7 contact requirement is not a formality for owners living in Australia. It is a
**structural requirement for local management** — and therefore direct evidence for gating
assumption C2.

### The 180-night cap — read carefully

The cap is routinely described as crippling. For this project's use case, that framing is
probably wrong, and the distinction matters for screening:

- A Japanese ski season runs roughly December to early April — on the order of **100–140
  sellable nights**. A winter-dominant property is unlikely to reach 180 nights of *demand*.
- What the cap forecloses is the **four-season upside** — summer hiking, biking, festivals —
  which is precisely the diversification the master prompt asks about in §19.

**Therefore:** minpaku-only status constrains the *diversification* case, not the *core winter*
case. It should be scored as a limit on `off_season_demand` and `capital_growth_potential`,
not treated as fatal to the investment. A 旅館業法 licence is what unlocks year-round trading.

This also explains why **an existing, transferable 旅館業法 licence is one of the strongest
value signals in this domain** — it is the difference between a capped side income and an
unrestricted accommodation business, and it is already a first-class field in
`schemas/domains/japan_ski_property/property.json`.

### Special zones (特区民泊)
`FACT` — 365-day operation is possible in designated National Strategic Special Zones (Osaka
City, Tokyo Ōta-ku, Kitakyushu and others). [S9]
**No ski market on the longlist is currently known to be a special zone.** Do not assume this
route is available; verify per municipality.

---

## 4. The municipal layer — outstanding, and decisive

`FACT` — Municipalities may impose stricter local ordinances (条例) on top of national law,
including designating residential zones where minpaku may operate **zero days per year**. [S9]

**This is the single largest open regulatory risk in the project.** National rules are uniform;
the binding constraint is local, and it varies between neighbouring towns. A property could
satisfy every national requirement and still be unable to trade.

Local opposition to foreign investment — already documented in Myoko
([Phase 4 screening](../research/phase-04-destination-screening.md) §3) — is a **leading
indicator of ordinance tightening**. Municipalities under development pressure from residents
are exactly the ones most likely to restrict lodging.

### Required per longlist town, before any recommendation
- [ ] Municipal minpaku ordinance, and any zero-day zones
- [ ] Zoning (用途地域) and whether lodging is permitted at the specific parcel
- [ ] Local fire and evacuation requirements for the relevant licence class
- [ ] Whether an existing licence transfers on sale, or must be re-applied for
- [ ] Any restriction specific to foreign owners at municipal level

---

## 5. Still outstanding

| Question | Why it matters | Phase |
| --- | --- | --- |
| Licence **transferability** on sale | Determines whether buying a licensed lodge preserves its licence — potentially decisive between two otherwise similar properties | 12 |
| Fire and evacuation standards by licence class | A major and frequently omitted renovation cost | 12/14 |
| Food service licensing | Required if meals are served; changes the operating model | 12 |
| Change of use, residential → lodging | The core question for every fixer-upper candidate | 12 |
| GK / company structures | May affect tax and liability for two non-resident owners | 12 |
| Ongoing taxation of rental income for non-residents | Directly affects modelled NOI | 12/17 |
| Financing for Australian non-residents | Currently assumed unavailable (`ASSUMPTIONS.md` D1) | 12 |
| Visa / residency implications | Not required for ownership; relevant only if plans change | 12 |

---

## 6. Effect on assumptions

| Assumption | Was | Now |
| --- | --- | --- |
| C3 — commercial operation legally achievable | `TESTING`, Low | **Partly resolved.** Ownership unrestricted; a lawful national path exists via 旅館業法. Remains `TESTING` on the **municipal** layer, which is where it can still fail. |
| D1 — no Japanese debt assumed | `HELD` | Unchanged; financing research outstanding. |

---

## Sources

| Ref | Source | Tier | Accessed |
| --- | --- | --- | --- |
| S7 | Japanese property ownership and tax guides (multiple, independent) | 4 | 2026-08-16 |
| S8 | Corroborating property guides | 4 | 2026-08-16 |
| S9 | Minpaku and Hotel Business Act regulation commentary | 4 | 2026-08-16 |

**Caveat.** All findings here rest on **Tier 4 secondary commentary**, not on primary statute or
ministry guidance. The framework is consistent across independent sources, which supports the
broad shape — but **no figure or rule here should be relied on for a transaction** until
confirmed against `JP-MHLW-RYOKAN`, `JP-MINPAKU` and the relevant municipal ordinance.
Regulatory detail is exactly where secondary summaries go stale.
