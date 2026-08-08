from client import LlmApiCostModelSelectorOptimizerClient

def main():
    client = LlmApiCostModelSelectorOptimizerClient()
    res = client.select_optimal_model(8_000_000, "MEDIUM", 1500)
    print(f"Recommended Tier: {res['recommended_model_tier']}")
    print(f"Estimated Monthly Cost: ${res['estimated_monthly_cost_usd']}")
    print(f"Potential Monthly Savings: ${res['savings_vs_current_usd']}")

if __name__ == "__main__":
    main()
