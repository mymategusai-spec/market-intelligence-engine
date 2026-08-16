# Next Actions

**Last updated:** 2026-08-16
**Branch:** `main`
**Current phases:** 4 (destination screening, active) · 12 (regulation, partial)
**Overall status:** Foundations complete. Research under way. **No investment conclusion
reached, and none should be inferred from anything in this repository.**

This is the handoff file. Read it first, then `prompts/master-prompt.md`, `PROJECT_BRIEF.md`
and `RESEARCH_PLAN.md`.

---

## Where the project stands

| Phase | Status |
| --- | --- |
| 1 — Architecture and foundations | `DONE` |
| 2 — Core schemas and engine | `DONE` — 104 tests, stdlib only |
| 3 — Domain module `japan_ski_property` | `DONE` |
| 4 — Destination screening | `ACTIVE` — first pass complete, six markets scored |
| 7 — Historical property markets | `PARTIAL` — 2026 land prices + 30-year histories |
| 8 — Tourism | `PARTIAL` — prefecture level, plus Myoko municipal |
| 12 — Regulation | `PARTIAL` — brought forward because it is gating |
| 21 — Risk and counter-thesis | `PARTIAL` — brought forward, snow and depopulation |
| 5, 6, 9–11, 13–20, 22, 23 | `PENDING` |

```bash
python3 -m unittest discover -s tests -t . -v          # 104 tests, no install step
python3 scripts/analysis/screen_markets.py --all-profiles --explain
```

The screening script runs the whole engine path on real evidence — config in, evidence in,
explained and reproducible ranking out. Change a weight in
`config/domains/japan_ski_property/weights.json` and re-run to see the ranking move.

**Current provisional order** (5 of 20 dimensions scored, all `low` confidence, Kutchan and
Furano withheld for insufficient coverage): **Hakuba > Nozawa Onsen > Myoko > Yuzawa**, stable
across every weight profile. [`analysis/scorecards/phase-04-market-screening.md`](../analysis/scorecards/phase-04-market-screening.md)
explains why that stability is weaker evidence than it appears — two of the five scored
dimensions derive from the same land-price dataset.

---

## The findings that matter so far

**1. Japanese ski land is three markets, not one.** Corroborated across two independent sources
to within 0.02pp:

| Regime | Markets (2026 公示地価 change) |
| --- | --- |
| Recovering strongly | Hakuba **+26.9%** (national #1), Nozawa Onsen **+21.7%** (#2) |
| Established, still rising | Kutchan **+12.3%**, Furano **+6.7%** |
| Flat or still falling | Myoko **−0.79%**, Yuzawa **−0.44%** |

→ [`domains/japan_ski_property/property_market/land-price-regimes.md`](../domains/japan_ski_property/property_market/land-price-regimes.md)

**2. Narrative and official data disagree about Myoko.** The market promoted hardest to exactly
this project's buyer profile bottomed in 2022, has recovered ~5%, and was still negative in 2026.
That is not disqualifying — it may be what a pre-capital market looks like — but the Myoko case
rests on **anticipated** rather than **realised** appreciation. It yields a monitorable
prediction: land prices should turn positive as the 2028 first stage approaches.

**3. Yuzawa is a documented 33-year value trap, and is now the benchmark.** Down **85%** from its
1993 peak and *still falling*, despite Shinkansen access, snow and abundant cheap stock. Every
cheap candidate must now answer: *what is different here that was not true of Yuzawa?* (D-0011)

**4. Nozawa Onsen was under-weighted and has been promoted.** National **#2** for appreciation,
with a fraction of Myoko's promotional coverage — precisely what an evidence-led screen should
surface and a sentiment-led one would miss.

**5. Neighbourhood matters about twice as much as town.** Within-town land-price spreads are
**11.1× in Hakuba** and **14.0× in Myoko**, against ~6× between municipalities. No property may
be scored on a market-level view alone (D-0012).

**6. Snow risk is real, and elevation-specific.** Japan's operational resort count is **40% below
its 1999 peak**. Peer-reviewed work finds snow declining at **low elevations on the Japan Sea
side**, but stable-to-heavier at **high elevations in eastern Honshu**, with no clear decline in
Hokkaido. Takada — adjacent to Myoko — is one of two stations named as showing marked decline.
Base elevation and regional regime are now screening criteria (D-0013).

**7. Depopulation is severe, and worst in the cheapest market.** Myoko is projected to lose
**46.7% of its population by 2050**. The sharper screening question is not "is the town
shrinking?" but "**has tourism demonstrably decoupled from resident decline here?**" Hakuba and
Kutchan appear to have; Myoko has not yet; Yuzawa did not over 33 years.

**7a. Myoko's own tourism numbers complicate its case — in both directions.** Myoko City's 4th
Tourism Promotion Plan (municipal government, the best tourism source obtained so far) records
**120,000 foreign overnight stays in FY2023** against Niigata's ~820,000 prefecture-wide. Myoko
is a **minority of the prefecture**, so the +55% cannot be attributed to it — weakening the
strongest evidence for the early-stage case. The city's own target is ~7%/year to 2029, modest
against a prefecture that grew 55% in a year.

But international visitors reportedly stay **one to two weeks** in Myoko Kogen, with Australians
specifically drawn there. For a self-contained lodge that is the single most valuable demand
characteristic found anywhere in this research: fewer turnovers, lower cleaning cost per night,
less marketing dependence. **The volume case is weaker than it looked; the quality-of-demand case
is stronger than anything else found.**

**8. A hypothesis now worth stating plainly.** The cheap Honshu markets tend to be lower-elevation
Japan Sea side *and* more severely depopulating. That is not a coincidence, and it is the most
plausible current answer to *why hasn't capital arbitraged this away?* — **the discount may be
compensation for real risk rather than an oversight.** Testing this is the central task of
Phases 5–11.
→ [`domains/japan_ski_property/research/thesis-critical-risks.md`](../domains/japan_ski_property/research/thesis-critical-risks.md)

**9. The buyer is not the constraint; the licence is.**
Foreign freehold ownership is unrestricted with no nationality surcharge. What determines the
business is the operating licence — and the minpaku 180-night cap probably does **not** bind on
a winter-dominant ski property, whose sellable season is ~100–140 nights. It constrains the
four-season upside instead. The genuinely open risk is the **municipal ordinance layer**, which
can designate zero-day lodging zones and varies between neighbouring towns.
→ [`domains/japan_ski_property/regulation/regulatory-baseline.md`](../domains/japan_ski_property/regulation/regulatory-baseline.md)

---

## Immediate next actions

In priority order. Each is independently startable.

1. **Retrieve land prices directly from MLIT**, upgrading `verification_status` from
   `CORROBORATED_SECONDARY`. Also retrieve the missing municipalities — Niseko-cho, Shiga
   Kogen/Yamanouchi, Iiyama (which contains Madarao), Appi/Hachimantai, Rusutsu, Kiroro — and
   build full year-by-year series with 1/3/5/10-year change and CAGR for survivors.
2. **Retrieve IPSS municipal population projections** for every longlist town. Depopulation is
   the constraint the marketing omits and applies across rural Japan; it must be measured per
   town, not assumed.
3. **Retrieve IPSS projections for Hakuba, Nozawa, Kutchan, Iiyama, Yuzawa and Furano.**
   Currently only Myoko's is known, so no cross-market comparison is possible. This is the
   highest-priority single gap — it is what would show whether the appreciating markets are
   also the depopulating ones.
4. **Pull JMA station series** for each candidate: 30+ years, with station elevation and
   distance recorded alongside. This resolves E3 per market rather than nationally.
5. **Research Nozawa Onsen properly.** Newly promoted on evidence; currently the largest gap
   between what the data says and what has actually been researched. Note its **565 m base** is
   the lowest of the Honshu candidates — the land-price signal and the snow-risk signal point in
   opposite directions here.
6. **Read the two peer-reviewed snow papers in full.** The elevation-dependence finding is
   load-bearing for screening and was accessed via summary only.
3. **Establish the accommodation capacity of the Patience Capital Myoko development.** Until
   room and bed counts are known it cannot enter the forward supply ratio — and a large nearby
   development raises a destination's profile *and* its competing supply at once.
4. **Pull JMA measured snowfall** for candidate towns and compare against marketed figures. The
   schema already stores both separately; the station's distance and elevation must be recorded
   with each figure.
5. **Check municipal minpaku ordinances** for Myoko, Hakuba, Nozawa, Madarao and Kutchan.
6. **Research the towns nobody is marketing.** Yuzawa first — a known cheap resort-apartment
   market and a clean test of whether cheap and viable coincide. Phase 4 cannot close until the
   screen has looked where the marketing does not.
7. **Check portal robots.txt and terms** before designing any Phase 13 collector. This may
   constrain the whole collection approach, so establish it before building.

---

## Known blockers

| Blocker | Impact | Status |
| --- | --- | --- |
| MLIT per-municipality land-price detail not in the press release | Phase 4's main finding stays `UNVERIFIED` | Detail pages and the Real Estate Information Library identified; retrieval is the next step |
| Japan Today returns HTTP 403 | One Myoko source unavailable | Worked around — same wire story via Financial Express; recorded in `SOURCES.md` |
| `gh` CLI token invalid | No PR/issue/API via `gh` | Not blocking — `git push` works via keychain. Fix with `gh auth login -h github.com` |
| No package manager or index access | Cannot install third-party libraries | **Resolved by design** — stdlib-only core (D-0002) |

---

## Requires owner approval

Never actioned autonomously (master prompt §53).

| Item | Why it needs approval | Blocking? |
| --- | --- | --- |
| **MLIT Real Estate Information Library API registration** | Free, but creates an account in the owners' name — an external commitment. Would give programmatic access to **actual transaction prices** from Q3 2005, the highest-value dataset for Phases 7, 13 and 22 | **No** — the same data is browsable without the API. It slows research, it does not stop it |
| Contacting agents, sellers, inspectors, contractors | External contact with real people | No — not needed until Phase 15/16 |
| Purchasing paid data | Spends money | No — none identified as necessary yet |
| Creating paid cloud resources | Spends money | No — the dashboard is designed to be static and free (D-0007) |

---

## Open questions for the owner

None blocking. Both would sharpen the work when convenient:

- **Capital ceiling.** Currently open-ended (`ASSUMPTIONS.md` A3). The engine will derive
  shoestring / sensible / strong requirements regardless, but a rough ceiling would focus
  screening considerably.
- **Return vs lifestyle weighting.** Five weight profiles exist and are fully adjustable.
  `balanced` is being used as a neutral default and is explicitly flagged as *not* the owners'
  stated preference.

---

## Standing rules for whoever works next

- Do not delete historical observations. Append.
- Do not cite a `CANDIDATE` source as evidence, or present an `ESTIMATE` as a `FACT`.
- Do not let a proposed development score like a funded one.
- Do not assume a residential property can lawfully be operated as commercial accommodation.
- Treat commentary from brokerages and developers as conflicted (D-0009); label it, use it, do
  not rely on it alone.
- Search Japanese-language sources. English-only research systematically over-weights the
  internationalised markets — the ones least likely to be undervalued.
- Commit and push to `origin/main` after every meaningful work unit.
- Update this file, `CHANGELOG.md`, `SOURCES.md`, `ASSUMPTIONS.md` and `DECISIONS.md` as work
  proceeds, not in a batch at the end.

---

## Session log

**2026-08-16 —** Intake blocker resolved when the owner supplied the master prompt. Phases 1–3
completed: architecture, core schemas and engine logic (104 tests), and the
`japan_ski_property` domain module with its scoring configuration. Phase 4 first pass written,
surfacing the narrative-versus-data tension on Myoko and the conflicted-source problem. Phase 12
brought forward, resolving foreign ownership favourably and identifying the municipal ordinance
layer as the largest open regulatory risk.
