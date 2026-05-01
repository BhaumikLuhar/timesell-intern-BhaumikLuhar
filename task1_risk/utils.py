import math

def validate_portfolio(portfolio: dict):
    """
    Validates the portfolio structure and values.
    Raises ValueError if invalid.
    """
    if "total_value_inr" not in portfolio or portfolio["total_value_inr"] < 0:
        raise ValueError("Invalid or missing total_value_inr")

    if "monthly_expenses_inr" not in portfolio or portfolio["monthly_expenses_inr"] < 0:
        raise ValueError("Invalid or missing monthly_expenses_inr")

    if "assets" not in portfolio or not isinstance(portfolio["assets"], list):
        raise ValueError("Assets must be a list")

    if len(portfolio["assets"]) == 0:
        raise ValueError("Portfolio must contain at least one asset")

    total_allocation = 0

    for asset in portfolio["assets"]:
        if "allocation_pct" not in asset or asset["allocation_pct"] < 0:
            raise ValueError(f"Invalid allocation in asset {asset.get('name')}")

        if "expected_crash_pct" not in asset:
            raise ValueError(f"Missing crash pct in asset {asset.get('name')}")

        total_allocation += asset["allocation_pct"]

    if total_allocation == 0:
        raise ValueError("Total allocation cannot be zero")


def normalize_allocations(assets: list):
    """
    Ensures allocations sum to 100%.
    If not, normalizes them proportionally.
    """
    total = sum(a["allocation_pct"] for a in assets)

    if total == 100:
        return assets

    normalized_assets = []
    for asset in assets:
        normalized_asset = asset.copy()
        normalized_asset["allocation_pct"] = (asset["allocation_pct"] / total) * 100
        normalized_assets.append(normalized_asset)

    return normalized_assets


def compute_asset_post_crash_value(total_value: float, allocation_pct: float, crash_pct: float):
    """
    Computes post-crash value of a single asset.
    """
    allocation = allocation_pct / 100
    crash = crash_pct / 100

    # Clamp crash to -100% minimum
    crash = max(crash, -1)

    return total_value * allocation * (1 + crash)


def compute_risk_score(asset: dict):
    """
    Risk = allocation * absolute crash magnitude
    """
    return asset["allocation_pct"] * abs(asset["expected_crash_pct"])


def compute_total_post_crash_value(total_value: float, assets: list, crash_scale: float = 1.0):
    """
    Computes total portfolio value after applying scaled crash.
    
    crash_scale = 1.0 → severe crash
    crash_scale = 0.5 → moderate crash
    """
    total = 0

    for asset in assets:
        allocation = asset["allocation_pct"]
        crash = asset["expected_crash_pct"] * crash_scale

        total += compute_asset_post_crash_value(
            total_value,
            allocation,
            crash,
        )

    return total