from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, constr

from app.constants import CONTENT_MAX_LENGTH, CONTENT_MIN_LENGTH, MOOD_MAX_LENGTH


class JournalCreate(BaseModel):
    content: constr(strip_whitespace=True, min_length=CONTENT_MIN_LENGTH, max_length=CONTENT_MAX_LENGTH) = Field(
        ...,
        description="Main textual content",
        example="Today I felt surprisingly calm and reflective",
    )
    mood: constr(strip_whitespace=True, max_length=MOOD_MAX_LENGTH) | None = Field(
        default=None,
        description="Mood tag",
    )

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
    mood: str | None = Field(
        default=None,
        description="Mood tag",
    )

    model_config = ConfigDict(from_attributes=True)
