from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, constr


class JournalCreate(BaseModel):
    content: constr(strip_whitespace=True, min_length=1, max_length=5000) = Field(
        ...,
        description="Main textual content",
        example="Today I felt surprisingly calm and reflective",
    )
    mood: constr(strip_whitespace=True, max_length=50) | None = Field(
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
