def build_prompt(portfolio: dict, risk_metrics: dict, tone: str = "beginner") -> str:
    """
    Builds a structured prompt for LLM.
    """

    tone_map = {
        "beginner": "Explain in very simple, non-technical language.",
        "experienced": "Use moderately technical financial language.",
        "expert": "Use precise financial terminology."
    }

    return f"""
You are a professional financial advisor.

Your job is to explain portfolio risk clearly and honestly.

{tone_map.get(tone, tone_map["beginner"])}

INPUT DATA:
Portfolio:
{portfolio}

Risk Metrics:
{risk_metrics}

INSTRUCTIONS:
- Be concise but insightful.
- Do NOT use jargon unless tone = expert.
- Be specific (mention assets like BTC, NIFTY, etc.)

OUTPUT FORMAT (IMPORTANT — RESPOND WITH ONLY THE JSON OBJECT, NO MARKDOWN CODE FENCES, NO BACKTICKS, NO EXPLANATION):

{{
  "summary": "3-4 sentences explaining overall risk",
  "good": "One thing the investor is doing well",
  "improve": "One specific improvement + why",
  "verdict": "Only one word: Aggressive / Balanced / Conservative"
}}
"""
