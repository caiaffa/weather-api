import secrets
from typing import List

from starlette.config import Config
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    config = Config()

    API_V1: str = "/api/v1"
    SECRET_KEY: str = config("SECRET_KEY", default=secrets.token_urlsafe(32))
    PROJECT_NAME: str = config("PROJECT_NAME", default="api")
    CORS_ORIGINS = config("CORS_HOSTS", default=['*'])


settings = Settings()
