from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, constr

from app.constants import CONTENT_MAX_LENGTH, CONTENT_MIN_LENGTH, MOOD_MAX_LENGTH


class JournalCreate(BaseModel):
    content: constr(min_length=CONTENT_MIN_LENGTH, max_length=CONTENT_MAX_LENGTH) = Field(
        ...,
        description="Main textual content",
        json_schema_extra={"examples": ["Today I felt surprisingly calm and reflective"]},
    )
    mood: constr(max_length=MOOD_MAX_LENGTH) | None = Field(
        default=None,
        description="Mood tag",
    )

    model_config = ConfigDict(str_strip_whitespace=True)


class JournalUpdate(BaseModel):
    content: constr(min_length=CONTENT_MIN_LENGTH, max_length=CONTENT_MAX_LENGTH) | None = Field(
        default=None,
        description="Main textual content",
    )
    mood: constr(max_length=MOOD_MAX_LENGTH) | None = Field(
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
    updated_at: datetime | None = Field(
        default=None,
        description="Timestamp of last modification in UTC",
    )
    mood: str | None = Field(
        default=None,
        description="Mood tag",
    )

    model_config = ConfigDict(from_attributes=True)
