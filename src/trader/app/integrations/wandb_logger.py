from typing import Any, Dict


class WandbLogger:
	def __init__(self, project: str = "ai-trading-agent") -> None:
		self.project = project
		self.enabled = False

	def init(self) -> None:
		self.enabled = True

	def log(self, data: Dict[str, Any]) -> None:
		if self.enabled:
			pass