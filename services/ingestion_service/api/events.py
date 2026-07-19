from fastapi import APIRouter, status

from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)
from services.ingestion_service.services.event_service import event_service


router = APIRouter(
    prefix="/api/v1/events",
    tags=["Events"],
)


@router.post(
    "",
    response_model=MarketEventAccepted,
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_event(
    event: MarketEventCreate,
) -> MarketEventAccepted:
    return event_service.accept_event(event)