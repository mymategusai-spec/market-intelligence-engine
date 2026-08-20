#!/usr/bin/env python3
"""Score and rank candidate markets from committed evidence and committed weights.

Demonstrates the whole engine path end to end: config in, evidence in, explained ranking
out. Run it, change a weight in config, run it again — the ranking moves. That is the
point of the dashboard, verified here without one.

    python3 scripts/analysis/screen_markets.py
    python3 scripts/analysis/screen_markets.py --weight-set lifestyle
    python3 scripts/analysis/screen_markets.py --all-profiles --explain

Standard library only. No install step.
"""

from __future__ import annotations

import argparse
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from core.config import load_json, load_weight_sets  # noqa: E402
from core.models.common import Confidence  # noqa: E402
from core.scoring.engine import ScoreComponent, rank, score  # noqa: E402

WEIGHTS_PATH = os.path.join(REPO_ROOT, "config", "domains", "japan_ski_property", "weights.json")
COMPONENTS_PATH = os.path.join(
    REPO_ROOT, "config", "domains", "japan_ski_property", "scoring_components.json"
)
EVIDENCE_PATH = os.path.join(
    REPO_ROOT, "domains", "japan_ski_property", "research", "market-screening-scores.json"
)


def load_markets():
    evidence = load_json(EVIDENCE_PATH)
    definitions = load_json(COMPONENTS_PATH)["components"]

    markets = []
    for entry in evidence["markets"]:
        components = []
        for raw in entry["components"]:
            key = raw["key"]
            if key not in definitions:
                raise ValueError(
                    "Market %s scores unknown component %r — add it to "
                    "scoring_components.json or fix the typo." % (entry["market_id"], key)
                )
            components.append(
                ScoreComponent(
                    component_key=key,
                    label=definitions[key]["label"],
                    value=float(raw["value"]),
                    confidence=Confidence(raw["confidence"]),
                    rationale=raw["rationale"],
                    is_estimate=True,
                )
            )
        markets.append((entry["market_id"], entry["name"], components))
    return evidence, markets


def weight_coverage(result, weight_set):
    """Fraction of total available weight that was actually scored.

    Necessary because the score is normalised over the weights applied. Without this, a
    market scored only on its strong dimensions is flattered against one scored on
    everything — it dodges the penalty its unscored dimensions would have carried. A
    ranking that ignores coverage rewards ignorance.
    """
    total = sum(weight_set.weights.values())
    if total <= 0:
        return 0.0
    scored = sum(
        weight_set.weight_for(row["component_key"]) for row in result.components
    )
    return scored / total


def run(weight_set, markets, explain=False, min_coverage=0.0, min_dimensions=0):
    """Rank markets, withholding any whose evidence is too thin to compare honestly.

    Two independent guards, because either alone is gameable. Weight coverage stops a
    market being carried by one heavily-weighted dimension; the dimension count stops a
    market qualifying on a handful of its strongest scores. A market must clear both.
    """
    results = [score(name, components, weight_set) for _mid, name, components in markets]
    coverage = {r.subject_id: weight_coverage(r, weight_set) for r in results}
    dims = {r.subject_id: len(r.components) for r in results}

    def qualifies(r):
        return coverage[r.subject_id] >= min_coverage and dims[r.subject_id] >= min_dimensions

    rankable = [r for r in results if qualifies(r)]
    withheld = [r for r in results if not qualifies(r)]
    ranked = rank(rankable)

    print("\n%s" % ("=" * 78))
    print("WEIGHT SET: %s" % weight_set.weight_set_id)
    if weight_set.description:
        print("  %s" % weight_set.description)
    print("=" * 78)

    print("\n%-4s %-22s %-8s %-12s %-10s %s"
          % ("#", "Market", "Score", "Confidence", "Coverage", "Unscored"))
    print("-" * 78)
    for position, result in enumerate(ranked, start=1):
        print(
            "%-4d %-22s %-8.2f %-12s %-10s %d of 20"
            % (
                position,
                result.subject_id,
                result.total_score,
                result.overall_confidence.value,
                "%.0f%%" % (coverage[result.subject_id] * 100),
                len(result.components_missing),
            )
        )

    if withheld:
        print("\n  INSUFFICIENT DATA FOR RANKING (needs >=%.0f%% coverage and >=%d dimensions):"
              % (min_coverage * 100, min_dimensions))
        for result in withheld:
            print(
                "    %-24s coverage %.0f%%, %d dimensions scored"
                % (result.subject_id, coverage[result.subject_id] * 100, dims[result.subject_id])
            )
        print("    Not ranked. Too little is known to compare these with the others,")
        print("    and ranking them on their strongest dimensions alone would reward ignorance.")

    if explain:
        for result in ranked:
            print("\n" + result.explain())

    return ranked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weight-set", default=None, help="Named weight set to apply")
    parser.add_argument("--all-profiles", action="store_true", help="Run every weight set")
    parser.add_argument("--explain", action="store_true", help="Show component breakdowns")
    parser.add_argument(
        "--min-coverage",
        type=float,
        default=0.40,
        help="Minimum fraction of total weight that must be scored for a market to be "
             "ranked at all (default 0.40). Below this, too little is known.",
    )
    parser.add_argument(
        "--min-dimensions",
        type=int,
        default=10,
        help="Minimum number of scored dimensions for a market to be ranked (default 10 "
             "of 20). Stops a market qualifying on a handful of its strongest scores.",
    )
    args = parser.parse_args()

    evidence, markets = load_markets()
    weight_sets = load_weight_sets(WEIGHTS_PATH)

    print("=" * 78)
    print("PROVISIONAL MARKET SCREENING — NOT A RECOMMENDATION")
    print("=" * 78)
    print("Evidence as of : %s" % evidence["as_of"])
    print("Status         : %s" % evidence["status"])
    print("Dimensions     : %d defined in the scorecard" % evidence["scored_dimensions_available"])
    print()
    print("Unscored dimensions are reported, never substituted with a midpoint - that")
    print("would flatter exactly the markets least is known about. Absence of negative")
    print("evidence is never scored as a positive.")
    print()
    print("Markets are ranked only with >=%.0f%% weight coverage AND >=%d of 20 dimensions."
          % (args.min_coverage * 100, args.min_dimensions))
    print("Below either threshold: INSUFFICIENT DATA FOR RANKING.")

    if args.all_profiles:
        selected = list(weight_sets.values())
    elif args.weight_set:
        if args.weight_set not in weight_sets:
            parser.error(
                "Unknown weight set %r. Available: %s"
                % (args.weight_set, ", ".join(sorted(weight_sets)))
            )
        selected = [weight_sets[args.weight_set]]
    else:
        selected = [weight_sets[load_json(WEIGHTS_PATH)["default_weight_set"]]]

    orderings = {}
    for weight_set in selected:
        ranked = run(
            weight_set, markets, explain=args.explain,
            min_coverage=args.min_coverage, min_dimensions=args.min_dimensions,
        )
        orderings[weight_set.weight_set_id] = [r.subject_id for r in ranked]

    if len(orderings) > 1:
        print("\n%s" % ("=" * 78))
        print("SENSITIVITY — does re-weighting actually change the answer?")
        print("=" * 78)
        for name, order in orderings.items():
            print("  %-18s %s" % (name, " > ".join(order)))
        distinct = len({tuple(o) for o in orderings.values()})
        print(
            "\n  %d distinct ordering(s) across %d profiles."
            % (distinct, len(orderings))
        )
        if distinct == 1:
            print("  Identical under every profile — the evidence, not the weights, is driving this.")
        else:
            print("  Ranking is preference-dependent. No single ordering is 'the' answer.")

    print("\nProvisional. See domains/japan_ski_property/research/ for the underlying evidence.\n")


if __name__ == "__main__":
    main()
