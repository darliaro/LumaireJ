from sqlmodel import SQLModel, create_engine
from app.core.config import settings
from app import models  # noqa: F401

engine = create_engine(settings.database_url, echo=settings.debug)


def init_db() -> None:
    """Create all tables (run once at startup)."""
    SQLModel.metadata.create_all(engine)
