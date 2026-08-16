"""Shared value types used across the engine.

Mirrors ``schemas/core/common.json``. The schema is canonical; these types exist for
typed construction and arithmetic in Python. Standard library only.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date
from enum import Enum
from typing import Any, Dict, Optional


class ClaimType(str, Enum):
    """How a value came to be known.

    The distinction is load-bearing: an ESTIMATE presented as a FACT is the single
    easiest way for this system to mislead its owners.
    """

    FACT = "FACT"
    CALCULATION = "CALCULATION"
    ESTIMATE = "ESTIMATE"
    ASSUMPTION = "ASSUMPTION"
    OPINION = "OPINION"


class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


#: Ordering used when propagating confidence. Lower is weaker.
_CONFIDENCE_RANK = {
    Confidence.UNKNOWN: 0,
    Confidence.LOW: 1,
    Confidence.MEDIUM: 2,
    Confidence.HIGH: 3,
}

_RANK_TO_CONFIDENCE = {rank: conf for conf, rank in _CONFIDENCE_RANK.items()}


def weakest(*confidences: Confidence) -> Confidence:
    """Return the weakest confidence given.

    Confidence propagates pessimistically: a conclusion is only as trustworthy as its
    least trustworthy input. Averaging would let one high-confidence input launder a
    pile of guesses into apparent certainty.
    """
    if not confidences:
        return Confidence.UNKNOWN
    return _RANK_TO_CONFIDENCE[min(_CONFIDENCE_RANK[c] for c in confidences)]


class SourceStatus(str, Enum):
    CANDIDATE = "CANDIDATE"
    ACCESSED = "ACCESSED"
    BLOCKED = "BLOCKED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class FxConversion:
    """A currency conversion, inseparable from the rate and the date of that rate.

    An AUD figure without them cannot be interpreted a year later, and cannot be
    recomputed when the rate moves.
    """

    from_currency: str
    to_currency: str
    rate: float
    rate_date: date
    rate_source_id: Optional[str] = None

    def __post_init__(self) -> None:
        if self.rate <= 0:
            raise ValueError("FX rate must be positive")
        if len(self.from_currency) != 3 or len(self.to_currency) != 3:
            raise ValueError("Currency codes must be ISO 4217 three-letter codes")

    def convert(self, amount: float) -> float:
        return amount * self.rate


@dataclass(frozen=True)
class Money:
    """An amount in its original currency, optionally with a conversion attached.

    The original is never discarded. Estimates carry a range rather than pretending to
    a precision the evidence does not support.
    """

    amount: float
    currency: str
    converted_amount: Optional[float] = None
    converted_currency: Optional[str] = None
    fx: Optional[FxConversion] = None
    is_estimate: bool = False
    range_low: Optional[float] = None
    range_high: Optional[float] = None

    def __post_init__(self) -> None:
        if len(self.currency) != 3:
            raise ValueError("Currency must be an ISO 4217 three-letter code")
        if self.converted_amount is not None and self.fx is None:
            raise ValueError(
                "A converted amount requires its FX conversion (rate and rate date). "
                "Silent conversion destroys auditability."
            )
        if self.range_low is not None and self.range_high is not None:
            if self.range_low > self.range_high:
                raise ValueError("range_low cannot exceed range_high")

    @classmethod
    def of(cls, amount: float, currency: str) -> "Money":
        return cls(amount=amount, currency=currency)

    @classmethod
    def estimate(cls, low: float, high: float, currency: str) -> "Money":
        """An estimate is a range whose point value is its midpoint, and which says so."""
        return cls(
            amount=(low + high) / 2.0,
            currency=currency,
            is_estimate=True,
            range_low=low,
            range_high=high,
        )

    def converted_to(self, fx: FxConversion) -> "Money":
        if fx.from_currency != self.currency:
            raise ValueError(
                "FX conversion is from %s but amount is in %s" % (fx.from_currency, self.currency)
            )
        return Money(
            amount=self.amount,
            currency=self.currency,
            converted_amount=fx.convert(self.amount),
            converted_currency=fx.to_currency,
            fx=fx,
            is_estimate=self.is_estimate,
            range_low=self.range_low,
            range_high=self.range_high,
        )

    def in_currency(self, currency: str) -> float:
        """Value in the requested currency, or raise if it cannot be produced honestly."""
        if currency == self.currency:
            return self.amount
        if self.converted_currency == currency and self.converted_amount is not None:
            return self.converted_amount
        raise ValueError(
            "No conversion to %s available; attach an FxConversion rather than "
            "assuming a rate" % currency
        )

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(
                "Cannot add %s to %s without an explicit conversion" % (other.currency, self.currency)
            )
        low = None
        high = None
        if self.range_low is not None or other.range_low is not None:
            low = (self.range_low if self.range_low is not None else self.amount) + (
                other.range_low if other.range_low is not None else other.amount
            )
            high = (self.range_high if self.range_high is not None else self.amount) + (
                other.range_high if other.range_high is not None else other.amount
            )
        return Money(
            amount=self.amount + other.amount,
            currency=self.currency,
            is_estimate=self.is_estimate or other.is_estimate,
            range_low=low,
            range_high=high,
        )


def sum_money(*amounts: Optional[Money], currency: str) -> Money:
    """Total a set of optional amounts, preserving estimate ranges.

    Missing components are treated as absent, not as zero-with-confidence: the caller
    is responsible for knowing whether an omission means "nil" or "unknown".
    """
    total = Money(amount=0.0, currency=currency)
    for item in amounts:
        if item is None:
            continue
        total = total + item
    return total


@dataclass(frozen=True)
class Provenance:
    """Ties a value to a source, a date and an honesty rating.

    Every material value in the engine carries one. A value without provenance cannot
    be audited and therefore cannot support an investment decision.
    """

    source_id: str
    retrieved_at: date
    claim_type: ClaimType
    confidence: Confidence
    notes: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.source_id:
            raise ValueError("Provenance requires a source_id")


@dataclass
class RecordMeta:
    schema_version: str = "1.0.0"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    supersedes: Optional[str] = None
    superseded_by: Optional[str] = None


@dataclass
class Transformation:
    """Any change between the published value and the stored value."""

    kind: str
    description: str
    formula: Optional[str] = None
    applied_by: Optional[str] = None


def to_dict(obj: Any) -> Dict[str, Any]:
    """Serialise a dataclass to plain JSON-compatible types."""

    def _convert(value: Any) -> Any:
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, date):
            return value.isoformat()
        if isinstance(value, dict):
            return {k: _convert(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [_convert(v) for v in value]
        return value

    return {k: _convert(v) for k, v in asdict(obj).items()}
