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
| 4 — Destination screening | `ACTIVE` — first pass written |
| 12 — Regulation | `PARTIAL` — brought forward because it is gating |
| 5–11, 13–23 | `PENDING` |

Run the tests with `python3 -m unittest discover -s tests -t . -v` from the repository root.
No install step.

---

## The two findings that matter so far

**1. Narrative and official data disagree about Myoko.**
Hakuba recorded the largest residential land-price rise in Japan for 2026 (+33.0%) and Kutchan
continued rising, while Myoko — the market most heavily promoted to exactly this project's buyer
profile — appears flat to slightly negative on the best figures currently available. That is not
disqualifying; it may be what a pre-capital market looks like. But it means the Myoko case rests
on **anticipated** rather than **realised** appreciation.
→ [`domains/japan_ski_property/research/phase-04-destination-screening.md`](../domains/japan_ski_property/research/phase-04-destination-screening.md)

**2. The buyer is not the constraint; the licence is.**
Foreign freehold ownership is unrestricted with no nationality surcharge. What determines the
business is the operating licence — and the minpaku 180-night cap probably does **not** bind on
a winter-dominant ski property, whose sellable season is ~100–140 nights. It constrains the
four-season upside instead. The genuinely open risk is the **municipal ordinance layer**, which
can designate zero-day lodging zones and varies between neighbouring towns.
→ [`domains/japan_ski_property/regulation/regulatory-baseline.md`](../domains/japan_ski_property/regulation/regulatory-baseline.md)

---

## Immediate next actions

In priority order. Each is independently startable.

1. **Replace every `UNVERIFIED` land-price figure with primary MLIT data.** The Phase 4 finding
   currently rests on secondary commentary published by parties with transactional interests.
   Until this is done, the headline tension is a lead, not a fact.
2. **Retrieve IPSS municipal population projections** for every longlist town. Depopulation is
   the constraint the marketing omits and applies across rural Japan; it must be measured per
   town, not assumed.
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
