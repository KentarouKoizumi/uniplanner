from fastapi import APIRouter

from app.api.controller.plan_router import router as plan_router

api_router = APIRouter()

api_router.include_router(plan_router, prefix="/plans", tags=["plans"])
