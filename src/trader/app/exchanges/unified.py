from typing import Literal

from .bybit import BybitClient
from .mexc import MexcClient
from .base import ExchangeClient


ExchangeName = Literal["mexc", "bybit"]


def get_exchange_client(name: ExchangeName) -> ExchangeClient:
	if name == "mexc":
		return MexcClient()
	if name == "bybit":
		return BybitClient()
	raise ValueError(f"Unsupported exchange: {name}")