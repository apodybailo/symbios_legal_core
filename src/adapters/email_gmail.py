import base64, email, httpx, time
from pathlib import Path
from typing import List
from src.settings_loader import get_settings  # noqa: F401
settings = get_settings()

TOKEN_URL = "https://oauth2.googleapis.com/token"
GMAIL_API = "https://gmail.googleapis.com/gmail/v1"

def _get_access_token() -> str:
    data = {
        "client_id": settings.GMAIL_CLIENT_ID,
        "client_secret": settings.GMAIL_CLIENT_SECRET,
        "refresh_token": settings.GMAIL_REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }
    r = httpx.post(TOKEN_URL, data=data, timeout=10)
    r.raise_for_status()
    return r.json()["access_token"]

def _api_get(url: str) -> dict:
    headers = {"Authorization": f"Bearer {_get_access_token()}"}
    r = httpx.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json()

def list_message_ids(q: str = "", limit: int = 50) -> List[str]:
    box = settings.IMAP_BOX or "INBOX"
    url = f"{GMAIL_API}/users/me/messages?maxResults={limit}&labelIds={box}&q={q}"
    data = _api_get(url)
    return [m["id"] for m in data.get("messages", [])]

def fetch_message(mid: str) -> dict:
    url = f"{GMAIL_API}/users/me/messages/{mid}?format=full"
    return _api_get(url)

def extract_body(msg: dict) -> str:
    parts = msg["payload"].get("parts", [])
    for p in parts:
        if p.get("mimeType") == "text/plain":
            data = p["body"]["data"]
            return base64.urlsafe_b64decode(data).decode()
    # fallback to snippet
    return msg.get("snippet", "")
