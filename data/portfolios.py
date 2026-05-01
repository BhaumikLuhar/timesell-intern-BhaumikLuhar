portfolios = {
    "aggressive": {
        "total_value_inr": 10_000_000,
        "monthly_expenses_inr": 80_000,
        "assets": [
            {"name": "BTC", "allocation_pct": 50, "expected_crash_pct": -80},
            {"name": "ETH", "allocation_pct": 20, "expected_crash_pct": -70},
            {"name": "NIFTY50", "allocation_pct": 20, "expected_crash_pct": -40},
            {"name": "CASH", "allocation_pct": 10, "expected_crash_pct": 0},
        ],
    },

    "balanced": {
        "total_value_inr": 10_000_000,
        "monthly_expenses_inr": 80_000,
        "assets": [
            {"name": "NIFTY50", "allocation_pct": 40, "expected_crash_pct": -40},
            {"name": "GOLD", "allocation_pct": 30, "expected_crash_pct": -15},
            {"name": "BTC", "allocation_pct": 10, "expected_crash_pct": -80},
            {"name": "CASH", "allocation_pct": 20, "expected_crash_pct": 0},
        ],
    },

    "conservative": {
        "total_value_inr": 10_000_000,
        "monthly_expenses_inr": 80_000,
        "assets": [
            {"name": "FD", "allocation_pct": 40, "expected_crash_pct": -5},
            {"name": "GOLD", "allocation_pct": 30, "expected_crash_pct": -15},
            {"name": "NIFTY50", "allocation_pct": 20, "expected_crash_pct": -40},
            {"name": "CASH", "allocation_pct": 10, "expected_crash_pct": 0},
        ],
    },
}