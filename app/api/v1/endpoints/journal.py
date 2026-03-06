from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session

from app.crud.journal import (
    create_journal_entry,
    delete_journal_entry,
    get_journal_entries,
    get_journal_entry,
    update_journal_entry,
)
from app.dependencies.session import get_session
from app.schemas import JournalCreate, JournalRead, JournalUpdate

router = APIRouter(
    prefix="/journal",
    tags=["Journal"],
)


@router.get(
    "",
    response_model=list[JournalRead],
    summary="List journal entries",
    response_description="Paginated list of journal entries",
)
def list_journal_entries(
    session: Annotated[Session, Depends(get_session)],
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> list[JournalRead]:
    """Return a paginated list of journal entries."""
    return get_journal_entries(session, skip=skip, limit=limit)


@router.get(
    "/{entry_id}",
    response_model=JournalRead,
    summary="Get a journal entry",
    response_description="The requested journal entry",
)
def get_journal_entry_endpoint(
    entry_id: int,
    session: Annotated[Session, Depends(get_session)],
) -> JournalRead:
    """Return a single journal entry by ID."""
    entry = get_journal_entry(session, entry_id)
    if entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found")
    return entry


@router.patch(
    "/{entry_id}",
    response_model=JournalRead,
    summary="Update a journal entry",
    response_description="The updated journal entry",
)
def patch_journal_entry(
    entry_id: int,
    payload: JournalUpdate,
    session: Annotated[Session, Depends(get_session)],
) -> JournalRead:
    """Update an existing journal entry."""
    entry = get_journal_entry(session, entry_id)
    if entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found")
    return update_journal_entry(session, entry, payload)


@router.delete(
    "/{entry_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a journal entry",
)
def delete_journal_entry_endpoint(
    entry_id: int,
    session: Annotated[Session, Depends(get_session)],
) -> None:
    """Delete a journal entry by ID."""
    entry = get_journal_entry(session, entry_id)
    if entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journal entry not found")
    delete_journal_entry(session, entry)


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
