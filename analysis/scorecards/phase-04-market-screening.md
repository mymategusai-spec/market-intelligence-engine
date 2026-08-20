# Provisional market screening output

Generated 2026-08-20 by `scripts/analysis/screen_markets.py --all-profiles`

```text
==============================================================================
PROVISIONAL MARKET SCREENING — NOT A RECOMMENDATION
==============================================================================
Evidence as of : 2026-08-20
Status         : PROVISIONAL - REVISED WITH MEASURED SNOW, OCCUPANCY AND SUBMARKET DATA
Dimensions     : 20 defined in the scorecard

Unscored dimensions are reported, never substituted with a midpoint - that
would flatter exactly the markets least is known about. Absence of negative
evidence is never scored as a positive.

Markets are ranked only with >=40% weight coverage AND >=10 of 20 dimensions.
Below either threshold: INSUFFICIENT DATA FOR RANKING.

==============================================================================
WEIGHT SET: balanced
  Neutral starting point pending owner preferences. Deliberately not treated as 'correct' — it is a default, not a recommendation.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.85     low          91%        2 of 20
2    Nozawa Onsen           6.39     low          77%        5 of 20
3    Myoko Kogen            6.16     low          91%        2 of 20
4    Kutchan / Niseko       6.15     low          68%        6 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 27%, 5 dimensions scored
    Furano                   coverage 24%, 5 dimensions scored
    Yuzawa (control case)    coverage 36%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
WEIGHT SET: pure_investment
  Return-maximising. Lifestyle factors weighted only insofar as they drive guest demand.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.83     low          91%        2 of 20
2    Nozawa Onsen           6.30     low          74%        5 of 20
3    Kutchan / Niseko       6.13     low          72%        6 of 20
4    Myoko Kogen            6.03     low          90%        2 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 28%, 5 dimensions scored
    Furano                   coverage 27%, 5 dimensions scored
    Yuzawa (control case)    coverage 38%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
WEIGHT SET: lifestyle
  Weighted toward what the owners would enjoy using, while still requiring the operation to be lawful and manageable.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.76     low          94%        2 of 20
2    Nozawa Onsen           6.51     low          86%        5 of 20
3    Myoko Kogen            6.33     low          91%        2 of 20
4    Kutchan / Niseko       6.31     low          65%        6 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 28%, 5 dimensions scored
    Furano                   coverage 24%, 5 dimensions scored
    Yuzawa (control case)    coverage 36%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
WEIGHT SET: emerging_upside
  Seeks earlier-stage markets. Deliberately paired with a high risk weight: emerging markets are cheap for reasons, and this profile must not be allowed to reward optimism.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.91     low          89%        2 of 20
2    Nozawa Onsen           6.40     low          73%        5 of 20
3    Myoko Kogen            6.10     low          92%        2 of 20
4    Kutchan / Niseko       5.99     low          71%        6 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 29%, 5 dimensions scored
    Furano                   coverage 26%, 5 dimensions scored
    Yuzawa (control case)    coverage 35%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
WEIGHT SET: low_risk
  Prioritises evidenced, liquid, well-serviced markets over upside.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.77     low          91%        2 of 20
2    Kutchan / Niseko       6.50     low          72%        6 of 20
3    Nozawa Onsen           6.19     low          78%        5 of 20
4    Myoko Kogen            5.86     low          88%        2 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 27%, 5 dimensions scored
    Furano                   coverage 23%, 5 dimensions scored
    Yuzawa (control case)    coverage 40%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
SENSITIVITY — does re-weighting actually change the answer?
==============================================================================
  balanced           Hakuba > Nozawa Onsen > Myoko Kogen > Kutchan / Niseko
  pure_investment    Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen
  lifestyle          Hakuba > Nozawa Onsen > Myoko Kogen > Kutchan / Niseko
  emerging_upside    Hakuba > Nozawa Onsen > Myoko Kogen > Kutchan / Niseko
  low_risk           Hakuba > Kutchan / Niseko > Nozawa Onsen > Myoko Kogen

  3 distinct ordering(s) across 5 profiles.
  Ranking is preference-dependent. No single ordering is 'the' answer.

Provisional. See domains/japan_ski_property/research/ for the underlying evidence.

```

---

## What changed this revision

Coverage rose to **91% / 18 of 20 dimensions** for Hakuba and Myoko.

**Myoko moved 4th → 3rd**, overtaking Kutchan/Niseko. Three revisions drove it, all from measured
data replacing inference:

- **Property momentum 2.0 → 5.5.** The Akakura submarket is **+7.07%** and Myoko Kogen **+3.54%**
  while the municipality is −0.79%. The municipal average was masking a rising ski micro-market.
- **Capital growth 3.5 → 5.5.** The bear case rested on capital not moving land prices; it has,
  where it was deployed.
- **Winter occupancy 4.0 → 5.5.** Niigata resort hotels reach **64.9% in January (rank 4)** against
  an annual 34.0% (rank 45).

**Snow scores were rebuilt from JMA station normals**, not elevation inference, and the corrections
were large in both directions — Myoko had the most snow of any market and was scored second-lowest;
Furano had the least and was scored highest. See
[`snow-quality-vs-resilience.md`](../../domains/japan_ski_property/research/snow-quality-vs-resilience.md).

## The ranking is now less decision-relevant than the shortlist

Hakuba > Nozawa > Myoko > Kutchan, with only **0.70 points** separating first from fourth on a
10-point scale, every market at `low` confidence.

**That spread is smaller than the uncertainty in the inputs.** Treating this as a market ranking
would over-read it. The useful output at this stage is
[`investment-shortlist.md`](../../domains/japan_ski_property/outputs/investment-shortlist.md) —
specific properties in specific submarkets — because submarket variation (Akakura +7.07% vs Myoko
−0.79%) is larger than the variation between markets.
