import os
import json

from dotenv import load_dotenv
import google.generativeai as genai

from task3_ai.prompt_builder import build_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Set GEMINI_API_KEY in your .env file to use Gemini.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a financial advisor.",
)


def generate_explanation(portfolio: dict, risk_metrics: dict, tone="beginner"):
    """
    Calls LLM and returns parsed JSON response
    """
    prompt = build_prompt(portfolio, risk_metrics, tone)

    try:
        response = model.generate_content(
            prompt,
            generation_config={"temperature": 0.5},
        )

        # Clean response text by removing markdown code fences
        text = response.text.strip()
        if text.startswith("```"):
            # Remove markdown code fence
            text = text.split("```")[1]  # Get content between fences
            if text.startswith("json\n"):
                text = text[5:]  # Remove 'json\n'
            text = text.strip()

        # Parse JSON response
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            # If still failing, show the raw text
            return {"error": f"Invalid JSON: {str(e)}\nRaw response: {response.text}"}
    except Exception as e:
        # Handle quota exceeded or other API errors
        error_msg = str(e)
        if "quota" in error_msg.lower() or "resource_exhausted" in error_msg.lower():
            return {
                "summary": "API quota limit reached. Please try again later.",
                "good": "N/A",
                "improve": "N/A",
                "verdict": "N/A",
                "error": "Gemini API quota exceeded"
            }
        else:
            return {"error": f"API Error: {error_msg}"}
