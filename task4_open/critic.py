import os
from dotenv import load_dotenv
import google.generativeai as genai
from task4_open.prompt_templates import critic_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Set GEMINI_API_KEY in your .env file to use Gemini.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a financial auditor.",
)


def critique_advice(advice_text, portfolio, risk_metrics):
    prompt = critic_prompt(advice_text, portfolio, risk_metrics)

    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0.3},
    )

    return response.text
