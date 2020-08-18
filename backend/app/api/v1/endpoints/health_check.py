from fastapi import APIRouter
from app import schemas

router = APIRouter()


@router.get("/health-check", response_model=schemas.Message)
def health_check():
    return {"msg": "ok", "content": {}}
