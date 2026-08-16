# Changelog

Meaningful changes to the engine, its data and its conclusions. Newest first.

Format: date · phase · what changed · why it matters.

---

## 2026-08-16

### Phase 1 — Foundational repository · `DONE`

- Saved the owner's master prompt verbatim to `prompts/master-prompt.md` as the authoritative
  brief, with an amendments section for later owner instructions.
- Established the two-layer architecture: domain-agnostic `core/` and domain modules under
  `domains/`, with a one-directional dependency rule.
- Created the repository structure: `config/`, `core/`, `schemas/`, `domains/`, `data/`,
  `analysis/`, `app/`, `scripts/`, `workflows/`, `tests/`, `outputs/`.
- Wrote foundational documentation: `README.md`, `PROJECT_BRIEF.md`, `ARCHITECTURE.md`,
  `RESEARCH_PLAN.md`, `ASSUMPTIONS.md`, `DECISIONS.md`, `SOURCES.md`.
- Set the dependency policy to Python 3.9+ stdlib only after verifying the environment has no
  package manager and no package-index access (`DECISIONS.md` D-0002).
- Populated the source register with the official Japanese statistical, land-price, tourism,
  meteorological and regulatory sources the research will depend on, each marked `CANDIDATE`
  pending first access.
- Recorded initial assumptions, flagging **C2** (management procurable), **C3** (commercial
  operation legally achievable) and **E3** (snow viable over 10–15 years) as low-confidence
  gating assumptions that can each independently disqualify a market or the thesis.

### Repository intake

- Recorded and then resolved the intake blocker: the master prompt was not present in the
  repository at session start, and was supplied by the owner mid-session.

---

## Conventions

- **Data changes** note which append-only path was written and how many records were added.
- **Conclusion changes** note what evidence moved the conclusion, and its confidence.
- **Retractions** are recorded explicitly. A number that turns out to be wrong is corrected in
  the log, not quietly overwritten — the correction is itself intelligence about source
  reliability.
