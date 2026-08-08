class LlmApiCostModelSelectorOptimizerClient:
    def select_optimal_model(self, monthly_token_volume: int, task_complexity: str = "MEDIUM", latency_requirement_ms: int = 2000) -> dict:
        if task_complexity == "LOW" or monthly_token_volume > 5_000_000:
            tier = "EFFICIENT_LIGHTWEIGHT_TIER"
            cost = round(monthly_token_volume * 0.0000002, 2)
        else:
            tier = "BALANCED_PERFORMANCE_TIER"
            cost = round(monthly_token_volume * 0.0000008, 2)
        return {
            "recommended_model_tier": tier,
            "estimated_monthly_cost_usd": cost,
            "savings_vs_current_usd": round(cost * 0.35, 2)
        }
