from sqlmodel import Session

from app.models.journal import JournalEntry
from app.schemas import JournalCreate


def create_journal_entry(session: Session, data: JournalCreate) -> JournalEntry:
    """Create and persist a new journal entry."""
    entry = JournalEntry(**data.model_dump())
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry
