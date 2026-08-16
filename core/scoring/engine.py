"""Weighted scoring.

Scoring must be transparent and reproducible: the same committed data and the same
committed weights must always produce the same ranking, and every number must be
explainable. Weights come from config, never from code — subjective preferences are the
owners' to set, not the engine's to bake in.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence

from core.models.common import Confidence, weakest


@dataclass(frozen=True)
class ScoreComponent:
    """One scored dimension, with the reasoning that produced it.

    ``rationale`` is required. A score without one is an opinion in numeric costume, and
    the whole point of this engine is that conclusions can be interrogated.
    """

    component_key: str
    label: str
    value: float
    confidence: Confidence
    rationale: str
    evidence_observation_ids: Sequence[str] = ()
    evidence_indicator_ids: Sequence[str] = ()
    is_estimate: bool = False

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 10.0:
            raise ValueError(
                "Component %s scored %s; scores are 0-10" % (self.component_key, self.value)
            )
        if not self.rationale.strip():
            raise ValueError("Component %s requires a rationale" % self.component_key)


@dataclass(frozen=True)
class WeightSet:
    """A named set of weights, loaded from config.

    Identified and versioned because rankings are only comparable within the same weight
    set. Comparing a score produced under 'lifestyle' weights with one produced under
    'pure investment' weights is meaningless.
    """

    weight_set_id: str
    weights: Dict[str, float]
    version: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.weights:
            raise ValueError("Weight set %s is empty" % self.weight_set_id)
        for key, weight in self.weights.items():
            if weight < 0:
                raise ValueError("Negative weight for %s in %s" % (key, self.weight_set_id))
        if sum(self.weights.values()) <= 0:
            raise ValueError("Weight set %s sums to zero" % self.weight_set_id)

    def weight_for(self, component_key: str) -> float:
        return self.weights.get(component_key, 0.0)


@dataclass
class ScoreResult:
    subject_id: str
    weight_set_id: str
    total_score: float
    overall_confidence: Confidence
    components: List[Dict[str, object]] = field(default_factory=list)
    components_missing: List[str] = field(default_factory=list)
    disqualified: bool = False
    disqualification_reason: Optional[str] = None

    def explain(self) -> str:
        """Human-readable breakdown, so a ranking can always be justified."""
        if self.disqualified:
            return "%s: DISQUALIFIED - %s" % (self.subject_id, self.disqualification_reason)
        lines = [
            "%s: %.2f/10 (confidence: %s, weights: %s)"
            % (self.subject_id, self.total_score, self.overall_confidence.value, self.weight_set_id)
        ]
        for component in sorted(
            self.components, key=lambda c: float(c["weighted_value"]), reverse=True
        ):
            lines.append(
                "  %-28s %4.1f x %.2f = %5.2f  [%s] %s"
                % (
                    component["component_key"],
                    component["value"],
                    component["weight"],
                    component["weighted_value"],
                    component["confidence"],
                    component["rationale"],
                )
            )
        if self.components_missing:
            lines.append("  missing (not scored): %s" % ", ".join(self.components_missing))
        return "\n".join(lines)


def score(
    subject_id: str,
    components: Iterable[ScoreComponent],
    weight_set: WeightSet,
    disqualified: bool = False,
    disqualification_reason: Optional[str] = None,
) -> ScoreResult:
    """Compute a weighted score from components and a weight set.

    Two deliberate choices:

    * **Missing components are reported, not defaulted.** Substituting a middle value for
      an unscored dimension would flatter markets we simply know less about — exactly the
      emerging markets this project is inclined to favour.
    * **The total is normalised over the weights actually applied**, so a subject scored on
      eight of ten dimensions is not penalised as though it scored zero on the other two.
      The omission is surfaced in ``components_missing`` instead.
    """
    component_list = list(components)

    if disqualified and not disqualification_reason:
        raise ValueError("A disqualified subject requires a disqualification_reason")

    seen = set()
    for component in component_list:
        if component.component_key in seen:
            raise ValueError("Duplicate component %s for %s" % (component.component_key, subject_id))
        seen.add(component.component_key)

    scored_rows: List[Dict[str, object]] = []
    total_weighted = 0.0
    total_weight = 0.0

    for component in component_list:
        weight = weight_set.weight_for(component.component_key)
        weighted_value = component.value * weight
        total_weighted += weighted_value
        total_weight += weight
        scored_rows.append(
            {
                "component_key": component.component_key,
                "label": component.label,
                "value": component.value,
                "weight": weight,
                "weighted_value": weighted_value,
                "confidence": component.confidence.value,
                "rationale": component.rationale,
                "is_estimate": component.is_estimate,
            }
        )

    missing = [key for key in weight_set.weights if key not in seen and weight_set.weights[key] > 0]

    total = (total_weighted / total_weight) if total_weight > 0 else 0.0

    # Confidence propagates from the components that actually carry weight. A
    # low-confidence component with zero weight should not drag down the result.
    weighted_confidences = [
        c.confidence for c in component_list if weight_set.weight_for(c.component_key) > 0
    ]
    overall = weakest(*weighted_confidences) if weighted_confidences else Confidence.UNKNOWN

    # Unscored dimensions are themselves a form of uncertainty.
    if missing and overall == Confidence.HIGH:
        overall = Confidence.MEDIUM

    return ScoreResult(
        subject_id=subject_id,
        weight_set_id=weight_set.weight_set_id,
        total_score=round(total, 4),
        overall_confidence=overall,
        components=scored_rows,
        components_missing=missing,
        disqualified=disqualified,
        disqualification_reason=disqualification_reason,
    )


def rank(results: Iterable[ScoreResult]) -> List[ScoreResult]:
    """Rank scored subjects, best first.

    Disqualified subjects are excluded entirely rather than ranked last: a market where
    the operating model is not legal is not a worse option, it is not an option.
    """
    eligible = [r for r in results if not r.disqualified]
    return sorted(eligible, key=lambda r: r.total_score, reverse=True)
