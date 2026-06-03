"""Tests de humo. Verifican que la app arranca y responde."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_openapi_disponible():
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    assert "/auth/register" in resp.json()["paths"]
    assert "/accounts" in resp.json()["paths"]
