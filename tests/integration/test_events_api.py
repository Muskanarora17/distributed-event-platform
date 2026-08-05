from uuid import uuid4

from fastapi.testclient import TestClient

from services.ingestion_service.main import app


client = TestClient(app)


def create_event_payload() -> dict:
    return {
        "event_id": str(uuid4()),
        "symbol": "aapl",
        "event_type": "TRADE",
        "price": "192.45",
        "volume": 100,
        "timestamp": "2026-07-19T18:30:00Z",
        "exchange": "NASDAQ",
    }


def test_create_event_returns_accepted():
    payload = create_event_payload()

    response = client.post(
        "/api/v1/events",
        json=payload,
    )

    assert response.status_code == 202

    response_body = response.json()

    assert response_body["status"] == "accepted"
    assert response_body["event_id"] == payload["event_id"]
    assert response_body["symbol"] == "AAPL"
    assert response_body["event_type"] == "TRADE"


def test_duplicate_event_returns_conflict():
    payload = create_event_payload()

    first_response = client.post(
        "/api/v1/events",
        json=payload,
    )
    second_response = client.post(
        "/api/v1/events",
        json=payload,
    )

    assert first_response.status_code == 202
    assert second_response.status_code == 409
    assert "already exists" in second_response.json()["detail"]