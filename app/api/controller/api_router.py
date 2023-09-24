from fastapi import APIRouter

from app.api.controller.event_router import router as event_router

api_router = APIRouter()

api_router.include_router(event_router, prefix="/events", tags=["events"])
