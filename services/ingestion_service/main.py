from fastapi import FastAPI

from services.ingestion_service.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment
    }