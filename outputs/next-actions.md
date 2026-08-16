# Next Actions

**Last updated:** 2026-08-16
**Branch:** `task/bootstrap-intake`
**Status:** Blocked at intake — awaiting the master prompt.

---

## Current repository state

| Item | State |
| --- | --- |
| Commits | 1 (`d2557d8` — "Initialise market intelligence engine") |
| Tracked files | `README.md` (empty, 0 bytes) |
| Remote | `origin` → `github.com/mymategusai-spec/market-intelligence-engine` |
| Project docs | None (no `CLAUDE.md`, no brief, no phase definitions) |
| Source code | None |
| Data / outputs | None prior to this file |

---

## Blocker

**What is needed:** the master prompt (project brief / phase definitions).

**Why it matters:** the autonomy instruction directs work to proceed "through the phases
sequentially," resolving open questions from "the master prompt, repository documentation,
existing data, or standard engineering/research practice." Three of those four sources are
empty, and the fourth cannot substitute for them:

- The repository contains no brief, spec, phase list, or documentation of any kind.
- There is no existing data to infer scope from.
- No prior Claude Code session exists for this project — the session transcript directory
  contains only the current session, and project memory is empty.
- Standard practice can supply *how* to build a market intelligence engine, but not *what
  market*, *whose competitors*, *which sources*, or *what deliverables* — and every one of
  those choices determines essentially all downstream work.

**Why this was not resolved by assumption:** the unknown is the entire subject matter, not a
detail. Guessing an industry, a competitor set, and an output format would produce a
plausible-looking codebase with a high probability of being wholly irrelevant. There is no
conservative reversible default for "which market to analyse."

**Searched before escalating:**

```
git log --stat --all                     # 1 commit, empty README
find . -not -path './.git/*'             # .claude/, README.md only
~/.claude/projects/-Users-gusai-market-intelligence-engine/   # current session only
~/.claude/projects/.../memory/           # empty
find ~ -maxdepth 3 -iname '*master*prompt*' -o -iname '*market*intel*' -o -iname '*brief*'
```

---

## To unblock

Provide the master prompt by whichever route is easiest:

1. **Paste it into the session** — fastest; work resumes immediately.
2. **Commit it to the repo** — e.g. `docs/master-prompt.md`, then say so. Preferred for
   durability: it survives session boundaries and future runs can read it directly.
3. **Point at a file path or URL** and it will be read in.
4. **Ask for a draft** — a candidate scope can be proposed (market, sources, phases,
   deliverables) for approval or editing, rather than the brief being written from scratch.

The minimum needed to start Phase 1 productively:

- **Market / domain** — the industry, category, or vertical under analysis.
- **Subject** — whose position this serves (a company, product, or neutral market view).
- **Deliverables** — reports, dashboard, dataset, API, alerting, or some combination.
- **Sources** — which data sources are in scope, and which credentials exist for them.
- **Phases** — the sequence the work should follow, if a specific one is intended.

---

## Secondary blocker: GitHub authentication

`gh auth status` reports the token for `mymategusai-spec` is invalid:

```
X Failed to log in to github.com account mymategusai-spec (default)
  - The token in default is invalid.
```

Re-authenticate with `! gh auth login -h github.com` in this session (the `!` prefix runs it
here, so the output lands in the conversation). Credentials are not altered or created
without explicit approval, so this is left for the owner.

Push status for this branch is recorded in the session handoff.

---

## Work completed this session

- Repository, git state, session history, and project memory surveyed for the master prompt.
- Task branch `task/bootstrap-intake` created (main left untouched, per the working contract).
- This blocker record written and committed.

## Deferred pending the master prompt

Everything below is deliberately *not* started, because each would encode a guess about the
domain that is likely wrong:

- Language, runtime, and dependency choices.
- Repository scaffolding, module layout, and test harness.
- Data source integrations and credential/secret handling (`.env.example`).
- Schema design for collected market data.
- Output format, and the reporting or visualisation layer.

No further independent work can be done without materially guessing at scope.
