import secrets

from starlette.config import Config
from pydantic import BaseSettings


class Settings(BaseSettings):
    config = Config()

    API_V1: str = "/api/v1"
    SECRET_KEY: str = config("SECRET_KEY", default=secrets.token_urlsafe(32))
    PROJECT_NAME: str = config("PROJECT_NAME", default="api")
    CORS_ORIGINS = config("CORS_HOSTS", default=['*'])

    CELERY_BROKER: str = config("CELERY_BROKER", default="amqp://guest@rabbit//")
    CELERY_TASK: str = config("CELERY_TASK", default="app.worker.weather_consumer")
    CELERY_QUEUE: str = config("CELERY_QUEUE", default="weather_queue")

    REDIS_HOST: str = config("REDIS_HOST", default="redis")
    REDIS_PORT: int = config("REDIS_PORT", default=6379)
    REDIS_PASSWORD: str = config("REDIS_PASSWORD", default="")


settings = Settings()
