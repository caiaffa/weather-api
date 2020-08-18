from fastapi import APIRouter
from app import schemas

router = APIRouter()


@router.post("/weather", response_model=schemas.Message)
def search_weather(city: schemas.ItemCreate):
    return {"msg": "ok"}
