# 🚀 Timecell AI Internship Technical Test

This repository contains my implementation of the **Timecell AI & Fintech Engineering Internship Technical Assessment (2025)**.

The project simulates a real-world AI-powered wealth management system by combining:

- Quantitative portfolio risk analysis
- Live market data integration
- AI-generated financial insights
- Decision-making and validation using multi-stage AI

---

## 🎯 Project Objective

The goal of this project is to build a **modular, production-style Python system** that evaluates, explains, and improves investment portfolios — similar to what Timecell aims to build.

Rather than solving isolated problems, the system is designed as a **connected pipeline**:

`Portfolio → Risk Engine → Market Data → AI Explanation → AI Decision System`

---

## 🧩 Tasks Implemented

### 🔵 Task 1 — Portfolio Risk Calculator

**✔ Features**
- Computes **post-crash portfolio value**
- Calculates **runway (months of survival)**
- Performs **ruin test (PASS / FAIL)**
- Identifies:
  - Largest risk asset
  - Concentration risk
- Handles **edge cases** (zero expenses, invalid allocations, etc.)

**⭐ Enhancements**
- Added **moderate crash scenario (50% severity)**
- Built **CLI allocation visualization (ASCII bar chart)**

**🧠 Key Insight**
Portfolio safety is not about returns — it's about **survival under stress scenarios**.

---

### 🔵 Task 2 — Live Market Data Fetch

**✔ Features**
- Fetches real-time prices for:
  - Stock/index (via Yahoo Finance)
  - Crypto (via CoinGecko)
- Displays clean **CLI table output**
- Includes:
  - Timestamp
  - Currency normalization

**⚙️ Engineering Focus**
- Fault-tolerant API calls
- Logging errors instead of crashing
- Consistent data structure across sources

---

### 🔵 Task 3 — AI-Powered Portfolio Explainer

**✔ Features**
- Converts quantitative risk into **plain-English financial advice**
- Structured output:
  - Summary
  - Strength
  - Improvement suggestion
  - Verdict (Aggressive / Balanced / Conservative)

**🧠 Prompt Design**
- Strong output constraints for consistency
- Tone control (`beginner / experienced / expert`)
- Grounded using real risk metrics (from Task 1)

**⚙️ Engineering**
- Separation of:
  - Prompt construction
  - API call
  - Output parsing

---

### 🔵 Task 4 — AI Decision Advisor + Critic System

**💡 Concept**
A **two-stage AI system** that not only gives financial advice but also evaluates its own quality.

**🧠 Stage 1 — AI Decision Advisor**
- Takes:
  - Portfolio
  - Risk metrics
  - User goal
- Produces:
  - Goal-based assessment
  - Risk identification
  - Actionable recommendations

**🔍 Stage 2 — AI Critic**
- Evaluates advisor output for:
  - Accuracy
  - Missing insights
  - Weak reasoning

**🎯 Why This Matters**
Most AI systems generate answers.
This system **questions its own answers**.

This reflects real-world financial decision-making where:
- Advice must be **validated**, not blindly trusted

**🧠 Key Insight**
This task demonstrates **AI system design**, not just API usage.

---

## 🏗️ Architecture
```text
timecell-intern-bhaumik/
│
├── data/              # Input portfolio
├── task1_risk/        # Risk computation engine
├── task2_market/      # Market data pipeline
├── task3_ai/          # AI explanation layer
├── task4_open/        # AI decision + critique system
├── logs/              # Error logs
└── main.py            # Entry point
```


## ⚙️ Tech Stack

- Python 3.10+
- `yfinance` (stocks)
- `CoinGecko API` (crypto)
- `google-generativeai API` (LLM)
- `tabulate` (CLI output)
- `python-dotenv` (env management)

---

## 🧠 Design Decisions

### 1. Modular Architecture
Each task is isolated into its own module:
- Improves readability
- Enables reuse across tasks

### 2. Separation of Concerns
- Computation ≠ API calls ≠ AI prompting
- Makes system easier to debug and extend

### 3. Grounded AI Outputs
All AI responses are based on:
- Real portfolio data
- Computed risk metrics

*This reduces hallucination risk.*

### 4. Fault-Tolerant System
- API failures are logged, not fatal
- System continues execution

---

## 🤖 AI Usage

AI tools (ChatGPT / Copilot) were used for:
- Structuring approach
- Improving prompt design
- Refining edge-case handling

All outputs were:
- Reviewed
- Understood
- Modified before use

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py
```
## ⚠️ Challenges Faced

### 1. Prompt Consistency
Ensuring the LLM produces structured output reliably required:
- Multiple prompt iterations
- Strict formatting constraints

### 2. Avoiding AI Hallucination
Solved by:
- Passing real computed metrics
- Constraining outputs

### 3. API Reliability
Handled using:
- Try/catch blocks
- Logging failures

### 4. Designing Task 4
The challenge was moving beyond:  
**“using AI” → to → “designing an AI system”**

---

## 🚀 Key Learnings

- Financial risk is about downside protection, not just returns.
- AI systems need structure and constraints to be reliable.
- Clean architecture matters as much as correctness.
- Combining small modules creates powerful systems.

---

## 🏁 Conclusion

This project demonstrates:
- Strong fundamentals in Python and system design.
- Practical use of APIs and real-world data.
- Thoughtful integration of AI into decision-making workflows.
- Ability to think beyond tasks and build product-like systems.

---

**Thank you for reviewing my submission.**
