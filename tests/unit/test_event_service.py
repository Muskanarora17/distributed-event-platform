from services.ingestion_service.schemas.event import (
    EventType,
    MarketEventCreate,
)
from services.ingestion_service.services.event_service import EventService


def test_accept_event_returns_accepted_response():
    event = MarketEventCreate(
        event_id="490692a1-bf50-4c87-b0ea-dcde30fd424c",
        symbol="aapl",
        event_type="TRADE",
        price="192.45",
        volume=100,
        timestamp="2026-07-19T18:30:00Z",
        exchange="NASDAQ",
    )

    service = EventService()

    result = service.accept_event(event)

    assert result.status == "accepted"
    assert result.event_id == event.event_id
    assert result.symbol == "AAPL"
    assert result.event_type == EventType.TRADE