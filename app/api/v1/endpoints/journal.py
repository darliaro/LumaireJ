from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.crud.journal import create_journal_entry
from app.dependencies.session import get_session
from app.schemas import JournalCreate, JournalRead

router = APIRouter(
    prefix="/journal",
    tags=["Journal"],
)


@router.post(
    "",
    response_model=JournalRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new journal entry",
    response_description="The created journal entry",
)
def post_journal_entry(
    payload: JournalCreate,
    session: Annotated[Session, Depends(get_session)],
) -> JournalRead:
    """Create a new journal entry"""
    return create_journal_entry(session, payload)
