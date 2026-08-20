# Provisional market screening output

Generated 2026-08-20 by `scripts/analysis/screen_markets.py --all-profiles`

```text
==============================================================================
PROVISIONAL MARKET SCREENING — NOT A RECOMMENDATION
==============================================================================
Evidence as of : 2026-08-20
Status         : PROVISIONAL - EXPANDED
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
1    Hakuba                 6.84     low          85%        3 of 20
2    Nozawa Onsen           6.22     low          70%        6 of 20
3    Kutchan / Niseko       6.06     low          68%        6 of 20
4    Myoko Kogen            5.78     low          85%        3 of 20

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
1    Hakuba                 6.83     low          87%        3 of 20
2    Nozawa Onsen           6.18     low          71%        6 of 20
3    Kutchan / Niseko       6.01     low          72%        6 of 20
4    Myoko Kogen            5.57     low          86%        3 of 20

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
1    Hakuba                 6.73     low          85%        3 of 20
2    Nozawa Onsen           6.31     low          77%        6 of 20
3    Kutchan / Niseko       6.23     low          65%        6 of 20
4    Myoko Kogen            6.01     low          81%        3 of 20

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
1    Hakuba                 6.91     low          84%        3 of 20
2    Nozawa Onsen           6.25     low          68%        6 of 20
3    Kutchan / Niseko       5.91     low          71%        6 of 20
4    Myoko Kogen            5.61     low          87%        3 of 20

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
1    Hakuba                 6.78     low          87%        3 of 20
2    Kutchan / Niseko       6.40     low          72%        6 of 20
3    Nozawa Onsen           6.05     low          73%        6 of 20
4    Myoko Kogen            5.56     low          84%        3 of 20

  INSUFFICIENT DATA FOR RANKING (needs >=40% coverage and >=10 dimensions):
    Madarao                  coverage 27%, 5 dimensions scored
    Furano                   coverage 23%, 5 dimensions scored
    Yuzawa (control case)    coverage 40%, 7 dimensions scored
    Not ranked. Too little is known to compare these with the others,
    and ranking them on their strongest dimensions alone would reward ignorance.

==============================================================================
SENSITIVITY — does re-weighting actually change the answer?
==============================================================================
  balanced           Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen
  pure_investment    Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen
  lifestyle          Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen
  emerging_upside    Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen
  low_risk           Hakuba > Kutchan / Niseko > Nozawa Onsen > Myoko Kogen

  2 distinct ordering(s) across 5 profiles.
  Ranking is preference-dependent. No single ordering is 'the' answer.

Provisional. See domains/japan_ski_property/research/ for the underlying evidence.

```

---

## What changed since the first pass

Coverage rose from 5 of 20 dimensions to **17 of 20 for Hakuba and Myoko**, 14 for Nozawa and
Kutchan. Three markets are now withheld as `INSUFFICIENT DATA FOR RANKING`.

**Myoko fell from 3rd to last of the ranked four.** The dimensions added since the first pass —
occupancy, capital growth potential, exit liquidity, business growth and a properly evidenced
risk score — all told against it. Its two strongest dimensions (affordability 9.0, town vibe 8.5)
were already scored; almost everything added was negative.

**Nozawa rose to 2nd** on the strength of town structure (9.0, the highest single town-vibe score
awarded) and national #2 land momentum, despite having the lowest base elevation of the Honshu
candidates.

## Guards

Two independent thresholds, because either alone is gameable:

- **Weight coverage ≥40%** — stops a market being carried by one heavily-weighted dimension.
- **≥10 of 20 dimensions** — stops a market qualifying on a handful of its strongest scores.

The second guard was added after Furano ranked **2nd under `pure_investment` on 5 dimensions**,
purely because the only things known about it are favourable. That is precisely the failure the
brief warned against: *do not award a market a high score simply because negative evidence is
missing.*

## Still weak

- **Every market is `low` confidence.** Most component scores are `ESTIMATE`-class.
- **No ADR anywhere**, so no revenue, NOI or yield informs any score.
- **Ski quality is unscored for every market** — no station snowfall data has been retrieved.
- **Infrastructure and future supply are scored only for Myoko and Kutchan**, the two markets
  whose pipelines were researched. Hakuba's absence is a real gap given it leads.
- Municipal regulation is unchecked everywhere, so `regulation` does not currently discriminate.
