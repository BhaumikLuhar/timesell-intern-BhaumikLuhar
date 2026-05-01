from data.sample_portfolio import portfolios

# Task 1
from task1_risk.risk_calculator import compute_risk_metrics
from task1_risk.visualizer import print_allocation_chart

# Task 2
from task2_market.fetch_prices import fetch_all_prices_from_portfolio
from task2_market.formatter import print_price_table

# Task 3
from task3_ai.explainer import generate_explanation
from task3_ai.parser import parse_explanation

# Task 4
from task4_open.runner import run_ai_advisor_system


# -----------------------------
# SELECT PORTFOLIO
# -----------------------------
def select_portfolio():
    print("\nAvailable Portfolios:\n")

    keys = list(portfolios.keys())

    for i, key in enumerate(keys, 1):
        print(f"{i}. {key}")

    choice = int(input("\nSelect a portfolio: "))
    selected_key = keys[choice - 1]

    return portfolios[selected_key], selected_key


# -----------------------------
# FULL PIPELINE
# -----------------------------
def run_full_analysis(portfolio, name):
    print("\n" + "=" * 60)
    print(f"RUNNING FULL ANALYSIS FOR: {name.upper()}")
    print("=" * 60)

    # 🔵 Task 1
    print("\n--- TASK 1: RISK METRICS ---\n")
    risk_metrics = compute_risk_metrics(portfolio)
    print(risk_metrics)
    print_allocation_chart(portfolio["assets"])

    # 🔵 Task 2
    print("\n--- TASK 2: MARKET DATA ---\n")
    results = fetch_all_prices_from_portfolio(portfolio)
    print_price_table(results)

    # 🔵 Task 3
    print("\n--- TASK 3: AI EXPLANATION ---\n")
    raw_output = generate_explanation(portfolio, risk_metrics)
    print("\nRAW OUTPUT:\n", raw_output)

    # 🔵 Task 4
    print("\n--- TASK 4: AI DECISION SYSTEM ---\n")
    run_ai_advisor_system(portfolio)


# -----------------------------
# MAIN
# -----------------------------
def main():
    print("\n🚀 Timecell AI Portfolio Analysis System\n")

    portfolio, name = select_portfolio()
    run_full_analysis(portfolio, name)

    print("\n✅ Analysis Completed\n")


if __name__ == "__main__":
    main()