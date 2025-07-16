from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class JournalEntry(SQLModel, table=True):
    __tablename__ = "journal_entries"

    id: int | None = Field(primary_key=True, description="Unique identifier for the journal entry")
    content: str = Field(
        min_length=1,
        max_length=5000,
        description="Main textual content written by the user",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp of entry creation in UTC",
    )
    mood: str | None = Field(description="Optional mood tag")
