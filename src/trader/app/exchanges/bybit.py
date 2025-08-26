from typing import Any, AsyncIterator, Dict, Optional

from .base import ExchangeClient


class BybitClient(ExchangeClient):
	async def get_ticker(self, symbol: str) -> Dict[str, Any]:
		return {"symbol": symbol, "price": None}

	async def place_order(
		self,
		symbol: str,
		side: str,
		order_type: str,
		quantity: float,
		price: Optional[float] = None,
		**kwargs: Any,
	) -> Dict[str, Any]:
		return {"status": "submitted", "symbol": symbol}

	async def cancel_order(self, symbol: str, order_id: str) -> Dict[str, Any]:
		return {"status": "cancelled", "order_id": order_id}

	async def subscribe_ticker(self, symbol: str) -> AsyncIterator[Dict[str, Any]]:
		yield {"symbol": symbol, "price": None}