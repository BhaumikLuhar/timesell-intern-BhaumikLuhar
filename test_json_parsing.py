#!/usr/bin/env python3
"""Test that markdown fence stripping works correctly"""

import json
from task3_ai.parser import format_explanation

# Simulate the LLM response WITH markdown code fences
test_cases = [
    {
        "name": "Markdown-wrapped JSON (what we're fixing)",
        "response": """```json
{
  "summary": "Your portfolio is highly concentrated in cryptocurrencies like BTC and ETH, making it very aggressive. In a severe market crash, your total value could drop by over 60%.",
  "good": "It's positive that even in a severe downturn, your portfolio is not entirely wiped out.",
  "improve": "You should significantly reduce your high concentration in BTC and ETH.",
  "verdict": "Aggressive"
}
```"""
    },
    {
        "name": "Plain JSON (ideal case)",
        "response": """{
  "summary": "Your portfolio is well-balanced with good diversification across assets and sufficient cash reserves.",
  "good": "Strong cash allocation of 20% provides good financial runway for at least 8+ years.",
  "improve": "Consider rebalancing quarterly to maintain your target allocation and reduce gold holdings.",
  "verdict": "Balanced"
}"""
    }
]

print("="*70)
print("TESTING JSON PARSING WITH MARKDOWN FENCE STRIPPING")
print("="*70)

for test in test_cases:
    print(f"\n📝 Test Case: {test['name']}")
    print("-" * 70)

    text = test["response"].strip()

    # Apply the stripping logic from explainer.py
    if text.startswith("```"):
        text = text.split("```")[1]  # Get content between fences
        if text.startswith("json\n"):
            text = text[5:]  # Remove 'json\n'
        text = text.strip()

    try:
        result = json.loads(text)
        print("✅ JSON parsed successfully!\n")
        print("Formatted Output:")
        print(format_explanation(result))
    except Exception as e:
        print(f"❌ Failed: {e}")
        print(f"Text to parse: {text[:100]}...")
