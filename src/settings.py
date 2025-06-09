from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///../data/legal_db.sqlite"
    OPENAI_API_KEY: str | None = None
    GOOGLE_SERVICE_ACCOUNT_JSON: str | None = None
    MINIO_ENDPOINT: str | None = None
    MINIO_ACCESS_KEY: str | None = None
    MINIO_SECRET_KEY: str | None = None
    REDIS_URL: str = "redis://redis:6379/0"
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
