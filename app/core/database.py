from sqlmodel import SQLModel, create_engine

from app import models  # noqa: F401
from app.core.config import settings

# Note: echo=False to avoid logging user data in SQL queries
# For SQL debugging, set a separate environment variable if needed
engine = create_engine(settings.database_url, echo=False)


def init_db() -> None:
    """Create all tables (run once at startup)."""
    SQLModel.metadata.create_all(engine)
