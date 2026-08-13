from fastapi import APIRouter, Depends, HTTPException, status

from services.ingestion_service.dependencies import get_event_service
from services.ingestion_service.exceptions import DuplicateEventError
from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)
from services.ingestion_service.services.event_service import EventService


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
    service: EventService = Depends(get_event_service),
) -> MarketEventAccepted:
    try:
        return service.accept_event(event)
    except DuplicateEventError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc