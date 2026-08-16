# Project Brief — Japan Ski Property Intelligence

**Domain module:** `japan_ski_property`
**Status:** Active — thesis untested
**Owner decision pending:** none yet; no conclusion has been reached
**Authoritative source:** [`prompts/master-prompt.md`](prompts/master-prompt.md)

---

## 1. The thesis under test

> Two Australians may be able to purchase an undervalued property close to genuinely excellent
> Japanese snow, renovate or reposition it into attractive accommodation, use it personally,
> have tourism materially support ownership costs, and potentially benefit from an emerging ski
> destination appreciating over the next 10–15 years.

**This thesis is not assumed to be correct.** It is the object of investigation. The engine's
job is to discover what the evidence supports, and it is explicitly tasked with trying to
destroy the thesis rather than to confirm it.

### Admissible conclusions

| Verdict | Meaning |
| --- | --- |
| `YES` | The thesis holds broadly on current evidence |
| `YES, ABOVE CAPITAL LEVEL` | Holds only above a determinable capital threshold |
| `YES, IN SPECIFIC MARKETS` | Holds only in named markets, not generally |
| `YES, FOR SPECIFIC PROPERTY TYPES` | Holds only for particular asset types |
| `WATCH` | Not currently actionable; defined triggers would change that |
| `NO` | Evidence does not support the thesis |

A `NO` or `WATCH` outcome is a successful result. The system exists to improve decision
quality, not to justify a purchase.

---

## 2. Who this is for

Two Australian owners, expected to hold 50/50, remaining resident in Australia. They intend to:

- use the property personally for roughly 2–4 weeks each winter;
- operate it commercially as accommodation the rest of the time;
- rely on local management, since they will not be on the ground;
- renovate or reposition where that improves the asset.

They have **no fixed budget yet**. Determining the realistic capital requirement is one of the
project's outputs, not one of its inputs. See `ASSUMPTIONS.md` for the full, explicit list.

---

## 3. Core questions, in order

1. **Where?** Where in Japan is the best intersection of excellent snow, relatively low
   property entry price, growing tourism, good town amenities, accommodation demand,
   manageable renovation, realistic remote operation, year-round potential and future capital
   appreciation?
2. **What?** What property type and guest capacity produce the best economics?
3. **How much?** How much AUD capital would two Australians realistically need?
4. **Which?** Which actual, currently available properties should they inspect?

Every answer must be supported by traceable evidence.

---

## 4. Asset types in scope

Houses · chalets · ski lodges · pensions · guesthouses · ryokan · small hotels · former hotels ·
commercial accommodation · fixer-uppers · multi-building properties.

Owner/manager accommodation within the asset is treated as a positive attribute, because it
reduces the revenue cost of owner use and supports on-site management.

---

## 5. What "good" looks like

### Location
Cheap alone is not enough. Serious candidates sit approximately 0–5, 5–10 or 10–15 minutes from
skiing, and are **not** isolated from shops and restaurants. Greater distances are considered
only where the investment case is exceptional.

### Snow and terrain
For every serious area the engine must be able to answer: *could a serious snowboarder happily
spend seven days here?* — benchmarked against Hakuba and Niseko.

### Town
A property in a town guests do not enjoy is a bad investment regardless of price. Town vibe,
walkability, dining, après, bad-weather options and whether guests would return are treated as
first-class investment inputs, not colour commentary.

### Guest reality
For serious destinations the engine models a concrete scenario: *four Australian snowboarders
book seven nights here — what does their holiday actually look like?* — from airport transfer
through groceries, mountain transport, rest day, bad-weather day and likely repeat visitation.

### Economics
The headline metric is **TOTAL PROJECT COST (AUD)**, never the purchase price:

```
purchase price
+ acquisition costs        + legal              + due diligence
+ renovation               + furnishing         + licensing/compliance
+ initial working capital  + contingency
= TOTAL PROJECT COST
```

Yield is reported against total project cost as well as purchase price. AUD is the primary
displayed currency; JPY is retained alongside with the FX rate and date used.

### Legality
It is never assumed that a residential property can legally become commercial accommodation.
Licensing (Minpaku and its 180-day limit, Hotel Business Act, ryokan and simple-lodging
licences), zoning, fire and evacuation compliance, change of use and licence transferability
are gating research, not footnotes.

---

## 6. What would falsify the thesis

The engine actively researches these. Any one could be decisive:

