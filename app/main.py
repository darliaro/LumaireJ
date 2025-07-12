from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="LumaireJ",
    description="A journaling app for emotional self-awareness and reflection",
    version="0.1.0",
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


@app.get("/health")
def health_check() -> dict:
    """
    Health check endpoint.
    Returns a JSON response confirming the app is running and includes its version.
    """
    return {"status": "healthy", "version": app.version}
