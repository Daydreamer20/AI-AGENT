from typing import Any, Dict, List


class MarketDataIngestor:
	def __init__(self) -> None:
		self.subscriptions: List[str] = []

	def subscribe(self, symbol: str) -> None:
		self.subscriptions.append(symbol)

	def latest(self, symbol: str) -> Dict[str, Any]:
		return {"symbol": symbol, "price": None}