"""Configuración de la aplicación, leída desde variables de entorno."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    app_debug: bool = True

    database_url: str = "postgresql+psycopg://banco:banco@db:5432/core_bancario"
    redis_url: str = "redis://cache:6379/0"

    # Default solo para arranque local; en cualquier entorno real se inyecta por env.
    jwt_secret: str = "dev-secret-cambiar"  # noqa: S105
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15


settings = Settings()
