# src/adapters/minio_client.py
import time
from pathlib import Path
from minio import Minio
from minio.error import S3Error
from datetime import timedelta
from src.settings_loader import get_settings  # noqa:F401

settings = get_settings()
BUCKET = "legal-core"

def get_minio_client(retries=5, delay=2):
    endpoint = settings.MINIO_ENDPOINT.replace("http://", "")
    client = Minio(
        endpoint,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_ENDPOINT.startswith("https")
    )
    # спробуємо створити бакет із повторами
    for _ in range(retries):
        try:
            if not client.bucket_exists(BUCKET):
                client.make_bucket(BUCKET)
            break
        except S3Error:
            time.sleep(delay)
    return client

def upload(path: Path) -> str:
    client = get_minio_client()
    # завантажуємо й повертаємо presigned URL
    client.fput_object(BUCKET, path.name, str(path))
    return client.presigned_get_object(BUCKET, path.name, expires=timedelta(hours=1))