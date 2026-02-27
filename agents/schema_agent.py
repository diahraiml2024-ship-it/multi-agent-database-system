from typing import Dict, Any
from core.base_agent import BaseAgent


class SchemaAgent(BaseAgent):
    """
    Responsible for understanding database structure.
    (For now, mock schema. Later we connect real DB.)
    """

    def __init__(self):
        super().__init__(name="SchemaAgent")

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:

        # Mock schema representation
        schema = {
            "tables": {
                "customers": ["id", "name", "email", "created_at"],
                "orders": ["id", "customer_id", "product_id", "quantity", "order_date"],
                "products": ["id", "name", "category", "price"]
            }
        }

        data["schema"] = schema
        return data