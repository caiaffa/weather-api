import secrets

from starlette.config import Config
from pydantic import BaseSettings


class Settings(BaseSettings):
    config = Config()

    CELERY_BROKER: str = config("CELERY_BROKER", default="amqp://guest@rabbit//")
    CELERY_TASK: str = config("CELERY_TASK", default="app.worker.weather_celery")
    CELERY_QUEUE: str = config("CELERY_QUEUE", default="weather_queue")

    OPEN_WEATHER_HOST: str = config("OPEN_WEATHER_HOST", default="http://api.openweathermap.org")
    OPEN_WEATHER_KEY: str = config("OPEN_WEATHER_KEY", default="eb8b1a9405e659b2ffc78f0a520b1a46")
    OPEN_WEATHER_RETRIES: int = config("OPEN_WEATHER_RETRIES", default=3)

    CONNECT_TIMEOUT: float = config("CONNECT_TIMEOUT", default=5.0)
    READ_TIMEOUT: float = config("READ_TIMEOUT", default=10.0)

    REDIS_HOST: str = config("REDIS_HOST", default="redis")
    REDIS_PORT: int = config("REDIS_PORT", default=6379)
    REDIS_PASSWORD: str = config("REDIS_PASSWORD", default="")


settings = Settings()
