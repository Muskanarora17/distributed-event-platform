from fastapi import FastAPI

from services.ingestion_service.api.events import router as events_router
from services.ingestion_service.api.health import router as health_router
from services.ingestion_service.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(events_router)