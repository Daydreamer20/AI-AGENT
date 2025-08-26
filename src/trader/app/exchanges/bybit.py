from typing import Any, AsyncIterator, Dict, Optional

import httpx

from .base import ExchangeClient


class BybitClient(ExchangeClient):
	async def get_ticker(self, symbol: str) -> Dict[str, Any]:
		url = "https://api.bybit.com/v5/market/tickers"
		params = {"category": "spot", "symbol": symbol}
		try:
			async with httpx.AsyncClient(timeout=5.0) as client:
				resp = await client.get(url, params=params)
				resp.raise_for_status()
				payload = resp.json()
				items = (payload.get("result") or {}).get("list") or []
				last_price_str = items[0].get("lastPrice") if items else None
				price = float(last_price_str) if last_price_str is not None else None
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