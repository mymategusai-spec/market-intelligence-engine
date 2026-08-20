# Property-level financial models — full output

Generated 2026-08-20. Regenerate:

```bash
python3 scripts/analysis/property_financials.py
python3 scripts/analysis/capacity_sweep.py
```

```text
========================================================================================================
PROPERTY-LEVEL FINANCIAL MODELS  —  renovation scenario: minimum_viable
========================================================================================================
Season: 76 high-season nights (22 Dec - 7 Mar), 75 shoulder nights. Low season modelled at zero.
Occupancy is an ASSUMPTION, not evidence - the weakest input, and it drives revenue
linearly. Bracketed by Nagano simple lodging at 14.2% in January and Niigata resort
hotels at 64.9%. Operating cost rates are industry placeholders; no Japanese operator
has quoted. Yield is on TOTAL PROJECT COST.

--------------------------------------------------------------------------------------------------------
CONSERVATIVE  (high-season occupancy 40%, shoulder 10%)
--------------------------------------------------------------------------------------------------------
Property                         Market           Cap   Gross A$      NOI A$      TPC A$    Yield    Lic
Ski-in Ski-out Chalet Tsugaike   Hakuba            16     57,898      12,518   1,190,932    1.05%       
Mont Cervin                      Myoko             22     55,504      11,773   1,648,409    0.71%       
Myoko Forest Lodge               Myoko             20     50,458       9,704   1,390,110    0.70%       
Kodachi Lodge & Cottage          Myoko             19     47,935       8,670   1,297,566    0.67%    YES
Kuma Lodge Madarao               Madarao           20     43,250       6,749   1,028,492    0.66%       
Alpen View Art Villa             Myoko             16     40,367       5,567     956,169    0.58%       
Madarao Tangram Ridge Runner     Madarao           16     34,600       3,202     692,704    0.46%       
Funky Monkey Lodge               Myoko             16     40,367       5,567   1,369,446    0.41%       
Kawamotoya Penthouse             Nozawa Onsen       8     17,300      -3,891   3,818,116   -0.10%       
Peaceful Family Misorano Retrea  Hakuba             6     21,712      -2,171   1,118,608   -0.19%       
Midori Cottage Misorano          Hakuba             6     21,712      -2,171     777,654   -0.28%       
Shiki at Tangram                 Madarao            8     17,300      -3,891   1,390,110   -0.28%       
SOTO House Myoko                 Myoko              8     20,183      -2,709     956,169   -0.28%       
Cubby House Myoko                Myoko              8     20,183      -2,709     770,194   -0.35%       
Yotei View Retreat               Kimobetsu/Rusu     6     14,150      -5,220   1,221,928   -0.43%       
Sweet Wasabi Chalet              Niseko Annupur     6     14,150      -5,220   1,087,612   -0.48%       
Moriyuki                         Furano             4     11,266      -6,402   1,221,928   -0.52%       
3-Bedroom Ski Chalet Naeba       Naeba              6     14,150      -5,220     925,173   -0.56%       
3 Bedroom House Miyanomori       Sapporo Miyano     6     14,150      -5,220     806,584   -0.65%       
Shiki at Tangram (3B)            Madarao            4      8,650      -7,437     976,832   -0.76%       
Gakuto Villas                    Hakuba             4     14,475      -5,108     581,347   -0.88%       
Address Nagasaka 2A              Nozawa Onsen       2      4,325      -9,211     542,891   -1.70%       

--------------------------------------------------------------------------------------------------------
BASE  (high-season occupancy 55%, shoulder 20%)
--------------------------------------------------------------------------------------------------------
Property                         Market           Cap   Gross A$      NOI A$      TPC A$    Yield    Lic
Ski-in Ski-out Chalet Tsugaike   Hakuba            16     85,450      23,281   1,075,198    2.17%       
Madarao Tangram Ridge Runner     Madarao           16     51,580       9,463     543,821    1.74%       
Kuma Lodge Madarao               Madarao           20     64,475      14,890     879,609    1.69%       
Alpen View Art Villa             Myoko             16     60,176      13,081     807,285    1.62%       
Myoko Forest Lodge               Myoko             20     75,220      19,413   1,241,227    1.56%       
Mont Cervin                      Myoko             22     82,742      22,578   1,499,525    1.51%       
Kodachi Lodge & Cottage          Myoko             19     71,459      17,830   1,203,012    1.48%    YES
Funky Monkey Lodge               Myoko             16     60,176      13,081   1,220,563    1.07%       
Midori Cottage Misorano          Hakuba             6     32,044       1,077     661,920    0.16%       
Peaceful Family Misorano Retrea  Hakuba             6     32,044       1,077   1,002,874    0.11%       
Cubby House Myoko                Myoko              8     30,088         418     621,311    0.07%       
SOTO House Myoko                 Myoko              8     30,088         418     807,285    0.05%       
Kawamotoya Penthouse             Nozawa Onsen       8     25,790      -1,391   3,669,233   -0.04%       
Shiki at Tangram                 Madarao            8     25,790      -1,391   1,241,227   -0.11%       
Yotei View Retreat               Kimobetsu/Rusu     6     20,958      -3,494   1,106,194   -0.32%       
Sweet Wasabi Chalet              Niseko Annupur     6     20,958      -3,494     971,879   -0.36%       
3-Bedroom Ski Chalet Naeba       Naeba              6     20,958      -3,494     776,290   -0.45%       
Moriyuki                         Furano             4     16,659      -5,303   1,106,194   -0.48%       
3 Bedroom House Miyanomori       Sapporo Miyano     6     20,958      -3,494     690,850   -0.51%       
Gakuto Villas                    Hakuba             4     21,362      -3,364     465,614   -0.72%       
Shiki at Tangram (3B)            Madarao            4     12,895      -6,818     827,949   -0.82%       
Address Nagasaka 2A              Nozawa Onsen       2      6,447      -9,532     394,008   -2.42%       

--------------------------------------------------------------------------------------------------------
STRONG  (high-season occupancy 70%, shoulder 30%)
--------------------------------------------------------------------------------------------------------
Property                         Market           Cap   Gross A$      NOI A$      TPC A$    Yield    Lic
Ski-in Ski-out Chalet Tsugaike   Hakuba            16    113,002      34,045   1,075,198    3.17%       
Madarao Tangram Ridge Runner     Madarao           16     68,559      15,724     543,821    2.89%       
Kuma Lodge Madarao               Madarao           20     85,699      23,032     879,609    2.62%       
Alpen View Art Villa             Myoko             16     79,986      20,596     807,285    2.55%       
Myoko Forest Lodge               Myoko             20     99,982      29,121   1,241,227    2.35%       
Kodachi Lodge & Cottage          Myoko             19     94,983      26,990   1,203,012    2.24%    YES
Mont Cervin                      Myoko             22    109,980      33,384   1,499,525    2.23%       
Funky Monkey Lodge               Myoko             16     79,986      20,596   1,220,563    1.69%       
Midori Cottage Misorano          Hakuba             6     42,376       4,325     661,920    0.65%       
Cubby House Myoko                Myoko              8     39,993       3,544     621,311    0.57%       
SOTO House Myoko                 Myoko              8     39,993       3,544     807,285    0.44%       
Peaceful Family Misorano Retrea  Hakuba             6     42,376       4,325   1,002,874    0.43%       
Shiki at Tangram                 Madarao            8     34,280       1,109   1,241,227    0.09%       
Kawamotoya Penthouse             Nozawa Onsen       8     34,280       1,109   3,669,233    0.03%       
Yotei View Retreat               Kimobetsu/Rusu     6     27,765      -1,768   1,106,194   -0.16%       
Sweet Wasabi Chalet              Niseko Annupur     6     27,765      -1,768     971,879   -0.18%       
3-Bedroom Ski Chalet Naeba       Naeba              6     27,765      -1,768     776,290   -0.23%       
3 Bedroom House Miyanomori       Sapporo Miyano     6     27,765      -1,768     690,850   -0.26%       
Gakuto Villas                    Hakuba             4     28,250      -1,619     465,614   -0.35%       
Moriyuki                         Furano             4     22,052      -4,204   1,106,194   -0.38%       
Shiki at Tangram (3B)            Madarao            4     17,140      -6,199     827,949   -0.75%       
Address Nagasaka 2A              Nozawa Onsen       2      8,570      -9,853     394,008   -2.50%       

INSUFFICIENT INPUTS - not modelled (29 properties):
  Myoko Ski Out Onsen Lodge          missing: capacity
  Wonderland Chalet                  missing: capacity
  Exclusive Seki Onsen development   missing: capacity
  Echizenya Myoko                    missing: capacity
  Charming Renovated Alpine Home     missing: capacity
  Villa El Cielo Myoko               missing: capacity
  Myoko Akakura Kogen Ski Lodge      missing: capacity
  SOTO Myoko (lodge and house, two   missing: capacity
  Melo Haus Myoko                    missing: capacity
  Lower St Moritz Land               missing: capacity
  Light Reserve Land                 missing: capacity
  Upper Misorano Villa               missing: capacity
  ... and 17 more

  These are NOT ranked. A property without capacity cannot be modelled, and
  substituting a guess would produce a number with no evidence behind it.

```

