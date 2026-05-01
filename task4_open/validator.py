def is_valid_financial_goal(goal: str) -> bool:
    """
    Basic validation for financial goal input
    """

    if not goal or len(goal.strip()) < 5:
        return False

    goal = goal.lower()

    keywords = [
        "invest", "portfolio", "risk", "return", "income",
        "retirement", "wealth", "financial", "safe", "growth",
        "money", "savings", "expense", "cashflow"
    ]

    return any(word in goal for word in keywords)