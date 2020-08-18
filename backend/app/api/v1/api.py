from fastapi import APIRouter

from app.api.v1.endpoints import health_check, weather

api_router = APIRouter()
api_router.include_router(health_check.router, tags=["health"])
api_router.include_router(weather.router, tags=["weather"])

