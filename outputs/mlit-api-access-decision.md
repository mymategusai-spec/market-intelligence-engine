# Owner decision required: MLIT Real Estate Information Library API

**Prepared:** 2026-08-20
**Decision needed from:** the owners
**Blocking?** **No.** Research continues without it. This slows work; it does not stop it.
**Recommendation:** **Approve** — with one caveat about whose name the account is in.

---

## 1. What it is

The **不動産情報ライブラリ** (Real Estate Information Library), operated by Japan's Ministry of Land,
Infrastructure, Transport and Tourism. It has offered a public API since **April 2024**.

It carries the dataset this project most needs and cannot otherwise get:

| Dataset | Why it matters here |
| --- | --- |
| **不動産取引価格情報 — actual transaction prices** | **The single most valuable dataset in the project.** Everything so far uses *asking* prices |
| Coverage from **Q3 2005**, all 47 prefectures | 20 years of history, per area, per property type |
| 地価公示 published land prices | Currently obtained via a third-party aggregator |
| 都道府県地価調査 prefectural land surveys | Second annual series |
| Urban planning / zoning data | Feeds the Phase 12 municipal gating work |

---

## 2. Cost

**Free.** The API and the data carry no charge. There is no subscription, no metered billing and
no payment instrument required.

---

## 3. What approval actually involves

An **API application** to MLIT (API利用申請). This means:

- creating an account with a Japanese government service **in a named person's name**;
- supplying contact details and a stated purpose of use;
- accepting MLIT's terms of use;
- receiving and storing an API key.

**This is why it has not been done autonomously.** It is not a cost question. It is that
registering an account and accepting terms on the owners' behalf is an external commitment made in
their name, which the operating rules reserve for them (master prompt §53).

---

## 4. What it would change

### Immediately
1. **Replace asking prices with transaction prices.** The current working assumption — that
   slow-moving stock transacts 10–20% below asking — rests on **three observed listings** and is
   survivorship-biased. Transaction data replaces a guess with a measurement.
2. **Remove the aggregator dependency.** Land prices currently come via `tochidai.info` rather
   than MLIT directly. Every figure carries a "corroborated secondary" caveat that would clear.
3. **Answer the Myoko question.** The highest-value outstanding test is whether **Akakura**
   land is rising while the municipal average falls. Transaction-level data by area is the
   direct route to that answer.

### Over time
4. **Real comparables** for valuing specific properties.
5. **20-year price series** per area, enabling the CAGR analysis the brief asks for.
6. **Automated monitoring** of transaction activity as a market-health indicator.

---

## 5. Privacy and credential implications

| Consideration | Assessment |
| --- | --- |
| Personal data required | Name, email, stated purpose. Standard government registration. |
| Data sensitivity | The published data is **already public** and individually anonymised. No personal or transaction-identifying information is exposed. |
| Credential handling | The API key would go in a `.env` file, **already git-ignored**. It must never be committed. |
| Ongoing obligation | None beyond terms of use. No payment instrument, no auto-renewal. |
| Reversibility | An account can be abandoned at any time; no lock-in. |
| Whose name | **The point of decision.** An account should be in an owner's name, not created on their behalf by an agent. |

---

## 6. Recommendation

**Approve, with the account created by an owner personally.**

The value is high and specific, the cost is zero, the data is already public, and the only real
consideration is that a government account should exist in the name of a person who has read and
accepted the terms.

**Suggested route:** an owner registers at the Library's application page, then places the key in
a local `.env` file (never committed). The ingestion interface is already built and will pick the
key up without any code change.

### If the answer is no

Work continues. Land prices remain available through the aggregator with a caveat; transaction
prices remain unavailable and the asking-price discount stays an `ESTIMATE`. The Myoko Akakura
question would need a slower route through municipal land-price points.

---

## 7. Preparation already done

So the decision costs nothing in delay:

- **Ingestion interface built** — `scripts/ingestion/mlit_transactions.py`. It reads the key from
  the environment, and runs in a clearly-labelled unauthenticated mode without one.
- **`.env` is git-ignored**, verified.
- **Source registered** in `SOURCES.md` as `JP-MLIT-REINFOLIB`, status `CANDIDATE`.
- **No account has been created and no terms have been accepted.**
