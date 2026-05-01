import os
from dotenv import load_dotenv
import google.generativeai as genai
from task4_open.prompt_templates import advisor_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Set GEMINI_API_KEY in your .env file to use Gemini.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a financial advisor.",
)


def generate_advice(portfolio, risk_metrics, user_goal):
    prompt = advisor_prompt(portfolio, risk_metrics, user_goal)

    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0.5},
    )

    return response.text
