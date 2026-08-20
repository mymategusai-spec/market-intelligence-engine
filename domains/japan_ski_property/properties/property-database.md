# Property database — first collection

**Phase:** 13 · **Status:** First pass. 203 property records, 3 observed price events.
**Last updated:** 2026-08-20
**Data:** [`data/property-listings/`](../../../data/property-listings/)

---

## 1. What was collected

| Set | Records | Source | Availability |
| --- | --- | --- | --- |
| Candidate properties (lodge/chalet/pension/house/land) | **51** | Specialist agencies + LIFULL HOME'S | 8 verified at retrieval, 43 `AVAILABILITY UNVERIFIED` |
| Yuzawa resort apartments | **152** | LIFULL HOME'S | Verified at retrieval |
| **Total property records** | **203** | | |
| Listing observations (append-only) | **207** | | |
| Derived price-change events | **3** | | |

By market: Myoko 26 · Hakuba 6 · Madarao 6 · Nozawa Onsen 5 · Kutchan/Niseko 3 · Furano 1 ·
Rusutsu 1 · Naeba 1 · Kijimadaira 1 · Sapporo 1 · **Yuzawa 152**.

**Collection ethics.** LIFULL HOME'S robots.txt was checked on 2026-08-20: the `User-agent: *`
block disallows only functional endpoints (`/kksearch`, `/inquire/`, `/app.php`, review-edit
paths); listing pages are not disallowed. Data was taken from the schema.org JSON-LD embedded in
public listing pages. **The server began returning HTTP 202 after several requests and collection
was stopped rather than pressed.** That is why Hakuba, Nozawa, Kutchan and Iiyama portal sets are
missing — not because they were skipped.

---

## 2. The first real price events — all three are reductions

`FACT` — Three properties were observed at two or more dates from independent sources:

| Property | Market | From | To | Change | Period |
| --- | --- | --- | --- | --- | --- |
| Wonderland Chalet | Myoko | ¥135m | ¥98m | **−27.4%** | Feb–Jul 2026 |
| Kuma Lodge Madarao | Madarao | ¥89m | ¥75m | **−15.7%** | Dec 2023 – Dec 2024 |
| Alpen View Art Villa | Myoko | ¥80m | ¥68m | **−15.0%** | Feb–Jul 2026 |

Mean reduction **−19.4%**. No increases observed.

### The caveat that matters more than the finding

**This sample is survivorship-biased in the worst possible direction.** A property only appears in
two separate listing round-ups *because it did not sell the first time*. Properties that cleared
quickly are structurally absent. So this is a sample of slow movers, and −19.4% is an upper bound
on typical discounting, not an estimate of it.

What it does establish, with n=3:

- **Asking prices in these secondary markets are not firm.** Material reductions happen.
- **`ASSUMPTIONS.md` F3 is supported** — asking price is a biased proxy for transaction value, and
  the bias is downward.
- **The buyer has more negotiating room than the listing suggests**, at least on stock that has
  been sitting.

`ESTIMATE`, low confidence — a first working assumption of **10–20% below asking** for slow-moving
stock in Myoko/Madarao. This must be replaced by MLIT actual transaction data
(`JP-MLIT-TORIHIKI`), which is exactly what the API decision note addresses.

Note also the Wonderland Chalet timing: one source showed ¥135m on 15 Jul and another ¥98m on
23 Jul. An 8-day 27% cut is implausible; the likelier reading is that the ¥135m page was stale.
The record flags `occurred_at_is_inferred: true` and the change is dated to the Feb–Jul window.

---

## 3. Yuzawa: the value trap, now quantified

`FACT` — 152 resort apartments for sale in Yuzawa on a single portal, across just **30 distinct
buildings** — an average of **5.1 simultaneous sellers per building**.

| Asking price | JPY | AUD |
| --- | --- | --- |
| Minimum | ¥350,000 | **A$3,100** |
| 25th percentile | ¥1,400,000 | A$12,500 |
| **Median** | **¥2,500,000** | **A$22,250** |
| 75th percentile | ¥3,750,000 | A$33,400 |
| Maximum | ¥16,000,000 | A$142,400 |

**90% (137 of 152) are under ¥5m (A$44,500).**

Single buildings with the most simultaneous sellers: ステラタワー神立 **17**, ファミール・ヴィラ第２越後湯沢 **14**,
パノラミック湯沢 **13**, ホワイトプラザ湯沢Ｖプラージュ **9**, 西武ヴィラ苗場クリスタル１号館 **9**.

Seventeen owners of one building trying to exit simultaneously is not a market with a liquidity
problem — it is a market with a **demand** problem. Apartments are being offered at A$3,000 and
still not clearing.

**These are not candidate assets** and are not treated as such. They are 1980s–90s bubble-era
units carrying monthly management and repair-reserve charges (管理費・修繕積立金) that are
frequently a large fraction of, or exceed, achievable rent — which is precisely why the asking
price can fall to A$3,000 and still find no buyer. **A price near zero is not a bargain when the
liability is ongoing.**

They are recorded because they are the clearest available evidence for `DECISIONS.md` D-0011: the
Yuzawa control case.

