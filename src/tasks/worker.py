from celery import Celery
from ..settings_loader import get_settings
settings = get_settings()

celery_app = Celery(
    "symbios_legal_core",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

@celery_app.task
def ping():
    return "pong"
