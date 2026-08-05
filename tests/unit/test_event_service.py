import pytest

from services.ingestion_service.exceptions import DuplicateEventError
from services.ingestion_service.repositories.in_memory_event_repository import (
    InMemoryEventRepository,
)
from services.ingestion_service.schemas.event import (
    EventType,
    MarketEventCreate,
)
from services.ingestion_service.services.event_service import EventService


@pytest.fixture
def repository() -> InMemoryEventRepository:
    return InMemoryEventRepository()


@pytest.fixture
def service(
    repository: InMemoryEventRepository,
) -> EventService:
    return EventService(repository)


@pytest.fixture
def event() -> MarketEventCreate:
    return MarketEventCreate(
        event_id="490692a1-bf50-4c87-b0ea-dcde30fd424c",
        symbol="aapl",
        event_type="TRADE",
        price="192.45",
        volume=100,
        timestamp="2026-07-19T18:30:00Z",
        exchange="NASDAQ",
    )


def test_accept_event_returns_accepted_response(
    service: EventService,
    repository: InMemoryEventRepository,
    event: MarketEventCreate,
):
    result = service.accept_event(event)

    assert result.status == "accepted"
    assert result.event_id == event.event_id
    assert result.symbol == "AAPL"
    assert result.event_type == EventType.TRADE
    assert repository.exists(event.event_id)


def test_duplicate_event_raises_error(
    service: EventService,
    event: MarketEventCreate,
):
    service.accept_event(event)

    with pytest.raises(
        DuplicateEventError,
        match="already exists",
    ):
        service.accept_event(event)