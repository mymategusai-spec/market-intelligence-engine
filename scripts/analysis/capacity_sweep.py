#!/usr/bin/env python3
"""Guest-capacity optimisation: hold everything constant, vary capacity.

Answers the brief's question - is the best economic format 6, 8, 10, 12, 16 or 20+ guests? -
by modelling an identical hypothetical property at each capacity in each market.

Purchase price is scaled with capacity from the observed relationship in the real
candidate set, so bigger properties cost more rather than being free upside.

    python3 scripts/analysis/capacity_sweep.py
"""

from __future__ import annotations

import os
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from core.config import load_json  # noqa: E402

COSTS = load_json(os.path.join(REPO_ROOT, "data", "reference", "cost-assumptions.json"))
OPS = load_json(os.path.join(REPO_ROOT, "data", "reference", "operating-assumptions.json"))
FX = COSTS["fx"]["rate_jpy_per_aud"]

CAPACITIES = [6, 8, 10, 12, 16, 20, 24]

#: Purchase price per guest, from the real candidate set. Median of asking price divided by
#: capacity across the priced, capacity-known properties in each market.
PRICE_PER_GUEST_JPY = {"Hakuba": 5_900_000, "Myoko": 5_500_000, "Madarao": 3_500_000,
                       "Nozawa Onsen": 5_000_000, "Kutchan/Niseko": 11_000_000}


def model(market, capacity, scenario):
    occ = OPS["occupancy_scenarios"][scenario]
    season = OPS["season_structure"]
    rates = OPS["rate_per_guest_night_jpy"].get(market, OPS["rate_per_guest_night_jpy"]["default"])
    ops = OPS["operating_cost_rates"]

    high_nights = season["high_season"]["nights"] * occ["high_season"]
    shoulder_nights = season["shoulder_season"]["nights"] * occ["shoulder"]
    gross = high_nights * capacity * rates["high"] + shoulder_nights * capacity * rates["shoulder"]
    occupied = high_nights + shoulder_nights

    owner_foregone = OPS["owner_use"]["weeks_per_year"] * 7 * capacity * rates["high"] * occ["high_season"]
    net_revenue = gross - owner_foregone

    variable = (net_revenue * (ops["management_percent_of_gross"]
                               + ops["platform_commission_percent_of_gross"]
                               + ops["maintenance_percent_of_gross"]
                               + ops["capex_reserve_percent_of_gross"]) / 100
                + occupied / ops["assumed_average_stay_nights"] * ops["cleaning_per_changeover_jpy"]
                + occupied * ops["utilities_heating_per_occupied_night_jpy"])
    fixed = ops["insurance_annual_jpy"] + ops["snow_clearing_annual_jpy"] + ops["fixed_admin_annual_jpy"]
    noi = net_revenue - variable - fixed

    price = PRICE_PER_GUEST_JPY.get(market, 5_000_000) * capacity
    reno = COSTS["renovation_scenarios_jpy"]["minimum_viable"]["low"] * (1 + (capacity - 8) * 0.06)
    furnishing = COSTS["other_capital_jpy"]["furnishing"]["low"] * (1 + (capacity - 8) * 0.08)
    licensing = COSTS["other_capital_jpy"]["licensing_compliance"]["low"] * (1.0 if capacity < 16 else 2.5)
    acq = price * 0.071
    tpc = price + acq + reno + furnishing + licensing + reno * 0.4 + (price + reno) * 0.09
    return {"gross": net_revenue, "noi": noi, "tpc": tpc,
            "yield": noi / tpc * 100 if tpc else 0,
            "noi_per_guest": noi / capacity, "fixed_share": fixed / net_revenue * 100 if net_revenue else 0}


def main():
    print("=" * 96)
    print("GUEST-CAPACITY SWEEP  —  identical property, capacity varied, base-case occupancy")
    print("=" * 96)
    print("Purchase price scales with capacity from the observed price-per-guest in the real")
    print("candidate set. Licensing steps up 2.5x at 16+ guests to proxy the sprinkler threshold,")
    print("which is UNRESOLVED and is the largest single unknown in this analysis.\n")

    for market in ["Hakuba", "Myoko", "Madarao"]:
        print("-" * 96)
        print("%s   (rate %s JPY/guest/night high season)"
              % (market, "{:,}".format(OPS["rate_per_guest_night_jpy"][market]["high"])))
        print("-" * 96)
        print("%6s %12s %12s %13s %8s %14s %12s"
              % ("Guests", "Gross A$", "NOI A$", "TPC A$", "Yield", "NOI/guest A$", "Fixed % rev"))
        for cap in CAPACITIES:
            m = model(market, cap, "base")
            print("%6d %12s %12s %13s %7.2f%% %14s %11.1f%%"
                  % (cap, "{:,.0f}".format(m["gross"] / FX), "{:,.0f}".format(m["noi"] / FX),
                     "{:,.0f}".format(m["tpc"] / FX), m["yield"],
                     "{:,.0f}".format(m["noi_per_guest"] / FX), m["fixed_share"]))
        print()

    print("=" * 96)
    print("BREAKEVEN CAPACITY (base case, NOI turns positive)")
    print("=" * 96)
    for market in ["Hakuba", "Myoko", "Madarao", "Nozawa Onsen", "Kutchan/Niseko"]:
        be = next((c for c in range(2, 40) if model(market, c, "base")["noi"] > 0), None)
        be_cons = next((c for c in range(2, 40) if model(market, c, "conservative")["noi"] > 0), None)
        print("  %-16s base case: %s guests   conservative case: %s guests"
              % (market, be or ">40", be_cons or ">40"))
    print()


if __name__ == "__main__":
    main()
