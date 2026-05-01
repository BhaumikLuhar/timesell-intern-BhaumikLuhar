import re


def parse_explanation(text: str) -> dict:
    """
    Parses structured output from LLM response (legacy - for text format).
    """

    sections = {
        "summary": "",
        "good": "",
        "improve": "",
        "verdict": ""
    }

    current = None

    header_pattern = re.compile(
        r"^\**\s*(summary|good|improve|verdict)\s*:?\s*\**$",
        re.IGNORECASE,
    )

    for line in text.split("\n"):
        line = line.strip()

        header_match = header_pattern.match(line)
        if header_match:
            current = header_match.group(1).lower()
            continue

        if current and line:
            sections[current] += line + " "

    # Clean
    for key in sections:
        sections[key] = sections[key].strip()

    return sections


def format_explanation(explanation: dict) -> str:
    """
    Formats JSON explanation dict for pretty printing.
    """
    if "error" in explanation:
        return f"\n⚠️  Error: {explanation['error']}\n"

    formatted = "\n" + "=" * 60 + "\n"
    formatted += "📊 PORTFOLIO EXPLANATION\n"
    formatted += "=" * 60 + "\n\n"

    # Summary
    if "summary" in explanation:
        formatted += "📋 SUMMARY:\n"
        formatted += f"{explanation['summary']}\n\n"

    # Good
    if "good" in explanation:
        formatted += "✅ STRENGTHS:\n"
        formatted += f"{explanation['good']}\n\n"

    # Improve
    if "improve" in explanation:
        formatted += "⚡ IMPROVEMENTS:\n"
        formatted += f"{explanation['improve']}\n\n"

    # Verdict
    if "verdict" in explanation:
        formatted += "🎯 VERDICT:\n"
        formatted += f"{explanation['verdict']}\n"

    formatted += "=" * 60 + "\n"

    return formatted
