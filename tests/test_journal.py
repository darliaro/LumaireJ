import pytest
from pydantic import ValidationError
from sqlmodel import Session

from app.crud.journal import (
    create_journal_entry,
    delete_journal_entry,
    get_journal_entries,
    get_journal_entry,
    update_journal_entry,
)
from app.schemas import JournalCreate, JournalUpdate

# --- CRUD Layer Tests --- #


def test_create_journal_entry_with_valid_data(test_session: Session):
    """Test that a valid journal entry is successfully created and persisted."""

    payload = JournalCreate(content="Test entry")  # Arrange
    entry = create_journal_entry(test_session, payload)  # Act

    assert entry.id is not None, "Expected ID to be set after commit"  # Assert
    assert entry.content == "Test entry", f"Expected content='Test entry', got '{entry.content}'"
    assert entry.mood is None, f"Expected mood to default to None, got '{entry.mood}'"
    assert hasattr(entry, "created_at"), "Missing 'created_at' attribute"


def test_get_journal_entry_returns_entry(test_session: Session):
    entry = create_journal_entry(test_session, JournalCreate(content="Hello"))
    fetched = get_journal_entry(test_session, entry.id)
    assert fetched is not None
    assert fetched.id == entry.id
    assert fetched.content == "Hello"


def test_get_journal_entry_returns_none_for_missing(test_session: Session):
    result = get_journal_entry(test_session, 9999)
    assert result is None


def test_get_journal_entries_returns_list(test_session: Session):
    create_journal_entry(test_session, JournalCreate(content="Entry 1"))
    create_journal_entry(test_session, JournalCreate(content="Entry 2"))
    entries = get_journal_entries(test_session)
    assert len(entries) == 2


def test_get_journal_entries_pagination(test_session: Session):
    for i in range(5):
        create_journal_entry(test_session, JournalCreate(content=f"Entry {i}"))
    page = get_journal_entries(test_session, skip=2, limit=2)
    assert len(page) == 2


def test_update_journal_entry(test_session: Session):
    entry = create_journal_entry(test_session, JournalCreate(content="Original"))
    updated = update_journal_entry(test_session, entry, JournalUpdate(content="Updated", mood="happy"))
    assert updated.content == "Updated"
    assert updated.mood == "happy"
    assert updated.updated_at is not None


def test_delete_journal_entry(test_session: Session):
    entry = create_journal_entry(test_session, JournalCreate(content="To delete"))
    entry_id = entry.id
    delete_journal_entry(test_session, entry)
    assert get_journal_entry(test_session, entry_id) is None


# --- Schema Validation Tests --- #


def test_journal_create_with_empty_content_raises_validation_error():
    """Test that verifies that creating a JournalCreate object with empty content raises a ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="")

    assert "at least 1 character" in str(exc_info.value)
