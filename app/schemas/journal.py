from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, constr, PositiveInt


class JournalCreate(BaseModel):
    content: constr(strip_whitespace=True, min_length=1, max_length=5000) = Field(
        ...,
        description="Main textual content written by the user",
        example="Today I felt surprisingly calm and reflective",
    )
    mood: str | None = Field(
        default=None,
        max_length=50,
        description="Optional mood tag",
    )

    model_config = ConfigDict(str_strip_whitespace=True)


class JournalRead(BaseModel):
    id: PositiveInt = Field(
        ...,
        description="Unique identifier of the journal entry",
    )
    content: str = Field(
        ...,
        description="Main textual content written by the user",
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp of entry creation, stored in UTC",
    )
    mood: str | None = Field(
        default=None,
        description="Optional mood tag",
    )

    model_config = ConfigDict(from_attributes=True)
