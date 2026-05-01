from data.sample_portfolio import portfolio

# Task 1
from task1_risk.risk_calculator import compute_risk_metrics
from task1_risk.visualizer import print_allocation_chart

# Task 2
from task2_market.fetch_prices import fetch_all_prices
from task2_market.formatter import print_price_table

# Task 3
from task3_ai.explainer import generate_explanation
from task3_ai.parser import parse_explanation

# Task 4
from task4_open.runner import run_ai_advisor_system

# -----------------------------
# TASK 1 — Portfolio Risk
# -----------------------------
def run_task1():
    print("=" * 60)
    print("TASK 1 — Portfolio Risk Calculator")
    print("=" * 60)

    try:
        result = compute_risk_metrics(portfolio)

        print("\n--- Risk Metrics ---\n")

        print("Severe Scenario:")
        print(result["severe_scenario"])

        print("\nModerate Scenario:")
        print(result["moderate_scenario"])

        print("\nOther Insights:")
        print(f"Ruin Test: {result['ruin_test']}")
        print(f"Largest Risk Asset: {result['largest_risk_asset']}")
        print(f"Concentration Warning: {result['concentration_warning']}")

        print_allocation_chart(portfolio["assets"])

    except Exception as e:
        print(f"Error in Task 1: {e}")


# -----------------------------
# TASK 2 — Market Data Fetch
# -----------------------------
def run_task2():
    print("\n" + "=" * 60)
    print("TASK 2 — Live Market Data Fetch")
    print("=" * 60)

    try:
        results = fetch_all_prices()
        print_price_table(results)

    except Exception as e:
        print(f"Error in Task 2: {e}")

# -----------------------------
# TASK 3 — AI Portfolio Explainer
# -----------------------------
def run_task3():
    print("\n" + "=" * 60)
    print("TASK 3 — AI Portfolio Explainer")
    print("=" * 60)

    try:
        # reuse Task 1 output
        risk_metrics = compute_risk_metrics(portfolio)

        raw_output = generate_explanation(portfolio, risk_metrics, tone="beginner")

        print("\n--- RAW LLM OUTPUT ---\n")
        print(raw_output)

        parsed = parse_explanation(raw_output)

        print("\n--- STRUCTURED OUTPUT ---\n")
        for k, v in parsed.items():
            print(f"{k.upper()}: {v}")

    except Exception as e:
        print(f"Error in Task 3: {e}")

# -----------------------------
# TASK 4 — AI Decision Advisor + Critic
# -----------------------------
def run_task4():
    run_ai_advisor_system(portfolio)


# -----------------------------
# MAIN ENTRY
# -----------------------------
def main():
    print("\n🚀 Timecell AI Internship Technical Test\n")

    # Run tasks
    run_task1()
    run_task2()
    run_task3()
    run_task4()

    print("\n✅ Execution Completed\n")


if __name__ == "__main__":
    main()