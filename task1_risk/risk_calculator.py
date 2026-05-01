from task1_risk.utils import (
    validate_portfolio,
    normalize_allocations,
    compute_total_post_crash_value,
    compute_risk_score,
)


def compute_risk_metrics(portfolio: dict) -> dict:
    validate_portfolio(portfolio)

    total_value = portfolio["total_value_inr"]
    monthly_expenses = portfolio["monthly_expenses_inr"]
    assets = normalize_allocations(portfolio["assets"])

    # 🔴 Severe crash
    severe_value = compute_total_post_crash_value(total_value, assets, crash_scale=1.0)

    # 🟡 Moderate crash
    moderate_value = compute_total_post_crash_value(total_value, assets, crash_scale=0.5)

    # Runway calculations
    def compute_runway(value):
        return float("inf") if monthly_expenses == 0 else value / monthly_expenses

    severe_runway = compute_runway(severe_value)
    moderate_runway = compute_runway(moderate_value)

    # Ruin test (based on severe scenario)
    ruin_test = "PASS" if severe_runway > 12 else "FAIL"

    # Largest risk asset
    largest_risk_asset = max(assets, key=compute_risk_score)["name"]

    # Concentration warning
    concentration_warning = any(a["allocation_pct"] > 40 for a in assets)

    return {
        "severe_scenario": {
            "post_crash_value": round(severe_value, 2),
            "runway_months": round(severe_runway, 2) if severe_runway != float("inf") else float("inf"),
        },
        "moderate_scenario": {
            "post_crash_value": round(moderate_value, 2),
            "runway_months": round(moderate_runway, 2) if moderate_runway != float("inf") else float("inf"),
        },
        "ruin_test": ruin_test,
        "largest_risk_asset": largest_risk_asset,
        "concentration_warning": concentration_warning,
    }