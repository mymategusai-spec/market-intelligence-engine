# Source Register

Every source the engine uses, its reliability tier, how it is accessed, and whether that access
is permitted. Material claims in this repository must cite a `source_id` from this register.

**Status:** `CANDIDATE` (identified, not yet accessed) · `ACCESSED` (used, URL verified) ·
`BLOCKED` (unavailable — reason recorded) · `REJECTED` (terms prohibit use, or unreliable)

**Tier** follows the hierarchy in `ARCHITECTURE.md` §4 — 1 is highest.

> **Integrity note.** A `CANDIDATE` entry records *intent to use*, not a verified fact. URLs on
> candidate rows are identifications from domain knowledge and **must be confirmed on first
> access**; a row is only promoted to `ACCESSED` once actually retrieved, with its access date
> recorded. Nothing in this register may be cited as evidence while still `CANDIDATE`.

---

## 1. Japanese government — national (Tier 1)

| ID | Source | Publisher | What it provides | Status |
| --- | --- | --- | --- | --- |
| `JP-MLIT-CHIKA` | 地価公示 (Published Land Prices) | MLIT 国土交通省 | Official annual land valuations by point, long series | `CANDIDATE` |
| `JP-PREF-CHIKA` | 都道府県地価調査 | Prefectures via MLIT | Second annual land-price series, wider coverage | `CANDIDATE` |
| `JP-MLIT-TORIHIKI` | 不動産取引価格情報 (Real Estate Transaction Prices) | MLIT | **Actual transaction** prices by area — critical, since asking prices are biased | `CANDIDATE` |
| `JP-ESTAT` | e-Stat 政府統計の総合窓口 | Statistics Bureau | Portal for all official statistics; has an API | `CANDIDATE` |
| `JP-JUTAKU-TOCHI` | 住宅・土地統計調査 (Housing and Land Survey) | Statistics Bureau | Vacancy rates, akiya counts, dwelling stock by municipality | `CANDIDATE` |
| `JP-KEIZAI-CENSUS` | 経済センサス (Economic Census) | Statistics Bureau / METI | Business counts by industry and municipality — Phase 9 backbone | `CANDIDATE` |
| `JP-JMA-SNOW` | 気象庁 observation data (積雪・降雪) | Japan Meteorological Agency | Measured snow depth and snowfall by station, long series — the antidote to marketing snowfall claims | `CANDIDATE` |
| `JP-JTA-SHUKUHAKU` | 宿泊旅行統計調査 (Accommodation Survey) | Japan Tourism Agency 観光庁 | Overnight stays, occupancy, foreign/domestic split by prefecture | `CANDIDATE` |
| `JP-JNTO` | Visitor arrivals statistics | JNTO | Inbound arrivals by nationality, monthly, long series | `CANDIDATE` |
| `JP-MHLW-RYOKAN` | 旅館業法 (Hotel Business Act) guidance | MHLW 厚生労働省 | Hotel / ryokan / simple-lodging licence categories and requirements | `CANDIDATE` |
| `JP-MINPAKU` | 住宅宿泊事業法 (Minpaku Act) portal | MLIT / Japan Tourism Agency | Private-lodging rules, 180-day limit, notification process | `CANDIDATE` |
| `JP-POP-PROJ` | Population projections by municipality | IPSS 国立社会保障・人口問題研究所 | Depopulation risk — a Phase 21 falsifier | `CANDIDATE` |

## 2. Prefectural and municipal (Tier 2)

| ID | Source | Covers | What it provides | Status |
| --- | --- | --- | --- | --- |
| `PREF-NAGANO` | Nagano Prefecture statistics and tourism | Hakuba, Nozawa, Madarao, Shiga Kogen, Iiyama | Tourism, planning, population | `CANDIDATE` |
| `PREF-NIIGATA` | Niigata Prefecture statistics and tourism | Myoko, Yuzawa, Arai | Tourism, planning, population | `CANDIDATE` |
| `PREF-HOKKAIDO` | Hokkaido Government statistics | Niseko, Kutchan, Furano, Rusutsu, Kiroro | Tourism, planning, population | `CANDIDATE` |
| `PREF-IWATE` | Iwate Prefecture statistics | Appi Kogen | Tourism, planning, population | `CANDIDATE` |
| `MUNI-*` | Individual municipal sites | per town | Zoning, planning approvals, local lodging restrictions, budgets | `CANDIDATE` |
| `AKIYA-BANK-*` | 空き家バンク (municipal vacant-house banks) | per town | Genuinely cheap stock largely absent from English portals | `CANDIDATE` |

Municipal sources are registered individually as each town enters serious research, because
local lodging restrictions and zoning are decided at municipal level and vary sharply between
neighbouring towns.

## 3. Tourism organisations and industry (Tier 3–5)

| ID | Source | What it provides | Status |
| --- | --- | --- | --- |
| `DMO-*` | Local DMOs and tourism associations | Visitation, events, off-season programming, lift data | `CANDIDATE` |
| `RESORT-*` | Ski resort operators | Lifts, terrain, vertical, season dates, capex announcements | `CANDIDATE` |
| `JP-PROPERTY-CENTRAL` | Japan Property Central | English commentary on Japanese property law, tax and market data | `CANDIDATE` |

Resort operator material is marketing. Snowfall and visitation figures from operators are
recorded as `OPINION` or low-confidence `ESTIMATE` unless corroborated by `JP-JMA-SNOW` or
official statistics.

## 4. Property listing sources (Tier 4)

