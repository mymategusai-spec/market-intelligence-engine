#!/usr/bin/env python3
"""Property-level financial models: conservative / base / strong.

Produces gross revenue, NOI and yield on TOTAL PROJECT COST for shortlisted properties.

Two rules enforced in code rather than trusted to the analyst:

1. A property is NOT financially ranked unless it has the inputs the model needs
   (capacity and price). Missing inputs produce ``INSUFFICIENT INPUTS``, not a number.
2. Yield is reported against total project cost, never purchase price alone.

    python3 scripts/analysis/property_financials.py
    python3 scripts/analysis/property_financials.py --scenario strong --explain

Standard library only.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from core.config import load_json  # noqa: E402
from core.financial.model import CapitalStack, OperatingCosts, OwnerUse, compute  # noqa: E402
from core.models.common import Confidence, FxConversion, Money  # noqa: E402

COSTS = load_json(os.path.join(REPO_ROOT, "data", "reference", "cost-assumptions.json"))
OPS = load_json(os.path.join(REPO_ROOT, "data", "reference", "operating-assumptions.json"))
PROPS = load_json(os.path.join(REPO_ROOT, "data", "property-listings",
                               "candidate-properties-2026-08-20.json"))["properties"]

SNOW_COUNTRY = {"Myoko", "Yuzawa", "Nozawa Onsen", "Madarao", "Naeba", "Kijimadaira", "Iiyama"}
FX = FxConversion("AUD", "JPY", COSTS["fx"]["rate_jpy_per_aud"],
                  date.fromisoformat(COSTS["fx"]["rate_date"]))


def rates_for(market):
    table = OPS["rate_per_guest_night_jpy"]
    return table.get(market, table["default"])


def capital_for(prop, scenario_reno, high):
    """Capital stack. Licensed properties skip most of the compliance line."""
    pick = (lambda d: d["high"]) if high else (lambda d: d["low"])
    acq, other = COSTS["acquisition_costs"], COSTS["other_capital_jpy"]
    price = prop["asking_price_jpy"]

    reno = pick(COSTS["renovation_scenarios_jpy"][scenario_reno])
    if prop.get("market") in SNOW_COUNTRY:
        mult = 2.0 if high else 1.5
        reno = reno * (2 / 3) + reno * (1 / 3) * mult

    licensed = prop.get("licence_status") in ("hotel_licence", "ryokan_licence", "simple_lodging_licence")
    licensing = pick(other["licensing_compliance"]) * (0.25 if licensed else 1.0)
    if licensed:
        reno *= 0.6  # already operating; much of the conversion work is done

    furnishing = pick(other["furnishing"])
    build = price + reno + furnishing + licensing
    return CapitalStack(
        purchase_price=Money.of(price, "JPY"),
        acquisition_costs=Money.of(price * acq["agent_commission_percent"]["value"] / 100, "JPY"),
        taxes=Money.of(price * (acq["registration_transfer_tax_percent"]["value"]
                                + acq["acquisition_tax_effective_percent"]["value"]) / 100, "JPY"),
        legal=Money.of(pick(acq["legal_scrivener_jpy"]), "JPY"),
        due_diligence=Money.of(pick(acq["due_diligence_jpy"]), "JPY"),
        renovation=Money.of(reno, "JPY"),
        furnishing=Money.of(furnishing, "JPY"),
        licensing_compliance=Money.of(licensing, "JPY"),
        working_capital=Money.of(build * 0.015 * other["working_capital_months"]["value"], "JPY"),
        contingency=Money.of(reno * COSTS["contingency"]["renovation_contingency_percent"]["value"] / 100, "JPY"),
    ), licensed


def model(prop, scenario, reno_scenario):
    capacity = prop.get("practical_guest_capacity")
    if not capacity:
        beds = prop.get("bedrooms")
        capacity = beds * 2 if beds else None
    if not capacity or not prop.get("asking_price_jpy"):
        return None

    occ = OPS["occupancy_scenarios"][scenario]
    season = OPS["season_structure"]
    rates = rates_for(prop.get("market"))
    ops = OPS["operating_cost_rates"]

    high_nights = season["high_season"]["nights"] * occ["high_season"]
    shoulder_nights = season["shoulder_season"]["nights"] * occ["shoulder"]

    gross = (high_nights * capacity * rates["high"]) + (shoulder_nights * capacity * rates["shoulder"])
    occupied_nights = high_nights + shoulder_nights

    changeovers = occupied_nights / ops["assumed_average_stay_nights"]
    op_costs = OperatingCosts.from_breakdown(
        "JPY",
        management=Money.of(gross * ops["management_percent_of_gross"] / 100, "JPY"),
        platform_fees=Money.of(gross * ops["platform_commission_percent_of_gross"] / 100, "JPY"),
        cleaning=Money.of(changeovers * ops["cleaning_per_changeover_jpy"], "JPY"),
        utilities=Money.of(occupied_nights * ops["utilities_heating_per_occupied_night_jpy"], "JPY"),
        insurance=Money.of(ops["insurance_annual_jpy"], "JPY"),
        maintenance=Money.of(gross * ops["maintenance_percent_of_gross"] / 100, "JPY"),
        capex_reserve=Money.of(gross * ops["capex_reserve_percent_of_gross"] / 100, "JPY"),
        other=Money.of(ops["snow_clearing_annual_jpy"] + ops["fixed_admin_annual_jpy"], "JPY"),
    )

    has_own_quarters = bool(prop.get("has_owner_quarters") or prop.get("separate_buildings"))
    owner_weeks = OPS["owner_use"]["weeks_per_year"]
    foregone = owner_weeks * 7 * capacity * rates["high"] * occ["high_season"]
    owner_use = OwnerUse(weeks_per_year=owner_weeks, season="high",
                         revenue_foregone=Money.of(foregone, "JPY"),
                         offset_by_separate_quarters=has_own_quarters)

    high_cost = scenario == "conservative"
    capital, licensed = capital_for(prop, reno_scenario, high=high_cost)
    result = compute(capital, Money.of(gross, "JPY"), op_costs, owner_use,
                     input_confidence=[Confidence.LOW])
    return {"result": result, "capacity": capacity, "licensed": licensed,
            "occupied_nights": occupied_nights, "capital": capital}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scenario", default=None, choices=["conservative", "base", "strong"])
    ap.add_argument("--reno", default="minimum_viable",
                    choices=["minimum_viable", "good_lodge_standard", "premium_repositioning"])
    ap.add_argument("--explain", action="store_true")
    args = ap.parse_args()

    scenarios = [args.scenario] if args.scenario else ["conservative", "base", "strong"]
    candidates = [p for p in PROPS if p.get("asking_price_jpy")
                  and (p.get("practical_guest_capacity") or p.get("bedrooms"))]
    skipped = [p for p in PROPS if p not in candidates]

    print("=" * 104)
    print("PROPERTY-LEVEL FINANCIAL MODELS  —  renovation scenario: %s" % args.reno)
    print("=" * 104)
    print("Season: %d high-season nights (%s), %d shoulder nights. Low season modelled at zero."
          % (OPS["season_structure"]["high_season"]["nights"],
             OPS["season_structure"]["high_season"]["dates"],
             OPS["season_structure"]["shoulder_season"]["nights"]))
    print("Occupancy is an ASSUMPTION, not evidence - the weakest input, and it drives revenue")
    print("linearly. Bracketed by Nagano simple lodging at 14.2% in January and Niigata resort")
    print("hotels at 64.9%. Operating cost rates are industry placeholders; no Japanese operator")
    print("has quoted. Yield is on TOTAL PROJECT COST.\n")

    for scenario in scenarios:
        occ = OPS["occupancy_scenarios"][scenario]
        print("-" * 104)
        print("%s  (high-season occupancy %.0f%%, shoulder %.0f%%)"
              % (scenario.upper(), occ["high_season"] * 100, occ["shoulder"] * 100))
        print("-" * 104)
        print("%-32s %-15s %4s %10s %11s %11s %8s %6s"
              % ("Property", "Market", "Cap", "Gross A$", "NOI A$", "TPC A$", "Yield", "Lic"))
        rows = []
        for prop in candidates:
            out = model(prop, scenario, args.reno)
            if not out:
                continue
            r = out["result"]
            rows.append((prop, out, r.yield_on_total_project_cost_percent or -99))
        rows.sort(key=lambda x: -x[2])
        for prop, out, y in rows:
            r = out["result"]
            print("%-32s %-15s %4d %10s %11s %11s %7.2f%% %6s"
                  % ((prop.get("name") or prop["property_id"])[:31],
                     (prop.get("market") or "")[:14], out["capacity"],
                     "{:,.0f}".format(r.gross_revenue.amount / FX.rate),
                     "{:,.0f}".format(r.noi.amount / FX.rate),
                     "{:,.0f}".format(r.total_project_cost.amount / FX.rate),
                     y, "YES" if out["licensed"] else ""))
        if args.explain and rows:
            print("\n  Detail for top-ranked property:")
            for line in rows[0][1]["result"].summary().splitlines():
                print("    " + line)
        print()

    if skipped:
        print("INSUFFICIENT INPUTS - not modelled (%d properties):" % len(skipped))
        for prop in skipped[:12]:
            missing = []
            if not prop.get("asking_price_jpy"):
                missing.append("price")
            if not (prop.get("practical_guest_capacity") or prop.get("bedrooms")):
                missing.append("capacity")
            print("  %-34s missing: %s" % ((prop.get("name") or prop["property_id"])[:33],
                                           ", ".join(missing)))
        if len(skipped) > 12:
            print("  ... and %d more" % (len(skipped) - 12))
        print("\n  These are NOT ranked. A property without capacity cannot be modelled, and")
        print("  substituting a guess would produce a number with no evidence behind it.\n")


if __name__ == "__main__":
    main()
