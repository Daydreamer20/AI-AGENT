from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, Optional


class ExchangeClient(ABC):
	"""Abstract base for exchange clients."""

	@abstractmethod
	async def get_ticker(self, symbol: str) -> Dict[str, Any]:
		...

	@abstractmethod
	async def place_order(
		self,
		symbol: str,
		side: str,
		order_type: str,
		quantity: float,
		price: Optional[float] = None,
		**kwargs: Any,
	) -> Dict[str, Any]:
		...

	@abstractmethod
	async def cancel_order(self, symbol: str, order_id: str) -> Dict[str, Any]:
		...

	@abstractmethod
	async def subscribe_ticker(self, symbol: str) -> AsyncIterator[Dict[str, Any]]:
		...