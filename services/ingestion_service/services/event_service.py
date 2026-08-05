import logging

from services.ingestion_service.exceptions import DuplicateEventError
from services.ingestion_service.repositories.base import EventRepository
from services.ingestion_service.repositories.in_memory_event_repository import (
    InMemoryEventRepository,
)
from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)


logger = logging.getLogger(__name__)


class EventService:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def accept_event(
        self,
        event: MarketEventCreate,
    ) -> MarketEventAccepted:
        if self._repository.exists(event.event_id):
            raise DuplicateEventError(event.event_id)

        self._repository.save(event)

        logger.info(
            "event_accepted event_id=%s symbol=%s event_type=%s exchange=%s",
            event.event_id,
            event.symbol,
            event.event_type,
            event.exchange,
        )

        return MarketEventAccepted(
            status="accepted",
            event_id=event.event_id,
            symbol=event.symbol,
            event_type=event.event_type,
        )


event_repository = InMemoryEventRepository()
event_service = EventService(event_repository)