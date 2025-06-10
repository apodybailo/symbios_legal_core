from celery import Celery
from sqlmodel import Session
from src.settings_loader import get_settings
from src.adapters.email_gmail import list_message_ids, fetch_message, extract_body
from src.adapters.db.session import engine
from src.core.entities.email import Email  # додай entity

settings = get_settings()
celery_app = Celery("email_sync", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery_app.task
def sync_inbox(q: str = ""):
    ids = list_message_ids(q=q, limit=50)
    with Session(engine) as db:
        for mid in ids:
            if db.get(Email, mid):
                continue  # уже є
            msg = fetch_message(mid)
            body = extract_body(msg)
            email_rec = Email(id=mid,
                              subject=msg["payload"]["headers"][0]["value"],
                              from_addr=msg["payload"]["headers"][1]["value"],
                              body=body)
            db.add(email_rec)
        db.commit()
    return {"synced": len(ids)}