---

## 4. What the candidate set reveals

### Bathrooms, not bedrooms, are the binding constraint
Most candidates are bedroom-rich and bathroom-poor. Wonderland Chalet: 1 bathroom, priced at
¥98m. Myoko Forest Lodge sleeps 20 on 2 baths plus 6 WC/basins. For commercial accommodation the
bathroom ratio drives both guest satisfaction and licence feasibility.

**Exceptions worth noting:** Ski-in Ski-out Chalet Tsugaike (8 bed / **6 bath**), One Happo
(5 bed / 6 bath), Yotei View Retreat (3 **ensuite**).

### An existing licence is visibly rare and valuable
Only **4 of 51** candidates state an accommodation licence: Kodachi Lodge (hotel + minpaku,
operating), Kutchan Town Hotel License, Kutchan Fuso Yotei House, and Echizenya (hot-spring
eligible, not a licence). **Three of the four are in Hokkaido or already operating.** This
supports the existing judgement that a transferable 旅館業法 licence is a major value signal — it
is scarce in the listings actually available.

### Bedrooms per dollar varies by more than 3×

| Property | Beds | AUD | AUD per bedroom |
| --- | --- | --- | --- |
| Madarao Tangram Ridge Runner | 8 | 378,215 | **47,277** |
| Kuma Lodge Madarao | 10 | 667,438 | 66,744 |
| Myoko Forest Lodge | 8 | 978,908 | 122,364 |
| Mont Cervin | 11 | 1,201,388 | 109,217 |
| Alpen View Art Villa | 6 | 605,144 | 100,857 |
| Ski-in Ski-out Chalet Tsugaike | 8 | 845,422 | 105,678 |

`CALCULATION`. **Madarao is conspicuously the cheapest per bedroom** — and Madarao is also where
the observed price reduction occurred. Cheap per bedroom plus falling asking prices is the
signature of weak demand, not of value. **This is exactly the pattern the Yuzawa checklist exists
to catch**, and Madarao should be tested against it before it is treated as an opportunity.

### Myoko's portal stock is not in the ski villages
Of 8 Myoko houses on HOME'S, the cheap ones (¥4.8m, ¥8.99m) are in Gakko-cho and Shinonome-cho —
the **Arai/Niigata-side town centre**, not Akakura or the ski neighbourhoods. Only one
(Shin-Akakura, ¥35m) is in a ski-side location.

This directly confirms `DECISIONS.md` D-0012: within-municipality variation dominates. **A buyer
screening Myoko on municipal median price would be looking at a town 20+ minutes from the snow.**

---

## 5. Priority candidates for inspection

Eight records flagged `HIGH`. The strongest on current evidence:

1. **KUT-001 Kutchan Town Hotel License × Mt. Yotei View** — ¥95m / A$845k. Hotel licence, built
   Dec 2020 (no renovation, no pre-1981 seismic issue), two-unit structure allowing owner use
   without stopping trade, and the fullest data of any record. Expensive, but it eliminates the
   three largest unknowns at once.
2. **MYO-004 Kodachi Lodge & Cottage** — ¥110m / A$979k. Hotel + minpaku licences, operating,
   19 guests, 282 m² on 1,002 m², built 1996/2008.
3. **NOZ-001 Nozawa Onsen Lodge & House** — POA. A 10-bed lodge **plus a separate 3-bed house** is
   exactly the structure that removes the owner-use revenue cost identified in the capital model.
4. **HAK-001 Ski-in Ski-out Chalet Tsugaike** — ¥95m / A$845k. 8 bed / 6 bath, slopeside.
5. **MAD-004 Madarao Tangram Ridge Runner** — ¥42.5m / A$378k. Best bedrooms-per-dollar in the
   set — and therefore the one most needing the value-trap test.

**No contact has been made with any agent or vendor, and none will be without owner approval.**

---

## 6. Honest limitations

- **43 of 51 candidates are `AVAILABILITY UNVERIFIED`.** Sources include round-ups from Dec 2023
  and Dec 2024; those properties may well be sold.
- **Field coverage is poor.** Building size known for 9 of 51; land size for 6; year built for 8;
  bathrooms for 8; licence for 4. Nothing was invented — gaps are recorded as `data_gaps`.
- **No property has a verified distance to lift**, despite that being a core screening filter.
- **No Hokkaido or Hakuba portal data** — collection was stopped at the rate limit.
- **Prices are asking prices**, not transactions.
- AUD conversions are `CALCULATION` at a single 2026-08-16 rate and will drift.

---

## 7. Next

1. Re-verify the `AVAILABILITY UNVERIFIED` set and record confirmations or removals — the first
   real test of the append-only history.
2. Resume portal collection for Hakuba, Nozawa, Kutchan and Iiyama at a slower rate.
3. Add distance-to-lift for every candidate; it is a core filter and is currently empty.
4. Replace the asking-price discount `ESTIMATE` with MLIT transaction data.
5. Apply the Yuzawa value-trap checklist to Madarao before treating its per-bedroom pricing as
   opportunity.
