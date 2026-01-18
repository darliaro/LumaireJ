from datetime import UTC, datetime

from sqlmodel import Field, SQLModel

from app.constants import CONTENT_MAX_LENGTH, CONTENT_MIN_LENGTH


class JournalEntry(SQLModel, table=True):
    __tablename__ = "journal_entries"

    id: int | None = Field(primary_key=True, description="Unique identifier for the journal entry")
    content: str = Field(
        min_length=CONTENT_MIN_LENGTH,
        max_length=CONTENT_MAX_LENGTH,
        description="Main textual content written by the user",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp of entry creation in UTC",
    )
    updated_at: datetime | None = Field(
        default=None,
        description="Timestamp of last modification in UTC",
    )
    mood: str | None = Field(default=None, description="Optional mood tag")
