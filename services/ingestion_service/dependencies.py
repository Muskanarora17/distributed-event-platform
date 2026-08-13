from fastapi import Depends
from sqlalchemy.orm import Session

from services.ingestion_service.database.connection import get_database_session
from services.ingestion_service.repositories.postgres_event_repository import (
    PostgresEventRepository,
)
from services.ingestion_service.services.event_service import EventService


def get_event_service(
    session: Session = Depends(get_database_session),
) -> EventService:
    repository = PostgresEventRepository(session)
    return EventService(repository)