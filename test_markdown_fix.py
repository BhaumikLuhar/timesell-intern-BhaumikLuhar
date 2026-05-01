import json

# Simulate the LLM response with markdown code fences
raw_response = """```json
{
  "summary": "Your portfolio is highly concentrated in cryptocurrencies like BTC and ETH, making it very aggressive. In a severe market crash, your total value could drop by over 60%, leaving you with about INR 3.8 million.",
  "good": "It's positive that even in a severe downturn, your portfolio is not entirely wiped out, leaving you with a substantial amount (INR 3.8 million) to cover expenses for a few years.",
  "improve": "You should significantly reduce your high concentration in BTC and ETH. Having 70% of your portfolio in these highly volatile assets means any major crash in crypto markets would severely impact your overall wealth and financial security.",
  "verdict": "Aggressive"
}
```"""

# Test the stripping logic
text = raw_response.strip()
if text.startswith("```"):
    text = text.split("```")[1]  # Get content between fences
    if text.startswith("json\n"):
        text = text[5:]  # Remove 'json\n'
    text = text.strip()

print("Cleaned text:")
print(text)
print("\n" + "="*60 + "\n")

# Try parsing
try:
    result = json.loads(text)
    print("✅ Successfully parsed JSON!")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"❌ Failed to parse: {e}")
