from fastapi.testclient import TestClient

from services.ingestion_service.main import app


client = TestClient(app)


def test_response_contains_request_id():
    response = client.get("/health")

    assert response.status_code == 200
    assert "X-Request-ID" in response.headers


def test_existing_request_id_is_preserved():
    response = client.get(
        "/health",
        headers={"X-Request-ID": "test-request-123"},
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "test-request-123"