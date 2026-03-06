from datetime import UTC, datetime

from sqlmodel import Session, select

from app.models.journal import JournalEntry
from app.schemas.journal import JournalCreate, JournalUpdate


def get_journal_entry(session: Session, entry_id: int) -> JournalEntry | None:
    """Retrieve a single journal entry by ID."""
    return session.get(JournalEntry, entry_id)


def get_journal_entries(session: Session, skip: int = 0, limit: int = 20) -> list[JournalEntry]:
    """Retrieve a paginated list of journal entries."""
    return list(session.exec(select(JournalEntry).offset(skip).limit(limit)).all())


def delete_journal_entry(session: Session, entry: JournalEntry) -> None:
    """Delete a journal entry."""
    session.delete(entry)
    session.commit()


def create_journal_entry(session: Session, data: JournalCreate) -> JournalEntry:
    """Create and persist a new journal entry."""
    entry = JournalEntry(**data.model_dump())
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry


def update_journal_entry(
    session: Session, entry: JournalEntry, data: JournalUpdate
) -> JournalEntry:
    """Update an existing journal entry and set updated_at timestamp."""
    # Explicit whitelist of updatable fields for security
    updatable_fields = {"content", "mood"}
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field in updatable_fields:
            setattr(entry, field, value)
    entry.updated_at = datetime.now(UTC)
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry
