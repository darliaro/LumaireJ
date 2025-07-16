from fastapi import APIRouter

from app.api.v1.endpoints import journal

api_router = APIRouter()

api_router.include_router(journal.router)