| Falsifier | Why it matters |
| --- | --- |
| Snow reliability declining | Destroys the underlying product and the 10–15 year horizon |
| Accommodation oversupply | Forward supply outpacing demand growth compresses rates and occupancy |
| Regulatory tightening | Licence unavailability or foreign-ownership restriction can make the model illegal |
| Demographic and population decline | Erodes local services, labour and exit demand |
| Labour shortage | Remote operation depends on local managers, cleaners and contractors existing |
| Renovation cost reality | Mountain construction, snow-load and compliance upgrades can exceed purchase price |
| Exit illiquidity | An asset with no plausible buyer in 10–15 years is a trap, however good the yield |
| FX | AUD/JPY movement changes both entry cost and repatriated income |
| Natural hazard | Earthquake, volcanic, avalanche and flood exposure, and their insurance consequences |
| Already-arbitraged markets | If a market is genuinely obvious, sophisticated capital is likely already there |

Two standing questions are applied to every market:

> **Why is this cheap?**
> **Why hasn't sophisticated capital already arbitraged this opportunity away?**

---

## 7. Geographic scope

No location is assumed to be the answer — explicitly including Myoko. The screening longlist
spans Nagano/Niigata (Myoko Kogen, Madarao, Nozawa Onsen, Hakuba Valley and its lower-cost
fringes, Shiga Kogen, Iiyama, Arai, Yuzawa), Hokkaido (Niseko, Kutchan, Moiwa, Rusutsu, Furano,
Kiroro and other Hokkaido markets) and Tohoku (Appi Kogen and others), plus overlooked and
emerging towns actively discovered during screening rather than taken from a fixed list.

Regions are not treated as single markets. Each serious destination is decomposed into
neighbourhoods and submarkets — walk-to-lift, nightlife, family, premium, quiet, value,
shuttle-dependent, car-dependent — because entry price and guest convenience vary far more
within a resort town than between towns.

---

## 8. Deliverables

| Deliverable | Description |
| --- | --- |
| Destination screening | Japan-wide longlist scored and narrowed with stated criteria |
| Town profiles | Full amenity, vibe and guest-experience profile per serious destination |
| Micro-location analysis | Neighbourhood-level price, convenience and demand comparison |
| Market history | ~10 years of land/property price and transaction data, with CAGR and charts |
| Tourism analysis | ~10 years of visitation, nationality mix, occupancy, ADR, seasonality |
| Development pipeline | Forward-looking, status-classified infrastructure and accommodation supply |
| Regulation dossier | Ownership, licensing, tax, compliance and financing for Australian non-residents |
| Property database | ~20–30 live opportunities with full attributes, history and provenance |
| Renovation models | Three scenarios: minimum viable, good lodge standard, premium repositioning |
| Financial models | Conservative / base / strong, per serious candidate |
| Capital strategies | Shoestring / sensible / strong, total and per owner at 50/50 |
| Inspector network | Independent inspectors and contractors per finalist region |
| Risk and counter-thesis | Structured attempt to destroy each attractive conclusion |
| Ranked shortlist | Best 10 of ~20–30, with thesis and confidence per property |
| Recommendation | Named bests by category, including markets to reject, and what to inspect first |

The final recommendation must not conclude "it depends". It must make evidence-based calls,
including negative ones.

---

## 9. Constraints

- **No Japanese debt is assumed.** Financing for Australian non-residents is researched
  separately; it is upside if available, not a premise.
- **Owners remain in Australia.** Any model requiring their physical presence is invalid.
- **No autonomous external commitments.** The engine does not contact sellers, agents,
  inspectors or contractors, spend money, or enter any obligation. Those are queued for owner
  approval in `outputs/next-actions.md`.
- **Legal and ethical data collection only.** robots.txt, site terms, API limits and rate limits
  are respected; official APIs, government datasets and feeds are preferred over scraping.

---

## 10. Relationship to the core engine

This brief describes the **first domain module**, not the system. The reusable core must remain
domain-agnostic so that later modules — commercial property, development sites, businesses for
sale, other countries, other industries — reuse ingestion, provenance, snapshots, change
detection, scoring, financial modelling and monitoring without redesign.

Where this brief says *property*, the core says `asset`. Where it says *distance to lift*, the
core says `location_metric`. Where it says *new gondola*, the core says `market_catalyst`.
Where it says *renovation*, the core says `value_add_project`. See [`ARCHITECTURE.md`](ARCHITECTURE.md).
