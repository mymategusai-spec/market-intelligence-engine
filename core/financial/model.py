"""Capital and cash-flow modelling.

The governing rule: **purchase price is never the investment.** Total project cost is the
headline figure, and yield is reported against it as well as against purchase price. The
gap between those two yields is itself intelligence — it is where optimistic property
arithmetic usually hides.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from core.models.common import Confidence, Money, sum_money, weakest


@dataclass
class CapitalStack:
    """Everything required to get from listing to lawfully operating asset."""

    purchase_price: Money
    acquisition_costs: Optional[Money] = None
    taxes: Optional[Money] = None
    legal: Optional[Money] = None
    due_diligence: Optional[Money] = None
    renovation: Optional[Money] = None
    furnishing: Optional[Money] = None
    licensing_compliance: Optional[Money] = None
    working_capital: Optional[Money] = None
    contingency: Optional[Money] = None

    @property
    def currency(self) -> str:
        return self.purchase_price.currency

    def total_project_cost(self) -> Money:
        return sum_money(
            self.purchase_price,
            self.acquisition_costs,
            self.taxes,
            self.legal,
            self.due_diligence,
            self.renovation,
            self.furnishing,
            self.licensing_compliance,
            self.working_capital,
            self.contingency,
            currency=self.currency,
        )

    def cost_above_purchase_price(self) -> Money:
        """How much the purchase price understates the true investment."""
        total = self.total_project_cost()
        return Money(
            amount=total.amount - self.purchase_price.amount,
            currency=self.currency,
            is_estimate=total.is_estimate,
        )

    def missing_components(self) -> List[str]:
        """Unpopulated cost lines.

        Reported rather than silently treated as zero. An unmodelled compliance cost is
        the most common way a project budget turns out to be fiction.
        """
        return [
            name
            for name in (
                "acquisition_costs",
                "taxes",
                "legal",
                "due_diligence",
                "renovation",
                "furnishing",
                "licensing_compliance",
                "working_capital",
                "contingency",
            )
            if getattr(self, name) is None
        ]


@dataclass
class OwnerUse:
    """Owner use priced honestly, as revenue foregone at the rates that would apply.

    Treating personal use as free makes every lifestyle asset look like a better
    investment than it is.
    """

    weeks_per_year: float
    season: str
    revenue_foregone: Money
    offset_by_separate_quarters: Optional[bool] = None


@dataclass
class OperatingCosts:
    total: Money
    breakdown: Dict[str, Money] = field(default_factory=dict)

    @classmethod
    def from_breakdown(cls, currency: str, **items: Optional[Money]) -> "OperatingCosts":
        present = {k: v for k, v in items.items() if v is not None}
        total = sum_money(*present.values(), currency=currency)
        return cls(total=total, breakdown=present)


@dataclass
class FinancialResult:
    noi: Money
    gross_revenue: Money
    total_project_cost: Money
    yield_on_purchase_price_percent: Optional[float]
    yield_on_total_project_cost_percent: Optional[float]
    yield_gap_percentage_points: Optional[float]
    breakeven_occupancy_percent: Optional[float]
    confidence: Confidence
    caveats: List[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            "Gross revenue:        %s %s" % (self.gross_revenue.currency, _fmt(self.gross_revenue.amount)),
            "NOI:                  %s %s" % (self.noi.currency, _fmt(self.noi.amount)),
            "Total project cost:   %s %s" % (self.total_project_cost.currency, _fmt(self.total_project_cost.amount)),
        ]
        if self.yield_on_purchase_price_percent is not None:
            lines.append("Yield on purchase:    %.2f%%" % self.yield_on_purchase_price_percent)
        if self.yield_on_total_project_cost_percent is not None:
            lines.append("Yield on total cost:  %.2f%%  <- the honest figure" % self.yield_on_total_project_cost_percent)
        if self.yield_gap_percentage_points is not None:
            lines.append("Yield gap:            %.2f pp" % self.yield_gap_percentage_points)
        lines.append("Confidence:           %s" % self.confidence.value)
        for caveat in self.caveats:
            lines.append("  ! %s" % caveat)
        return "\n".join(lines)


def _fmt(amount: float) -> str:
    return "{:,.0f}".format(amount)


def compute(
    capital: CapitalStack,
    gross_annual_revenue: Money,
    operating_costs: OperatingCosts,
    owner_use: Optional[OwnerUse] = None,
    input_confidence: Optional[List[Confidence]] = None,
) -> FinancialResult:
    """Produce NOI and yields from a capital stack and a trading assumption.

    Owner use is deducted from revenue rather than ignored, so the reported yield is the
    yield the owners would actually experience — unless separate quarters let the asset
    keep trading while they are there.
    """
    currency = capital.currency
    for label, money in (
        ("gross revenue", gross_annual_revenue),
        ("operating costs", operating_costs.total),
    ):
        if money.currency != currency:
            raise ValueError(
                "%s is in %s but capital stack is in %s; attach an explicit conversion"
                % (label, money.currency, currency)
            )

    caveats: List[str] = []

    effective_revenue = gross_annual_revenue
    if owner_use is not None and not owner_use.offset_by_separate_quarters:
        if owner_use.revenue_foregone.currency != currency:
            raise ValueError("Owner-use revenue foregone is in a different currency")
        effective_revenue = Money(
            amount=gross_annual_revenue.amount - owner_use.revenue_foregone.amount,
            currency=currency,
            is_estimate=gross_annual_revenue.is_estimate or owner_use.revenue_foregone.is_estimate,
        )
        caveats.append(
            "Revenue is net of %.1f weeks owner use (%s %s foregone)"
            % (owner_use.weeks_per_year, currency, _fmt(owner_use.revenue_foregone.amount))
        )
    elif owner_use is not None:
        caveats.append(
            "Owner use assumed not to displace revenue (separate owner/manager quarters)"
        )

    noi = Money(
        amount=effective_revenue.amount - operating_costs.total.amount,
        currency=currency,
        is_estimate=effective_revenue.is_estimate or operating_costs.total.is_estimate,
    )

    total_cost = capital.total_project_cost()

    yield_purchase = (
        (noi.amount / capital.purchase_price.amount) * 100.0
        if capital.purchase_price.amount > 0
        else None
    )
    yield_total = (noi.amount / total_cost.amount) * 100.0 if total_cost.amount > 0 else None
    gap = (
        yield_purchase - yield_total
        if yield_purchase is not None and yield_total is not None
        else None
    )

    breakeven = None
    if effective_revenue.amount > 0:
        breakeven = min(100.0, (operating_costs.total.amount / effective_revenue.amount) * 100.0)

    missing = capital.missing_components()
    if missing:
        caveats.append(
            "Capital stack incomplete - not modelled: %s. Total project cost is understated."
            % ", ".join(missing)
        )

    if capital.contingency is None:
        caveats.append("No contingency modelled; value-add works routinely overrun.")

    confidences = list(input_confidence or [])
    if total_cost.is_estimate or noi.is_estimate:
        confidences.append(Confidence.LOW)
    overall = weakest(*confidences) if confidences else Confidence.UNKNOWN

    return FinancialResult(
        noi=noi,
        gross_revenue=effective_revenue,
        total_project_cost=total_cost,
        yield_on_purchase_price_percent=yield_purchase,
        yield_on_total_project_cost_percent=yield_total,
        yield_gap_percentage_points=gap,
        breakeven_occupancy_percent=breakeven,
        confidence=overall,
        caveats=caveats,
    )
