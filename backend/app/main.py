from fastapi import FastAPI
from app.api.facility import router as facility_router


app = FastAPI(
    title="Healthcare Resource Intelligence API",
    version="1.0.0"
)

app.include_router(facility_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Healthcare Resource Intelligence API"
    }