## Capacity sweep

```text
================================================================================================
GUEST-CAPACITY SWEEP  —  identical property, capacity varied, base-case occupancy
================================================================================================
Purchase price scales with capacity from the observed price-per-guest in the real
candidate set. Licensing steps up 2.5x at 16+ guests to proxy the sprinkler threshold,
which is UNRESOLVED and is the largest single unknown in this analysis.

------------------------------------------------------------------------------------------------
Hakuba   (rate 15,500 JPY/guest/night high season)
------------------------------------------------------------------------------------------------
Guests     Gross A$       NOI A$        TPC A$    Yield   NOI/guest A$  Fixed % rev
     6       32,044        5,379       444,206    1.21%            896        26.4%
     8       42,725       11,253       576,214    1.95%          1,407        19.8%
    10       53,406       17,128       708,223    2.42%          1,713        15.8%
    12       64,087       23,003       840,231    2.74%          1,917        13.2%
    16       85,450       34,752     1,117,597    3.11%          2,172         9.9%
    20      106,812       46,502     1,381,614    3.37%          2,325         7.9%
    24      128,175       58,251     1,645,631    3.54%          2,427         6.6%

------------------------------------------------------------------------------------------------
Myoko   (rate 10,500 JPY/guest/night high season)
------------------------------------------------------------------------------------------------
Guests     Gross A$       NOI A$        TPC A$    Yield   NOI/guest A$  Fixed % rev
     6       22,566          166       419,409    0.04%             28        37.5%
     8       30,088        4,303       543,152    0.79%            538        28.1%
    10       37,610        8,440       666,895    1.27%            844        22.5%
    12       45,132       12,577       790,638    1.59%          1,048        18.7%
    16       60,176       20,852     1,051,473    1.98%          1,303        14.0%
    20       75,220       29,126     1,298,959    2.24%          1,456        11.2%
    24       90,264       37,400     1,546,445    2.42%          1,558         9.4%

------------------------------------------------------------------------------------------------
Madarao   (rate 9,000 JPY/guest/night high season)
------------------------------------------------------------------------------------------------
Guests     Gross A$       NOI A$        TPC A$    Yield   NOI/guest A$  Fixed % rev
     6       19,342       -1,607       295,426   -0.54%           -268        43.7%
     8       25,790        1,939       377,841    0.51%            242        32.8%
    10       32,237        5,485       460,256    1.19%            549        26.2%
    12       38,685        9,031       542,672    1.66%            753        21.9%
    16       51,580       16,124       720,851    2.24%          1,008        16.4%
    20       64,475       23,216       885,681    2.62%          1,161        13.1%
    24       77,369       30,308     1,050,512    2.89%          1,263        10.9%

================================================================================================
BREAKEVEN CAPACITY (base case, NOI turns positive)
================================================================================================
  Hakuba           base case: 5 guests   conservative case: 6 guests
  Myoko            base case: 6 guests   conservative case: 8 guests
  Madarao          base case: 7 guests   conservative case: 10 guests
  Nozawa Onsen     base case: 7 guests   conservative case: 10 guests
  Kutchan/Niseko   base case: 4 guests   conservative case: 5 guests

```
