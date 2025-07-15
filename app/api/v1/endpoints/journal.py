from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.database import engine
from app.models.journal import JournalEntry
from app.schemas import JournalCreate, JournalRead

router = APIRouter(
    prefix="/journal",
    tags=["Journal"],  # Swagger grouping
)


def get_session() -> Session:
    """FastAPI dependency that yields a SQLModel session bound to the global engine"""
    with Session(engine) as session:
        yield session


@router.post(
    "",
    response_model=JournalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new journal entry",
    response_description="The created journal entry",
)
def create_journal_entry(
    payload: JournalCreate,
    session: Session = Depends(get_session),
) -> JournalRead:
    """Create a new journal entry"""
    entry = JournalEntry(**payload.model_dump())
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry
