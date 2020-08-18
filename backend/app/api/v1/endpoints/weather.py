import ujson

from fastapi import APIRouter, Query, HTTPException
from fastapi.encoders import jsonable_encoder

from app import schemas
from app.core.celery import celery
from app.core.config import settings
from app import exceptions
from app.core.redis import redis_client
from app.utils import hash_dict

router = APIRouter()


@router.post("/weather", response_model=schemas.Message, status_code=201)
def process_weather_by_city(city: schemas.CityBase):
    try:
        celery.send_task(settings.CELERY_TASK, args=[jsonable_encoder(city)])
    except Exception as exc:
        raise exceptions.CelerySendTaskException(exc)
    return {"msg": "success", "content": {}}


@router.get("/weather", response_model=schemas.Message)
def get_weather_by_city(
        name: str = Query(
            None,
            alias="name",
            title="City name",
            description="The name of the city",
        ),
        state_code: str = Query(
            None,
            alias="state_code",
            title="state code",
            description="The state code of the city",
        ),
        country_code: str = Query(
            None,
            alias="country_code",
            title="country code",
            description="The country code of the city",
        )
):
    data = {'name': name, 'state_code': state_code, 'country_code': country_code}
    result = redis_client.get(hash_dict(data))
    if not result:
        raise HTTPException(status_code=404, detail="City not found")
    return {"msg": "success", "content": ujson.loads(result)}
