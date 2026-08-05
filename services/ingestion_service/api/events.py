from fastapi import APIRouter, HTTPException, status

from services.ingestion_service.exceptions import DuplicateEventError
from services.ingestion_service.schemas.event import (
    MarketEventAccepted,
    MarketEventCreate,
)
from services.ingestion_service.services.event_service import event_service


router = APIRouter(
    prefix="/api/v1/events",
    tags=["events"],
)


@router.post(
    "",
    response_model=MarketEventAccepted,
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_event(
    event: MarketEventCreate,
) -> MarketEventAccepted:
    try:
        return event_service.accept_event(event)
    except DuplicateEventError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc