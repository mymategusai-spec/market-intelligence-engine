# Assumptions

Everything the analysis takes as given, stated explicitly so it can be challenged, tested or
overturned. An assumption is not evidence. Anything here that later acquires a source moves to
`FACT` and is recorded in `SOURCES.md`.

**Status:** `HELD` (in force) · `TESTING` (evidence being gathered) · `CONFIRMED` (evidenced,
now a fact) · `RETIRED` (shown false or no longer relevant)

**Confidence:** how much weight the assumption can currently bear.

---

## A. Owners and ownership

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| A1 | Two Australian owners, both resident in Australia | `HELD` | High | Owner brief | Owner statement |
| A2 | Ownership likely 50/50 | `HELD` | Medium | Owner brief ("likely") | Owner specifies a different split; tax or structuring advice favours otherwise |
| A3 | No fixed budget yet; capital requirement is an output, not an input | `HELD` | High | Owner brief | Owner sets a ceiling |
| A4 | Preference for low acquisition cost | `HELD` | High | Owner brief | Owner reprioritises toward asset quality over entry price |
| A5 | Owners remain non-resident and will not relocate to Japan | `HELD` | Medium | Owner brief implies remote ownership | Owner considers residency; visa research changes the calculus |
| A6 | Owner personal use ≈ 2–4 weeks each winter | `HELD` | Medium | Owner brief | Owner revises intended use; modelling shows use cost is decisive |

## B. Asset and location

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| B1 | Property should be close to genuinely good snow | `HELD` | High | Owner brief | — (core requirement) |
| B2 | Property should not be isolated from shops and restaurants | `HELD` | High | Owner brief | Exceptional investment case for an isolated asset |
| B3 | Fixer-uppers are acceptable | `HELD` | High | Owner brief | Renovation cost research shows unacceptable risk at owners' capital level |
| B4 | ~0–15 minutes from skiing is the acceptable band | `HELD` | Medium | Master prompt §10 | Evidence that guests accept more, or that shuttle quality makes distance irrelevant |
| B5 | Guest capacity is an open variable (6 → 20+), not a given | `HELD` | High | Master prompt §26 | Phase 17 identifies an economic optimum |

## C. Operating model

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| C1 | Local management will be required | `HELD` | High | Owners remain in Australia (A5) | Owners appoint an on-site partner or relocate |
| C2 | Competent local management can actually be procured in the chosen market | `TESTING` | **Low** | Assumed pending Phase 16 | Phase 16 finds no providers → market may be disqualified |
| C3 | Commercial accommodation operation is legally achievable for the asset type and market | `TESTING` | **Low–Medium** | Partly evidenced 2026-08-16: foreign freehold ownership is unrestricted, and a lawful national path to unlimited operation exists via a 旅館業法 licence. See [regulatory baseline](domains/japan_ski_property/regulation/regulatory-baseline.md) | The **municipal** layer, which is where this can still fail: local ordinances can designate zero-day lodging zones. Must be checked per town |
| C4 | Tourism revenue can materially support ownership costs | `TESTING` | **Low** | This is the thesis, not a premise | Phase 17 modelling |

## D. Finance

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| D1 | No Japanese debt is available; model all-cash | `HELD` | Medium | Master prompt §47 — conservative default | Phase 12 finds accessible non-resident financing; treated as upside, never as premise |
| D2 | AUD is the primary reporting currency; JPY retained with rate and date | `HELD` | High | Master prompt §21 | — |
| D3 | FX rates are recorded per observation, never applied retrospectively | `HELD` | High | Provenance requirement | — |
| D4 | Purchase price is never the true investment cost | `HELD` | High | Master prompt §24 | — |

## E. Market

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| E1 | No location is presumed to be the answer, explicitly including Myoko | `HELD` | High | Master prompt §9 | Evidence, at the end of screening — not at the start |
| E2 | Some Japanese ski markets are currently undervalued relative to fundamentals | `TESTING` | **Low** | This is the thesis under test | Phases 4–11, 21. May resolve to `NO` |
| E3 | Japanese snow quality remains commercially viable over a 10–15 year horizon | `TESTING` | **Low–Medium** | Advanced 2026-08-16. **No longer a single question.** Peer-reviewed evidence shows the trend is elevation- and region-dependent: declining at low elevations on the Japan Sea side, stable-to-heavier at high elevations in eastern Honshu, no clear decline in Hokkaido. Japan's operational resort count is down 40% from its 1999 peak. See [thesis-critical risks](domains/japan_ski_property/research/thesis-critical-risks.md) | Now assessed per candidate: *is snow viable at this elevation, in this regional regime?* JMA station series per market will resolve it |
| E6 | Tourism demand can decouple from resident population decline in a resort town | `TESTING` | **Medium for Hakuba, Low elsewhere** | Added 2026-08-16. Hakuba and Kutchan appear to have decoupled; Myoko has not yet; Yuzawa did not, over 33 years. Myoko is projected to lose 46.7% of its population by 2050 | Per-market evidence of tourism growth sustained against resident decline. This is the question that separates a recovering market from a value trap |
| E4 | Inbound tourism to Japan continues at or above current levels | `TESTING` | Low | Assumed pending Phase 8 | Tourism trend data; shock scenarios |
| E5 | A resort region is not a single market; neighbourhoods differ materially | `HELD` | Medium | Master prompt §14; standard property practice | Evidence of price uniformity within towns |

## F. Method and system

| ID | Assumption | Status | Confidence | Basis | What would change it |
| --- | --- | --- | --- | --- | --- |
| F1 | Public, permitted sources provide enough data for a defensible conclusion | `TESTING` | Medium–High | Strengthened 2026-08-16: MLIT publishes actual transaction prices and land values free, and JMA publishes measured snowfall free. The highest-value datasets are public | Material data proving available only from paid providers → owner decision required |
| F6 | Accessible English-language commentary on Japanese ski property is systematically biased toward markets its publishers transact in | `HELD` | Medium | Observed 2026-08-16: the most prominent "emerging market" commentary is published by brokerages and developers with direct interests. See Phase 4 screening §3 | Discovery of substantial independent English-language coverage; or Japanese-language sources showing the same emphasis |
| F2 | Committed files are sufficient as a datastore at this volume | `HELD` | Medium | `ARCHITECTURE.md` §5 | Volume or query needs justify a DuckDB index over the files |
| F3 | Asking prices are a usable but biased proxy where transaction data is unavailable | `HELD` | Medium | **Strengthened 2026-08-20:** three properties observed at two dates all showed reductions, mean −19.4%. But the sample is survivorship-biased toward slow movers, so that is an upper bound on discounting, not an estimate | MLIT transaction data — see `outputs/mlit-api-access-decision.md` |
| F7 | A winter-dominant property's economics must be modelled on winter-season occupancy, not annual occupancy | `HELD` | High | Added 2026-08-20. A property trading Dec–Mar and closed otherwise is structurally capped near 25–33% annual occupancy even at 100% winter occupancy. Nagano's 39.6% annual figure is partly a seasonality artefact | Nothing — this is arithmetic |
| E7 | Inbound growth offsets domestic decline | `TESTING` | **Low** | Added 2026-08-20. Japan's 2025 total overnight stays fell 0.8%: foreign +8.2% did NOT offset Japanese −3.8%. Every bullish argument in this project rests on inbound growth | Per-market evidence that inbound growth exceeds domestic decline in beds, not percentages |
| F4 | Historical listing records will become valuable comparable evidence | `HELD` | Medium | Master prompt §55 | — (drives the append-only rule) |
| F5 | Machine translation of Japanese sources is adequate for research, with material claims verified against the original | `HELD` | Medium | Practical necessity | Material misreading discovered → escalate to human translation |

---

## Assumptions deliberately **not** made

Recorded because assuming them would be the easy, and wrong, path:

- That a residential property can legally be operated as commercial accommodation.
- That a proposed development will be built.
- That marketing snowfall figures are accurate.
- That an English-language listing market represents the whole market — it does not, and the
  gap is precisely where undervaluation would be expected to survive.
- That cheap means undervalued. Cheap usually means correctly priced for a reason that has not
  yet been identified.
- That the owners' thesis is correct.

---

## Review protocol

Reviewed at the end of every phase. Any assumption still at **Low** confidence when it feeds a
material conclusion is escalated in `outputs/next-actions.md` rather than quietly relied upon.
The gating assumptions — **C2, C3, E3** — can each independently disqualify a market or the
whole thesis, and are researched before any recommendation is drafted.
