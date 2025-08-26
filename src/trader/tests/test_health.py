from fastapi.testclient import TestClient

from trader.app.main import app


def test_health() -> None:
	client = TestClient(app)
	resp = client.get("/health")
	assert resp.status_code == 200
	body = resp.json()
	assert body["status"] == "ok"
	assert "version" in body


def test_config_has_no_password() -> None:
	client = TestClient(app)
	resp = client.get("/config")
	assert resp.status_code == 200
	cfg = resp.json()
	assert "postgres_password" not in cfg