| ID | Source | Coverage | Access note | Status |
| --- | --- | --- | --- | --- |
| `PORTAL-SUUMO` | SUUMO | Large domestic residential portal | **Terms and robots.txt must be checked before any automated access** | `CANDIDATE` |
| `PORTAL-ATHOME` | at home | Domestic residential | Same | `CANDIDATE` |
| `PORTAL-HOMES` | LIFULL HOME'S | Domestic residential | Same | `CANDIDATE` |
| `PORTAL-RAKUMACHI` | 楽待 | Income-producing property — lodges, pensions, small hotels | Same | `CANDIDATE` |
| `PORTAL-KENBIYA` | 健美家 | Income-producing property | Same | `CANDIDATE` |
| `AGENT-*` | Local and foreign-facing agencies | Resort-town specific stock | Same | `CANDIDATE` |

**Access rule.** No portal is crawled until its robots.txt and terms have been checked and
recorded in this register. Where automated access is prohibited, the source is marked
`REJECTED` for automation and any use is manual and attributed. This constraint is
non-negotiable (master prompt §33) and is expected to shape Phase 13's design.

**Coverage bias.** Japanese-language portals carry stock that never appears in
English-language listings. A search confined to English sources would systematically miss the
cheap end of the market — precisely where the thesis expects to find value.

## 5. Community and anecdotal (Tier 6)

| ID | Source | What it provides | Status |
| --- | --- | --- | --- |
| `COMM-*` | Forums, review platforms, trip reports, local blogs | Town vibe, crowding, whether restaurants book out, whether the town is dead at 8pm, guest sentiment | `CANDIDATE` |

Tier 6 is often the *only* source for questions the master prompt treats as first-class
investment inputs (§12). It is used, labelled `OPINION`, corroborated across independent
sources where possible, and never presented as `FACT` or used alone for a material claim.

---

## Accessed sources

Populated as research proceeds. Each row records source ID, exact URL, publisher, publication
date, access date, what was extracted, and reliability tier.

| ID | URL | Publisher | Published | Accessed | Extracted | Tier |
| --- | --- | --- | --- | --- | --- | --- |
| `JP-MLIT-CHIKA` | `mlit.go.jp/report/press/tochi_fudousan_kensetsugyo04_hh_000001_00074.html` | MLIT | 2026-03-17 | 2026-08-16 | 令和8年地価公示 press release: 26,000 survey points; all-use, residential and commercial each rose for a 5th consecutive year. **Per-municipality figures are not in the release** — they are in the linked detail pages, still to be retrieved. | 1 |
| `JP-MLIT-REINFOLIB` | `reinfolib.mlit.go.jp` | MLIT | — | 2026-08-16 | Real Estate Information Library. Confirms an official **API since April 2024** covering published land prices, prefectural land surveys, **actual transaction prices** (from Q3 2005) and urban planning data, all 47 prefectures, free. **API use requires an application.** | 1 |
| `JP-JMA-SNOW` | `data.jma.go.jp/risk/obsdl/` and `data.jma.go.jp/stats/etrn/` | Japan Meteorological Agency | — | 2026-08-16 | Confirms downloadable historical station data including snow depth (積雪深) and cumulative snowfall, with CSV export. This is the antidote to marketed snowfall claims. | 1 |
| `SEC-PATIENCE-REALTY` | `patiencerealty.com` | Patience Realty | 2026 | 2026-08-16 | 2026 land prices: Hakuba Village **+33.0%** largest residential rise nationwide; Chitose **+44.1%** largest commercial. **Conflict: a brokerage with transactional interest; shares a name with the Myoko developer.** | 4 |
| `SEC-PROPERTY-COMMENTARY` | various | Multiple property commentators | 2026 | 2026-08-16 | Per-market land-price averages (Kutchan, Hakuba, Myoko) and the Myoko population projection. **All `UNVERIFIED`** pending MLIT and IPSS primary data. | 5 |
| `SEC-MOTHERSHIP-PCG` | `mothership.sg` | Mothership.SG | 2025-03 | 2026-08-16 | Patience Capital Group Myoko development: 350 ha, ~US$1.4bn/S$1.8bn, first stage 2028, up to ¥70bn, ¥35bn raised incl. Mizuho, Pavilion Capital. | 5 |
| `SEC-JP-REGULATION` | various | Japanese property and lodging-law commentators | 2026 | 2026-08-16 | Foreign ownership unrestricted; acquisition costs ~6–8%; MoF report within 20 days; minpaku 180-night cap; 旅館業法 licence classes; municipal ordinance powers incl. zero-day zones. | 4 |

---

## Blocked and rejected sources

| ID | Source | Reason | Alternative pursued |
| --- | --- | --- | --- |
| `SEC-JAPANTODAY` | Japan Today article on foreign investment in Myoko | **HTTP 403** on direct fetch (2026-08-16) | Same wire story carried by The Financial Express; substance captured via search summary. Claim recorded at Tier 5 with the access failure noted. |

Blockers are recorded rather than worked around silently. Where a source is unavailable, the
alternative pursued is named, so a later reader can judge whether a gap in the evidence is a
research failure or a genuine data limitation.

---

## Paid sources — owner decision required

Sources requiring payment are never purchased autonomously (master prompt §53). Any identified
during research are listed here with what they would add and an indicative cost, for the owner
to decide.

| Source | What it would add | Indicative cost | Status |
| --- | --- | --- | --- |
| *(no paid source identified yet)* | | | |

### Free, but requiring registration — owner decision

| Source | What it would add | What it requires | Status |
| --- | --- | --- | --- |
| `JP-MLIT-REINFOLIB` API | Programmatic access to **actual transaction prices** (not asking prices) from Q3 2005, published land prices and prefectural land surveys, all 47 prefectures — the single highest-value dataset for Phases 7, 13 and 22 | A **free API application** to MLIT, which means creating an account in the owners' name | **Awaiting owner approval.** Registering an account is an external commitment made on the owners' behalf and is not done autonomously. The same data is browsable without the API, so research is not blocked — only slowed. |
