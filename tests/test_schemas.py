"""Unit tests for schema validation."""

import pytest
from pydantic import ValidationError

from app.schemas.journal import JournalCreate, JournalUpdate

# --- JournalCreate Tests ---


def test_journal_create_with_valid_content():
    """Test creating JournalCreate with valid content."""
    payload = JournalCreate(content="Valid content")
    assert payload.content == "Valid content"
    assert payload.mood is None


def test_journal_create_with_mood():
    """Test creating JournalCreate with mood value."""
    payload = JournalCreate(content="Test entry", mood="happy")
    assert payload.content == "Test entry"
    assert payload.mood == "happy"


def test_journal_create_strips_whitespace():
    """Test that str_strip_whitespace config works."""
    payload = JournalCreate(content="  Test entry  ", mood="  happy  ")
    assert payload.content == "Test entry"
    assert payload.mood == "happy"


def test_journal_create_empty_content_raises_error():
    """Test that empty content raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="")

    errors = exc_info.value.errors()
    assert any("content" in str(error["loc"]) for error in errors)


def test_journal_create_whitespace_only_content_raises_error():
    """Test that whitespace-only content raises ValidationError after stripping."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="   ")

    errors = exc_info.value.errors()
    assert any("content" in str(error["loc"]) for error in errors)


def test_journal_create_content_exceeding_max_length_raises_error():
    """Test that content exceeding 5000 chars raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="x" * 5001)

    errors = exc_info.value.errors()
    assert any("content" in str(error["loc"]) for error in errors)


def test_journal_create_content_at_max_length_succeeds():
    """Test that content at exactly 5000 chars is valid."""
    payload = JournalCreate(content="x" * 5000)
    assert len(payload.content) == 5000


def test_journal_create_content_at_min_length_succeeds():
    """Test that content at exactly 1 char is valid."""
    payload = JournalCreate(content="x")
    assert payload.content == "x"


def test_journal_create_mood_exceeding_max_length_raises_error():
    """Test that mood exceeding 50 chars raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JournalCreate(content="valid", mood="x" * 51)

    errors = exc_info.value.errors()
    assert any("mood" in str(error["loc"]) for error in errors)


def test_journal_create_empty_mood_converts_to_none():
    """Test that empty mood string is converted to None."""
    payload = JournalCreate(content="valid", mood="")
    assert payload.mood is None


def test_journal_create_whitespace_mood_converts_to_none():
    """Test that whitespace-only mood is converted to None."""
    payload = JournalCreate(content="valid", mood="   ")
    assert payload.mood is None


# --- JournalUpdate Tests ---


def test_journal_update_all_fields_optional():
    """Test that all fields are optional in JournalUpdate."""
    payload = JournalUpdate()
    assert payload.content is None
    assert payload.mood is None


def test_journal_update_content_validation_applies():
    """Test that content validation constraints apply to updates."""
    with pytest.raises(ValidationError):
        JournalUpdate(content="")


def test_journal_update_mood_validation_applies():
    """Test that mood length validation applies to updates."""
    with pytest.raises(ValidationError):
        JournalUpdate(mood="x" * 51)


def test_journal_update_partial_update_content_only():
    """Test partial update with only content."""
    payload = JournalUpdate(content="Updated content")
    assert payload.content == "Updated content"
    assert payload.mood is None


def test_journal_update_partial_update_mood_only():
    """Test partial update with only mood."""
    payload = JournalUpdate(mood="sad")
    assert payload.content is None
    assert payload.mood == "sad"


def test_journal_update_empty_mood_converts_to_none():
    """Test that empty mood in update converts to None."""
    payload = JournalUpdate(mood="")
    assert payload.mood is None
