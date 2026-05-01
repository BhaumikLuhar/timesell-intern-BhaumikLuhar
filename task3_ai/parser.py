import re


def parse_explanation(text: str) -> dict:
    """
    Parses structured output from LLM response.
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
