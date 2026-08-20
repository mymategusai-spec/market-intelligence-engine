#!/usr/bin/env python3
"""Per-property total project cost under three renovation scenarios.

The brief's headline metric: TOTAL PROJECT COST AUD, never asking price. Properties are
ordered by total project cost, not by what the vendor is asking.

    python3 scripts/analysis/property_costs.py
    python3 scripts/analysis/property_costs.py --all
    python3 scripts/analysis/property_costs.py --scenario good_lodge_standard

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
from core.financial.model import CapitalStack  # noqa: E402
from core.models.common import FxConversion, Money  # noqa: E402

COSTS = os.path.join(REPO_ROOT, "data", "reference", "cost-assumptions.json")
PROPS = os.path.join(REPO_ROOT, "data", "property-listings", "candidate-properties-2026-08-20.json")

SCENARIOS = ["minimum_viable", "good_lodge_standard", "premium_repositioning"]

#: Markets in heavy-snow regions where roof/exterior work runs 1.5-2.0x plains rates.
SNOW_COUNTRY = {"Myoko", "Yuzawa", "Nozawa Onsen", "Madarao", "Naeba", "Kijimadaira", "Iiyama"}


def stack_for(price_jpy, scenario, costs, high, snow_country):
    pick = (lambda d: d["high"]) if high else (lambda d: d["low"])
    acq, other = costs["acquisition_costs"], costs["other_capital_jpy"]

    reno = pick(costs["renovation_scenarios_jpy"][scenario])
    # Snow-country premium applies to the roof/exterior share of a renovation, taken here
    # as roughly a third of the job. Multiplier 1.5 (low) to 2.0 (high) on that share.
    if snow_country:
        mult = 2.0 if high else 1.5
        reno = reno * (2 / 3) + reno * (1 / 3) * mult

    furnishing = pick(other["furnishing"])
    licensing = pick(other["licensing_compliance"])
    build = price_jpy + reno + furnishing + licensing

    return CapitalStack(
        purchase_price=Money.of(price_jpy, "JPY"),
        acquisition_costs=Money.of(price_jpy * acq["agent_commission_percent"]["value"] / 100, "JPY"),
        taxes=Money.of(price_jpy * (acq["registration_transfer_tax_percent"]["value"]
                                    + acq["acquisition_tax_effective_percent"]["value"]) / 100, "JPY"),
        legal=Money.of(pick(acq["legal_scrivener_jpy"]), "JPY"),
        due_diligence=Money.of(pick(acq["due_diligence_jpy"]), "JPY"),
        renovation=Money.of(reno, "JPY"),
        furnishing=Money.of(furnishing, "JPY"),
        licensing_compliance=Money.of(licensing, "JPY"),
        working_capital=Money.of(build * 0.015 * other["working_capital_months"]["value"], "JPY"),
        contingency=Money.of(reno * costs["contingency"]["renovation_contingency_percent"]["value"] / 100, "JPY"),
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scenario", default="minimum_viable", choices=SCENARIOS)
    ap.add_argument("--all", action="store_true", help="All priced candidates, not just HIGH priority")
    ap.add_argument("--max-aud", type=float, default=None, help="Filter on total project cost")
    args = ap.parse_args()

    costs = load_json(COSTS)
    fx = FxConversion("AUD", "JPY", costs["fx"]["rate_jpy_per_aud"],
                      date.fromisoformat(costs["fx"]["rate_date"]))
    props = load_json(PROPS)["properties"]

    selected = [p for p in props if p.get("asking_price_jpy")]
    if not args.all:
        selected = [p for p in selected if p.get("priority") == "HIGH"]
    if not selected:
        print("No properties matched.")
        return

    print("=" * 100)
    print("TOTAL PROJECT COST BY PROPERTY  —  scenario: %s" % args.scenario)
    print("=" * 100)
    print("FX %.2f JPY/AUD @ %s. Ranges are low/high across every cost input." % (fx.rate, fx.rate_date))
    print("Snow-country premium (1.5-2.0x on roof/exterior share) applied to: %s"
          % ", ".join(sorted(SNOW_COUNTRY)))
    print("Renovation scenarios are ESTIMATE-class. No contractor has quoted any property.\n")

    rows = []
    for p in selected:
        snow = p.get("market") in SNOW_COUNTRY
        lo = stack_for(p["asking_price_jpy"], args.scenario, costs, False, snow).total_project_cost().amount
        hi = stack_for(p["asking_price_jpy"], args.scenario, costs, True, snow).total_project_cost().amount
        rows.append((p, lo / fx.rate, hi / fx.rate, p["asking_price_jpy"] / fx.rate, snow))

    rows.sort(key=lambda r: r[1])
    if args.max_aud:
        rows = [r for r in rows if r[1] <= args.max_aud]

    print("%-34s %-16s %11s %11s %11s %6s" % ("Property", "Market", "Ask A$", "TPC low", "TPC high", "Mult"))
    print("-" * 100)
    for p, lo, hi, ask, snow in rows:
        name = (p.get("name") or p["property_id"])[:33]
        print("%-34s %-16s %11s %11s %11s %5.1fx%s"
              % (name, (p.get("market") or "")[:15], "{:,.0f}".format(ask),
                 "{:,.0f}".format(lo), "{:,.0f}".format(hi), lo / ask, "*" if snow else ""))
    print("-" * 100)
    print("* snow-country premium applied")
    print("\nPer owner at 50/50: halve the TPC columns.")
    print("Reminder: no revenue is modelled, so none of these can yet be judged as good or bad value.\n")


if __name__ == "__main__":
    main()
