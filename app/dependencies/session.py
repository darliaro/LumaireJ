from collections.abc import Iterator

from sqlmodel import Session

from app.core.database import engine


def get_session() -> Iterator[Session]:
    """FastAPI dependency that yields a SQLModel session bound to the global engine"""
    with Session(engine) as session:
        yield session
