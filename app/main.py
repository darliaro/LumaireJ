from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.config import settings
from app.core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run once at startup, then yield control until shutdown."""
    init_db()
    yield


app = FastAPI(
    title="LumaireJ",
    description="A journaling app for emotional self-awareness and reflection",
    version="0.1.0",
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)


@app.get("/health")
def health_check() -> dict:
    """Basic heartbeat endpoint."""
    return {"status": "healthy", "version": app.version}
