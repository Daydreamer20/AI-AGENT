from typing import Any, AsyncIterator, Dict, Optional

import httpx

from .base import ExchangeClient


class MexcClient(ExchangeClient):
	async def get_ticker(self, symbol: str) -> Dict[str, Any]:
		url = "https://api.mexc.com/api/v3/ticker/price"
		try:
			async with httpx.AsyncClient(timeout=5.0) as client:
				resp = await client.get(url, params={"symbol": symbol})
				resp.raise_for_status()
				data = resp.json()
				price_str = data.get("price")
				price = float(price_str) if price_str is not None else None
				return {"symbol": symbol, "price": price}
		except Exception:
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