from typing import Dict, Any
from core.base_agent import BaseAgent


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent")

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        user_query = data.get("query")

        # Simple intent extraction (placeholder for LLM later)
        plan = {
            "intent": "database_query",
            "original_query": user_query,
            "steps": [
                "analyze_schema",
                "generate_sql",
                "optimize_query",
                "execute_query",
                "validate_results",
                "format_response"
            ]
        }

        data["plan"] = plan
        return data
    