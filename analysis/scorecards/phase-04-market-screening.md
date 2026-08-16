# Provisional market screening output

Generated: 2026-08-16 by `scripts/analysis/screen_markets.py --all-profiles`

Regenerate with:

```
python3 scripts/analysis/screen_markets.py --all-profiles --explain
```

```text
==============================================================================
PROVISIONAL MARKET SCREENING — NOT A RECOMMENDATION
==============================================================================
Evidence as of : 2026-08-16
Scored         : affordability, property_price_momentum, snow_reliability, tourism_growth, risk
Unscored       : 15 of 20 scorecard dimensions have no evidence at all

Missing entirely: ski quality, town vibe, amenities, accessibility, rental
demand, occupancy, off-season demand, management availability, regulation,
renovation opportunity, business growth, infrastructure, future supply
balance, capital growth potential, exit liquidity.

The engine reports these as missing rather than substituting a midpoint,
which would flatter exactly the markets least is known about.

Markets below 25% weight coverage are withheld from ranking entirely.

==============================================================================
WEIGHT SET: balanced
  Neutral starting point pending owner preferences. Deliberately not treated as 'correct' — it is a default, not a recommendation.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 7.04     low          29%        15 of 20
2    Nozawa Onsen           6.12     low          29%        15 of 20
3    Myoko Kogen            5.50     low          29%        15 of 20
4    Yuzawa                 4.69     low          29%        15 of 20

  Withheld — evidence coverage below 25%:
    Kutchan / Niseko       coverage 23% (would have scored 5.86)
    Furano                 coverage 16% (would have scored 7.00)
    Too little is known to rank these against the others.

==============================================================================
WEIGHT SET: pure_investment
  Return-maximising. Lifestyle factors weighted only insofar as they drive guest demand.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 7.18     low          28%        15 of 20
2    Nozawa Onsen           6.32     low          28%        15 of 20
3    Myoko Kogen            5.42     low          28%        15 of 20
4    Yuzawa                 4.69     low          28%        15 of 20

  Withheld — evidence coverage below 25%:
    Kutchan / Niseko       coverage 22% (would have scored 5.75)
    Furano                 coverage 16% (would have scored 6.74)
    Too little is known to rank these against the others.

==============================================================================
WEIGHT SET: lifestyle
  Weighted toward what the owners would enjoy using, while still requiring the operation to be lawful and manageable.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 7.00     low          26%        15 of 20
2    Nozawa Onsen           5.91     low          26%        15 of 20
3    Myoko Kogen            5.36     low          26%        15 of 20
4    Yuzawa                 4.43     low          26%        15 of 20

  Withheld — evidence coverage below 25%:
    Kutchan / Niseko       coverage 23% (would have scored 6.15)
    Furano                 coverage 17% (would have scored 7.33)
    Too little is known to rank these against the others.

==============================================================================
WEIGHT SET: emerging_upside
  Seeks earlier-stage markets. Deliberately paired with a high risk weight: emerging markets are cheap for reasons, and this profile must not be allowed to reward optimism.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 7.24     low          31%        15 of 20
2    Nozawa Onsen           6.34     low          31%        15 of 20
3    Kutchan / Niseko       5.82     low          25%        16 of 20
4    Myoko Kogen            5.40     low          31%        15 of 20
5    Yuzawa                 4.66     low          31%        15 of 20

  Withheld — evidence coverage below 25%:
    Furano                 coverage 19% (would have scored 6.83)
    Too little is known to rank these against the others.

==============================================================================
WEIGHT SET: low_risk
  Prioritises evidenced, liquid, well-serviced markets over upside.
==============================================================================

#    Market                 Score    Confidence   Coverage   Unscored
------------------------------------------------------------------------------
1    Hakuba                 6.80     low          27%        15 of 20
2    Nozawa Onsen           5.83     low          27%        15 of 20
3    Myoko Kogen            4.90     low          27%        15 of 20
4    Yuzawa                 4.10     low          27%        15 of 20

  Withheld — evidence coverage below 25%:
    Kutchan / Niseko       coverage 22% (would have scored 6.52)
    Furano                 coverage 13% (would have scored 7.33)
    Too little is known to rank these against the others.

==============================================================================
SENSITIVITY — does re-weighting actually change the answer?
==============================================================================
  balanced           Hakuba > Nozawa Onsen > Myoko Kogen > Yuzawa
  pure_investment    Hakuba > Nozawa Onsen > Myoko Kogen > Yuzawa
  lifestyle          Hakuba > Nozawa Onsen > Myoko Kogen > Yuzawa
  emerging_upside    Hakuba > Nozawa Onsen > Kutchan / Niseko > Myoko Kogen > Yuzawa
  low_risk           Hakuba > Nozawa Onsen > Myoko Kogen > Yuzawa

  2 distinct ordering(s) across 5 profiles.
  Ranking is preference-dependent. No single ordering is 'the' answer.

Provisional. See domains/japan_ski_property/research/ for the underlying evidence.

```

---

## How to read this

**The ranking is stable across every weight profile.** Hakuba > Nozawa Onsen > Myoko > Yuzawa
holds under balanced, pure-investment, lifestyle and low-risk weights; only `emerging_upside`
differs, and only by admitting Kutchan.

That looks like a robust result. It is weaker than it appears, for three reasons:

1. **The scored dimensions are correlated.** `affordability` and `property_price_momentum` are
   both derived from the same land-price dataset. Two of five scored dimensions are effectively
   one piece of evidence, so the market that wins on land prices wins overall almost by
   construction. Stability across weight profiles does not establish robustness across
   *evidence*.
2. **Only 5 of 20 dimensions are scored.** Everything that would distinguish these markets for
   an operator — town vibe, amenities, accessibility, rental demand, occupancy, management
   availability, regulation, exit liquidity — is absent. The dimensions most likely to reorder
   this table have not been researched.
3. **Confidence is `low` for every market.** The engine propagates confidence to the weakest
   input, and most inputs are `ESTIMATE`-class judgements from thin evidence.

**Kutchan and Furano are withheld, not rejected.** Their evidence coverage (22% and 13% of total
weight) is too low to rank them honestly. Furano would have scored top under two profiles purely
because the only dimensions scored for it are its strong ones — it has no risk score, and risk
carries the heaviest weight in several profiles. Ranking it would have rewarded ignorance.

**Yuzawa is included as a benchmark, not a candidate** (`DECISIONS.md` D-0011). It ranks last
under every profile, which is the expected result and a basic sanity check on the scoring.

## What would change this table

- Municipality-level tourism data, distinguishing Myoko from Niigata prefecture as a whole.
- JMA station snowfall series, replacing regional inference with measurement.
- IPSS population projections for the markets other than Myoko.
- Any evidence at all on town vibe, amenities, management availability or exit liquidity.
- Actual property listings, which would replace land-price proxies with real entry costs.
