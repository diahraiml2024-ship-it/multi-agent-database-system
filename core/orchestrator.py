from typing import Dict, Any, List
from core.base_agent import BaseAgent


class AgentOrchestrator:
    """
    Responsible for executing agents in sequence.
    """

    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    def run(self, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        data = initial_data

        for agent in self.agents:
            data = agent.execute(data)

        return data