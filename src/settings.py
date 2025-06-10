from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # === базове ===
    ENV: str = "dev"
    DATABASE_URL: str = "sqlite:///../data/legal_db.sqlite"
    OPENAI_API_KEY: str | None = None

    # === registry / ODB ===
    OPENDATABOT_TOKEN: str | None = None

    # === MinIO / S3 ===
    MINIO_ENDPOINT: str | None = None
    MINIO_ACCESS_KEY: str | None = None
    MINIO_SECRET_KEY: str | None = None

    # === Redis ===
    REDIS_URL: str = "redis://redis:6379/0"

    # === SMTP / IMAP (Gmail) ===
    SMTP_HOST: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASS: str | None = None
    SMTP_FROM: str | None = None

    IMAP_HOST: str | None = None
    IMAP_PORT: int | None = None
    IMAP_USER: str | None = None
    IMAP_PASS: str | None = None
    IMAP_BOX: str = "INBOX"

    model_config = SettingsConfigDict(env_file=".env")  # ← читаємо .env

@lru_cache
def get_settings() -> Settings:
    return Settings()