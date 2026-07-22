import logging

from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)


logger = logging.getLogger(__name__)


class EventService:
    def accept_event(
        self,
        event: MarketEventCreate,
    ) -> MarketEventAccepted:
        logger.info(
            "event_accepted event_id=%s symbol=%s event_type=%s "
            "exchange=%s",
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


event_service = EventService()