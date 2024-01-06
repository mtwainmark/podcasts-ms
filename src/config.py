from typing import Any

from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.constants import Environment


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"



settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"