from uuid import UUID

from services.ingestion_service.repositories.base import EventRepository
from services.ingestion_service.schemas.event import MarketEventCreate


class InMemoryEventRepository(EventRepository):
    def __init__(self):
        self._events: dict[UUID, MarketEventCreate] = {}

    def save(self, event: MarketEventCreate) -> None:
        self._events[event.event_id] = event

    def exists(self, event_id: UUID) -> bool:
        return event_id in self._events