def advisor_prompt(portfolio, risk_metrics, user_goal: str):
    return f"""
You are a senior financial advisor.

USER GOAL:
{user_goal}

PORTFOLIO:
{portfolio}

RISK METRICS:
{risk_metrics}

TASK:
Give clear, actionable financial advice.

OUTPUT FORMAT:

ASSESSMENT:
(2-3 sentences evaluating portfolio vs goal)

RISKS:
(key risks in portfolio)

RECOMMENDATION:
(specific changes with reasoning)

CONFIDENCE:
(Low / Medium / High)
"""


def critic_prompt(advice_text, portfolio, risk_metrics):
    return f"""
You are a strict financial auditor.

PORTFOLIO:
{portfolio}

RISK METRICS:
{risk_metrics}

ADVISOR OUTPUT:
{advice_text}

TASK:
Critically evaluate the advice.

OUTPUT FORMAT:

ACCURACY:
(Is the advice correct? Explain briefly)

MISSING_POINTS:
(What important risks or factors were ignored?)

IMPROVEMENTS:
(How can the advice be better?)

FINAL_VERDICT:
(Good / Needs Improvement / Poor)
"""