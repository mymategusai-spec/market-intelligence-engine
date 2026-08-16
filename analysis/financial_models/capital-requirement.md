# Capital requirement — illustrative model output

Generated 2026-08-16 by `scripts/analysis/capital_model.py --strategies`

```text
==============================================================================
CAPITAL REQUIREMENT MODEL — ILLUSTRATIVE, NOT A VALUATION
==============================================================================
FX          : 112.37 JPY/AUD as at 2026-08-16 (recent range ~110-114)
Cost inputs : data/reference/cost-assumptions.json

No revenue, NOI or yield is produced. Nightly rates and occupancy have not
been obtained, and inventing them would be false precision.

Purchase prices below are ROUND ILLUSTRATIVE FIGURES spanning a plausible
range. Phase 13 has not yet collected real listings.

==============================================================================
SHOESTRING — purchase ¥8,000,000, minimum_viable
  Lowest level at which the attempt is responsible. A cheap fixer-upper, minimum viable renovation, small guest capacity.
==============================================================================

                                           LOW (A$)          HIGH (A$)
------------------------------------------------------------------------------
Purchase price                               71,193             71,193
Agent commission                              2,349              2,349
Registration + acquisition tax                2,705              2,705
Legal / scrivener                             1,780              4,450
Due diligence / inspection                    1,335              4,450
Renovation                                   44,496             88,992
Furnishing                                   13,349             35,597
Licensing / compliance                        4,450             17,798
Working capital (6 months)                   12,014             19,222
Contingency (30% of reno)                    13,349             26,698
------------------------------------------------------------------------------
TOTAL PROJECT COST                          167,020            273,454
  per owner at 50/50                         83,510            136,727

Purchase price alone                         71,193             71,193
Total cost / purchase price                   2.35x              3.84x

  Purchase price understates the real investment by 135%-284%.

==============================================================================
SENSIBLE — purchase ¥25,000,000, good_lodge_standard
  Something genuinely commercially viable without constantly fighting limitations.
==============================================================================

                                           LOW (A$)          HIGH (A$)
------------------------------------------------------------------------------
Purchase price                              222,479            222,479
Agent commission                              7,342              7,342
Registration + acquisition tax                8,454              8,454
Legal / scrivener                             1,780              4,450
Due diligence / inspection                    1,335              4,450
Renovation                                  106,790            222,479
Furnishing                                   13,349             35,597
Licensing / compliance                        4,450             17,798
Working capital (6 months)                   31,236             44,852
Contingency (30% of reno)                    32,037             66,744
------------------------------------------------------------------------------
TOTAL PROJECT COST                          429,252            634,644
  per owner at 50/50                        214,626            317,322

Purchase price alone                        222,479            222,479
Total cost / purchase price                   1.93x              2.85x

  Purchase price understates the real investment by 93%-185%.

==============================================================================
STRONG — purchase ¥60,000,000, premium_repositioning
  A stronger asset with better revenue and resale prospects.
==============================================================================

                                           LOW (A$)          HIGH (A$)
------------------------------------------------------------------------------
Purchase price                              533,950            533,950
Agent commission                             17,620             17,620
Registration + acquisition tax               20,290             20,290
Legal / scrivener                             1,780              4,450
Due diligence / inspection                    1,335              4,450
Renovation                                  266,975            533,950
Furnishing                                   13,349             35,597
Licensing / compliance                        4,450             17,798
Working capital (6 months)                   73,685            100,917
Contingency (30% of reno)                    80,093            160,185
------------------------------------------------------------------------------
TOTAL PROJECT COST                        1,013,527          1,429,207
  per owner at 50/50                        506,763            714,604

Purchase price alone                        533,950            533,950
Total cost / purchase price                   1.90x              2.68x

  Purchase price understates the real investment by 90%-168%.

==============================================================================
HEALTH WARNINGS
==============================================================================

  * Renovation benchmarks are for RESIDENTIAL akiya work. Lawful COMMERCIAL
    accommodation adds fire, evacuation and possibly seismic work that those
    benchmarks exclude. Assume commercial conversion costs materially more.

  * Licensing/compliance is the least reliable line in the model. Phase 12 has not
    established the standards, and this could be several times the figure shown.

  * The acquisition tax is charged on ASSESSED value, not purchase price, and arrives
    months after settlement. A buyer who spends everything at closing meets a bill.

  * Working capital is proxied from build cost, not from a measured operating budget.

  * FX is doing real work here. AUD has risen from ~84 JPY in 2021 to ~112 in 2026, so
    the same Japanese property is ~25% cheaper in AUD than it was. Part of the "Japan is
    cheap" story is AUD strength, and it is reversible over a 10-15 year hold.

  * Every figure above is an ESTIMATE-class range. No contractor has quoted, no
    inspector has been engaged, and no property has been priced.

```
