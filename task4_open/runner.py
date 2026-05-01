from task1_risk.risk_calculator import compute_risk_metrics
from task4_open.advisor import generate_advice
from task4_open.critic import critique_advice
from task4_open.validator import is_valid_financial_goal

def get_valid_goal():
    while True:
        goal = input("\nEnter your financial goal: ")

        if is_valid_financial_goal(goal):
            return goal
        else:
            print("\n❌ Invalid input.")
            print("👉 Please enter a financial goal (e.g., retirement planning, reducing risk, stable income).")

def run_ai_advisor_system(portfolio):
    print("\n" + "=" * 60)
    print("TASK 4 — AI Decision Advisor + Critic")
    print("=" * 60)

    # Step 1 — Compute metrics
    risk_metrics = compute_risk_metrics(portfolio)

    # Step 2 — Ask user goal
    user_goal = get_valid_goal()

    try:
        # Step 3 — Advisor
        advice = generate_advice(portfolio, risk_metrics, user_goal)

        print("\n--- AI ADVISOR OUTPUT ---\n")
        print(advice)

        # Step 4 — Critic
        critique = critique_advice(advice, portfolio, risk_metrics)

        print("\n--- AI CRITIC OUTPUT ---\n")
        print(critique)
    except Exception as e:
        print(f"Error in Task 4: {e}")
