from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)


class EventService:
    def accept_event(
        self,
        event: MarketEventCreate,
    ) -> MarketEventAccepted:
        # Later this method will:
        # 1. Check for duplicate events.
        # 2. Publish the event to Kafka.
        # 3. Record metrics and logs.

        return MarketEventAccepted(
            status="accepted",
            event_id=event.event_id,
            symbol=event.symbol,
            event_type=event.event_type,
        )


event_service = EventService()