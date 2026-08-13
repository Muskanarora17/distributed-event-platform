from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from services.ingestion_service.database.models import MarketEventModel
from services.ingestion_service.repositories.base import EventRepository
from services.ingestion_service.schemas.event import MarketEventCreate


class PostgresEventRepository(EventRepository):
    def __init__(self, session: Session):
        self._session = session

    def save(self, event: MarketEventCreate) -> None:
        model = MarketEventModel(
            event_id=event.event_id,
            symbol=event.symbol,
            event_type=event.event_type.value,
            price=event.price,
            volume=event.volume,
            timestamp=event.timestamp,
            exchange=event.exchange.value,
        )

        self._session.add(model)
        self._session.commit()

    def exists(self, event_id: UUID) -> bool:
        statement = select(MarketEventModel.event_id).where(
            MarketEventModel.event_id == event_id
        )

        result = self._session.execute(statement).scalar_one_or_none()

        return result is not None