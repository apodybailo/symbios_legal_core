from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from src.adapters.email_client import send_email

router = APIRouter()

class EmailSendRequest(BaseModel):
    to: str
    subject: str
    body: str

@router.post("/sync", summary="Sync Gmail inbox")
def sync_inbox_task(background_tasks: BackgroundTasks):
    from src.tasks.email_sync import sync_inbox
    task = sync_inbox.delay()
    return {"task_id": task.id}

@router.get("/", summary="List stored emails")
def list_emails():
    from src.adapters.imap_client import fetch_last_messages
    return fetch_last_messages()

@router.post("/send", summary="Send an email")
def send_email_endpoint(
    req: EmailSendRequest, bg: BackgroundTasks
):
    bg.add_task(send_email, req.to, req.subject, req.body, None)
    return {"status": "queued"}