from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator

from app.constants import CONTENT_MAX_LENGTH, CONTENT_MIN_LENGTH, MOOD_MAX_LENGTH


class JournalCreate(BaseModel):
    content: str = Field(
        ...,
        min_length=CONTENT_MIN_LENGTH,
        max_length=CONTENT_MAX_LENGTH,
        description="Main textual content",
        json_schema_extra={"examples": ["Today I felt surprisingly calm and reflective"]},
    )
    mood: str | None = Field(
        default=None,
        min_length=1,  # Prevent empty strings
        max_length=MOOD_MAX_LENGTH,
        description="Mood tag",
    )

    @field_validator("mood", mode="before")
    @classmethod
    def convert_empty_mood_to_none(cls, v: str | None) -> str | None:
        """Convert empty or whitespace-only mood strings to None."""
        if v is not None and not v.strip():
            return None
        return v

    model_config = ConfigDict(str_strip_whitespace=True)


class JournalUpdate(BaseModel):
    content: str | None = Field(
        default=None,
        min_length=CONTENT_MIN_LENGTH,
        max_length=CONTENT_MAX_LENGTH,
        description="Main textual content",
    )
    mood: str | None = Field(
        default=None,
        min_length=1,  # Prevent empty strings
        max_length=MOOD_MAX_LENGTH,
        description="Mood tag",
    )

    @field_validator("mood", mode="before")
    @classmethod
    def convert_empty_mood_to_none(cls, v: str | None) -> str | None:
        """Convert empty or whitespace-only mood strings to None."""
        if v is not None and not v.strip():
            return None
        return v

    model_config = ConfigDict(str_strip_whitespace=True)


class JournalRead(BaseModel):
    id: PositiveInt = Field(
        ...,
        description="ID of the journal entry",
    )
    content: str = Field(
        ...,
        description="Main textual content",
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp of entry creation in UTC",
    )
    updated_at: datetime | None = Field(
        default=None,
        description="Timestamp of last modification in UTC",
    )
    mood: str | None = Field(
        default=None,
        description="Mood tag",
    )

    model_config = ConfigDict(from_attributes=True)
