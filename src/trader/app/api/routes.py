from fastapi import APIRouter

from ..config.settings import get_settings
from ..ai.decision_engine import decide
from ..exchanges.unified import get_exchange_client, ExchangeName
from ..mcp.context7 import Context7Client
from ..mcp.sequential import SequentialClient
from ..mcp.playwright_client import PlaywrightMCPClient
from prometheus_client import CollectorRegistry, CONTENT_TYPE_LATEST, generate_latest
from fastapi import Response

router = APIRouter()
settings = get_settings()


@router.get("/health")
def health() -> dict:
	return {"status": "ok", "version": settings.version}


@router.get("/config")
def get_config() -> dict:
	return settings.safe_dict()


@router.get("/decision")
def decision() -> dict:
	return {"signal": decide()}


@router.get("/ticker/{exchange}/{symbol}")
async def ticker(exchange: ExchangeName, symbol: str) -> dict:
	client = get_exchange_client(exchange)
	return await client.get_ticker(symbol)


@router.get("/mcp/health")
async def mcp_health() -> dict:
	ctx = Context7Client(base_url=settings.context7_url)
	seq = SequentialClient(base_url=settings.sequential_url)
	pw = PlaywrightMCPClient(base_url=settings.playwright_url)
	return {
		"context7": await ctx.ping(),
		"sequential": await seq.ping(),
		"playwright": await pw.ping(),
	}


@router.get("/metrics")
def metrics() -> Response:
	# Expose default process metrics. Using default registry implicitly inside generate_latest
	content = generate_latest()
	return Response(content=content, media_type=CONTENT_TYPE_LATEST)