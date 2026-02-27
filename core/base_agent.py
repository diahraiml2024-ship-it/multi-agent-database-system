from abc import ABC, abstractmethod
from typing import Any, Dict
import logging


class BaseAgent(ABC):
    """
    Abstract Base Class for all agents.
    Every agent must implement the execute method.
    """

    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(self.name)

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent logic.
        Must return updated data dictionary.
        """
        pass