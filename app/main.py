from contextlib import asynccontextmanager, suppress
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.database import init_db
from app.core.exceptions import register_exception_handlers
from app.dependencies.session import get_session

# Absolute path to static files
STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run once at startup, then yield control until shutdown."""
    try:
        init_db()
    except OperationalError as exc:
        raise RuntimeError(
            f"Failed to initialize database. Check DATABASE_URL in .env: {type(exc).__name__}"
        ) from exc
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Accept"],
)

register_exception_handlers(app)

app.include_router(api_router, prefix="/api/v1")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
async def root() -> FileResponse:
    """Serve the main page"""
    return FileResponse(str(STATIC_DIR / "index.html"))


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint for container orchestration"""
    # Check database connectivity
    try:
        session_gen = get_session()
        session = next(session_gen)
        try:
            session.execute(text("SELECT 1"))
            return {"status": "healthy"}
        finally:
            with suppress(StopIteration):
                next(session_gen)
    except Exception:
        from fastapi import status
        from fastapi.responses import JSONResponse

        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "unhealthy", "detail": "database unreachable"},
        )
