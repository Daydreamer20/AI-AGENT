import asyncio
from typing import Any, Dict

import types

from trader.app.exchanges.mexc import MexcClient
from trader.app.exchanges.bybit import BybitClient


class _MockResponse:
	def __init__(self, json_data: Dict[str, Any]) -> None:
		self._json = json_data

	def json(self) -> Dict[str, Any]:
		return self._json

	def raise_for_status(self) -> None:
		return None


class _MockAsyncClient:
	def __init__(self, response_json: Dict[str, Any]) -> None:
		self._response_json = response_json

	async def __aenter__(self) -> "_MockAsyncClient":
		return self

	async def __aexit__(self, exc_type, exc, tb) -> None:  # type: ignore[no-untyped-def]
		return None

	async def get(self, *_args: Any, **_kwargs: Any) -> _MockResponse:
		return _MockResponse(self._response_json)


def test_mexc_get_ticker_parses_price(monkeypatch) -> None:  # type: ignore[no-untyped-def]
	# Prepare mock AsyncClient returning MEXC payload
	def _mock_async_client_factory(*_args: Any, **_kwargs: Any) -> _MockAsyncClient:
		return _MockAsyncClient({"symbol": "BTCUSDT", "price": "123.45"})

	# Monkeypatch constructor
	import httpx  # local import to patch symbol used in module
	monkeypatch.setattr(httpx, "AsyncClient", _mock_async_client_factory)

	client = MexcClient()
	result = asyncio.run(client.get_ticker("BTCUSDT"))
	assert result["symbol"] == "BTCUSDT"
	assert result["price"] == 123.45


def test_bybit_get_ticker_parses_price(monkeypatch) -> None:  # type: ignore[no-untyped-def]
	bybit_payload = {
		"retCode": 0,
		"result": {
			"list": [
				{
					"symbol": "BTCUSDT",
					"lastPrice": "54321.0",
				}
			]
		}
	}

	def _mock_async_client_factory(*_args: Any, **_kwargs: Any) -> _MockAsyncClient:
		return _MockAsyncClient(bybit_payload)

	import httpx
	monkeypatch.setattr(httpx, "AsyncClient", _mock_async_client_factory)

	client = BybitClient()
	result = asyncio.run(client.get_ticker("BTCUSDT"))
	assert result["symbol"] == "BTCUSDT"
	assert result["price"] == 54321.0