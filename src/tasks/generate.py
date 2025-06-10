from celery import Celery
from src.settings_loader import get_settings
from src.adapters.template_engine import render
from src.adapters.minio_client import upload

settings = get_settings()
celery_app = Celery("legal_core", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery_app.task
def generate_contract_task(client: dict, template_name: str):
    path = render(template_name, {"client": client})
    return {"url": upload(path), "filename": path.name}

@celery_app.task
def generate_lawsuit_task(case: dict, template_name: str):
    path = render(template_name, {"case": case})
    return {"url": upload(path), "filename": path.name}