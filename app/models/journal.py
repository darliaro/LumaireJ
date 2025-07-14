from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class JournalEntry(SQLModel, table=True):
    __tablename__ = "journal_entries"

    id: int | None = Field(
        primary_key=True, description="Unique identifier for the journal entry"
    )
    content: str = Field(
        min_length=1,
        max_length=5000,
        description="Main textual content written by the user",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp of entry creation in UTC",
    )
    mood: str | None = Field(description="Optional mood tag")
    user_id: int | None = Field(
        description="Reference to the user who owns the entry",
    )
