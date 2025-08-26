from fastapi.testclient import TestClient

from trader.app.main import app


client = TestClient(app)


def test_decision_endpoint() -> None:
	resp = client.get("/decision")
	assert resp.status_code == 200
	body = resp.json()
	assert body["signal"] in {"buy", "sell", "hold"}


def test_ticker_endpoint() -> None:
	resp = client.get("/ticker/mexc/BTCUSDT")
	assert resp.status_code == 200
	data = resp.json()
	assert data["symbol"] == "BTCUSDT"
	assert "price" in data


def test_mcp_health_endpoint() -> None:
	resp = client.get("/mcp/health")
	assert resp.status_code == 200
	data = resp.json()
	assert "context7" in data and "sequential" in data and "playwright" in data
	assert data["context7"]["ok"] is True
	assert data["sequential"]["ok"] is True
	assert data["playwright"]["ok"] is True


def test_metrics_endpoint() -> None:
	resp = client.get("/metrics")
	assert resp.status_code == 200
	assert resp.headers["content-type"].startswith("text/plain")
	assert b"process_cpu_seconds_total" in resp.content