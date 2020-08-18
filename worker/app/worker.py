import ujson

from celery.utils.log import get_task_logger

from app.core.celery import celery
from app.core.config import settings
from app import exceptions
from app.clients.open_weather_client import weather_client
from app.core.redis import redis_client
from app.utils import hash_dict

logger = get_task_logger(__name__)


@celery.task(
    acks_late=True, serializer='json',
    autoretry_for=(exceptions.OpenWeatherClientException,), retry_kwargs={'max_retries': settings.OPEN_WEATHER_RETRIES}
)
def weather_consumer(message: dict):
    logger.info(f'Received message: {message}')
    result = weather_client.current_weather(message)
    redis_client.set(hash_dict(message), ujson.dumps(result))

