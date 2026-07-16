from fastapi import FastAPI

app = FastAPI(
    title="Distributed Event Processing Platform",
    description="Backend platform for processing financial events",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "ingestion-service"
    }