"""Configuration loading.

Configuration is JSON and lives outside the code, so weights and thresholds can be
changed — by an owner, an agent or the dashboard — without touching logic. Keys beginning
with an underscore are treated as inline commentary and ignored, which lets config files
explain themselves without a separate document drifting out of date.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

from core.scoring.engine import WeightSet


def _strip_comments(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _strip_comments(v) for k, v in value.items() if not k.startswith("_")}
    if isinstance(value, list):
        return [_strip_comments(v) for v in value]
    return value


def load_json(path: str, strip_comments: bool = True) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise FileNotFoundError("Config not found: %s" % path)
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)
    return _strip_comments(document) if strip_comments else document


def load_weight_sets(path: str) -> Dict[str, WeightSet]:
    """Load named weight sets from a config file.

    Each set is validated on load rather than at first use, so a malformed config fails
    immediately and visibly instead of silently producing a ranking nobody can reproduce.
    """
    document = load_json(path)
    raw_sets = document.get("weight_sets", {})
    if not raw_sets:
        raise ValueError("No weight_sets defined in %s" % path)

    version = document.get("config_version")
    loaded: Dict[str, WeightSet] = {}
    for name, definition in raw_sets.items():
        weights = definition.get("weights")
        if not weights:
            raise ValueError("Weight set %r in %s has no weights" % (name, path))
        loaded[name] = WeightSet(
            weight_set_id=name,
            weights={k: float(v) for k, v in weights.items()},
            version=version,
            description=definition.get("description"),
        )
    return loaded


def default_weight_set(path: str) -> WeightSet:
    document = load_json(path)
    name = document.get("default_weight_set")
    if not name:
        raise ValueError("No default_weight_set declared in %s" % path)
    sets = load_weight_sets(path)
    if name not in sets:
        raise ValueError("default_weight_set %r is not defined in %s" % (name, path))
    return sets[name]


def load_catalyst_status_weights(path: str) -> Dict[str, float]:
    """Confidence weight per development status.

    Used wherever a pipeline is aggregated, so that a proposal cannot contribute to
    forward supply as though it were under construction.
    """
    document = load_json(path)
    weights = document.get("catalyst_status_weights")
    if not weights:
        raise ValueError("No catalyst_status_weights defined in %s" % path)
    return {k: float(v) for k, v in weights.items()}


def weighted_pipeline_total(
    items,
    status_weights: Dict[str, float],
    quantity_key: str = "rooms",
    status_key: str = "status",
) -> float:
    """Sum a pipeline, discounting each item by the confidence its status deserves.

    An unweighted count of announced projects is the standard way forward supply gets
    overstated; this makes the discount explicit and auditable.
    """
    total = 0.0
    for item in items:
        quantity = item.get(quantity_key)
        if quantity is None:
            continue
        weight = status_weights.get(item.get(status_key, "unknown"), 0.0)
        total += float(quantity) * weight
    return total
