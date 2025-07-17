import pytest
from pydantic import ValidationError
from sqlmodel import Session

from app.crud.journal import create_journal_entry
from app.schemas import JournalCreate

# --- CRUD Layer Tests --- #


def test_create_journal_entry_with_valid_data(test_session: Session):
    """Test that a valid journal entry is successfully created and persisted."""

    payload = JournalCreate(content="Test entry")  # Arrange
    entry = create_journal_entry(test_session, payload)  # Act

    assert entry.id is not None, "Expected ID to be set after commit"  # Assert
    assert entry.content == "Test entry", f"Expected content='Test entry', got '{entry.content}'"
    assert entry.mood is None, f"Expected mood to default to None, got '{entry.mood}'"
    assert hasattr(entry, "created_at"), "Missing 'created_at' attribute"


# --- Schema Validation Tests --- #


def test_journal_create_with_empty_content_raises_validation_error():
    """Test that verifies that creating a JournalCreate object with empty content raises a ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="")

    assert "at least 1 character" in str(exc_info.value)
