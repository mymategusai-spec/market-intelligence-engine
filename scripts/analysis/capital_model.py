#!/usr/bin/env python3
"""Capital requirement model — what a purchase actually costs to get operating.

Answers one of the brief's four core questions: *how much AUD capital would two
Australians realistically need?* Parameterised by purchase price rather than asserting
prices that have not been sourced.

Reports **total project cost**, never purchase price alone. Deliberately produces **no
revenue, NOI or yield** — nightly rates and occupancy have not been obtained, and
inventing them would produce exactly the false precision the brief warns against.

    python3 scripts/analysis/capital_model.py
    python3 scripts/analysis/capital_model.py --price-jpy 25000000 --scenario good_lodge_standard
    python3 scripts/analysis/capital_model.py --strategies

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

COSTS_PATH = os.path.join(REPO_ROOT, "data", "reference", "cost-assumptions.json")

#: Illustrative strategies per master prompt section 47. Purchase prices are ROUND
#: ILLUSTRATIVE FIGURES chosen to span the plausible range, not sourced valuations —
#: Phase 13 has not collected real listings yet.
STRATEGIES = [
    ("SHOESTRING", 8_000_000, "minimum_viable",
     "Lowest level at which the attempt is responsible. A cheap fixer-upper, minimum "
     "viable renovation, small guest capacity."),
    ("SENSIBLE", 25_000_000, "good_lodge_standard",
     "Something genuinely commercially viable without constantly fighting limitations."),
    ("STRONG", 60_000_000, "premium_repositioning",
     "A stronger asset with better revenue and resale prospects."),
]


def build_stack(price_jpy, scenario, costs, use_high=False):
    """Assemble the capital stack in JPY. `use_high` selects the top of every range."""
    pick = (lambda d: d["high"]) if use_high else (lambda d: d["low"])

    acq = costs["acquisition_costs"]
    reno_band = costs["renovation_scenarios_jpy"][scenario]
    other = costs["other_capital_jpy"]

    commission = price_jpy * acq["agent_commission_percent"]["value"] / 100.0
    registration = price_jpy * acq["registration_transfer_tax_percent"]["value"] / 100.0
    acquisition_tax = price_jpy * acq["acquisition_tax_effective_percent"]["value"] / 100.0
    legal = pick(acq["legal_scrivener_jpy"])
    diligence = pick(acq["due_diligence_jpy"])

    renovation = pick(reno_band)
    furnishing = pick(other["furnishing"])
    licensing = pick(other["licensing_compliance"])

    contingency = renovation * costs["contingency"]["renovation_contingency_percent"]["value"] / 100.0

    # Working capital: six months of operating cost, itself unmeasured. Proxied at 1.5%
    # of total build cost per month — a placeholder, flagged in the output.
    build_total = price_jpy + renovation + furnishing + licensing
    working_capital = build_total * 0.015 * other["working_capital_months"]["value"]

    return CapitalStack(
        purchase_price=Money.of(price_jpy, "JPY"),
        acquisition_costs=Money.of(commission, "JPY"),
        taxes=Money.of(registration + acquisition_tax, "JPY"),
        legal=Money.of(legal, "JPY"),
        due_diligence=Money.of(diligence, "JPY"),
        renovation=Money.of(renovation, "JPY"),
        furnishing=Money.of(furnishing, "JPY"),
        licensing_compliance=Money.of(licensing, "JPY"),
        working_capital=Money.of(working_capital, "JPY"),
        contingency=Money.of(contingency, "JPY"),
    )


def aud(amount_jpy, fx):
    return amount_jpy / fx.rate


def report(label, price_jpy, scenario, costs, fx, description=None):
    low = build_stack(price_jpy, scenario, costs, use_high=False)
    high = build_stack(price_jpy, scenario, costs, use_high=True)

    print("\n" + "=" * 78)
    print("%s — purchase ¥%s, %s" % (label, "{:,.0f}".format(price_jpy), scenario))
    if description:
        print("  %s" % description)
    print("=" * 78)

    rows = [
        ("Purchase price", low.purchase_price, high.purchase_price),
        ("Agent commission", low.acquisition_costs, high.acquisition_costs),
        ("Registration + acquisition tax", low.taxes, high.taxes),
        ("Legal / scrivener", low.legal, high.legal),
        ("Due diligence / inspection", low.due_diligence, high.due_diligence),
        ("Renovation", low.renovation, high.renovation),
        ("Furnishing", low.furnishing, high.furnishing),
        ("Licensing / compliance", low.licensing_compliance, high.licensing_compliance),
        ("Working capital (6 months)", low.working_capital, high.working_capital),
        ("Contingency (30% of reno)", low.contingency, high.contingency),
    ]

    print("\n%-32s %18s %18s" % ("", "LOW (A$)", "HIGH (A$)"))
    print("-" * 78)
    for name, lo, hi in rows:
        print(
            "%-32s %18s %18s"
            % (name, "{:,.0f}".format(aud(lo.amount, fx)), "{:,.0f}".format(aud(hi.amount, fx)))
        )

    total_low = low.total_project_cost().amount
    total_high = high.total_project_cost().amount
    print("-" * 78)
    print(
        "%-32s %18s %18s"
        % ("TOTAL PROJECT COST", "{:,.0f}".format(aud(total_low, fx)), "{:,.0f}".format(aud(total_high, fx)))
    )
    print(
        "%-32s %18s %18s"
        % ("  per owner at 50/50", "{:,.0f}".format(aud(total_low, fx) / 2), "{:,.0f}".format(aud(total_high, fx) / 2))
    )
    print()
    print(
        "%-32s %18s %18s"
        % ("Purchase price alone", "{:,.0f}".format(aud(price_jpy, fx)), "{:,.0f}".format(aud(price_jpy, fx)))
    )
    multiple_low = total_low / price_jpy
    multiple_high = total_high / price_jpy
    print(
        "%-32s %17.2fx %17.2fx"
        % ("Total cost / purchase price", multiple_low, multiple_high)
    )
    print(
        "\n  Purchase price understates the real investment by %.0f%%-%.0f%%."
        % ((multiple_low - 1) * 100, (multiple_high - 1) * 100)
    )
    return total_low, total_high


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--price-jpy", type=float, default=None)
    parser.add_argument("--scenario", default="minimum_viable",
                        choices=["minimum_viable", "good_lodge_standard", "premium_repositioning"])
    parser.add_argument("--strategies", action="store_true",
                        help="Run the shoestring / sensible / strong strategies")
    args = parser.parse_args()

    costs = load_json(COSTS_PATH)
    fx_config = costs["fx"]
    fx = FxConversion(
        from_currency="AUD",
        to_currency="JPY",
        rate=fx_config["rate_jpy_per_aud"],
        rate_date=date.fromisoformat(fx_config["rate_date"]),
    )

    print("=" * 78)
    print("CAPITAL REQUIREMENT MODEL — ILLUSTRATIVE, NOT A VALUATION")
    print("=" * 78)
    print("FX          : %.2f JPY/AUD as at %s (recent range ~110-114)"
          % (fx.rate, fx.rate_date.isoformat()))
    print("Cost inputs : data/reference/cost-assumptions.json")
    print()
    print("No revenue, NOI or yield is produced. Nightly rates and occupancy have not")
    print("been obtained, and inventing them would be false precision.")
    print()
    print("Purchase prices below are ROUND ILLUSTRATIVE FIGURES spanning a plausible")
    print("range. Phase 13 has not yet collected real listings.")

    if args.strategies or args.price_jpy is None:
        for label, price, scenario, description in STRATEGIES:
            report(label, price, scenario, costs, fx, description)
    else:
        report("CUSTOM", args.price_jpy, args.scenario, costs, fx)

    print("\n" + "=" * 78)
    print("HEALTH WARNINGS")
    print("=" * 78)
    print("""
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
""")


if __name__ == "__main__":
    main()
