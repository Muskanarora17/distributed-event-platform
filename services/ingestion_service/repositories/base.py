from abc import ABC, abstractmethod
from uuid import UUID

from services.ingestion_service.schemas.event import MarketEventCreate


class EventRepository(ABC):
    @abstractmethod
    def save(self, event: MarketEventCreate) -> None:
        """Persist an event."""
        raise NotImplementedError

    @abstractmethod
    def exists(self, event_id: UUID) -> bool:
        """Return True if the event already exists."""
        raise NotImplementedError