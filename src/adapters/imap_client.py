import email, imaplib
from src.settings_loader import get_settings  # noqa: F401
settings = get_settings()

def fetch_last_messages(limit: int = 10, inbox: str = "INBOX"):
    mails = []
    with imaplib.IMAP4_SSL(settings.IMAP_HOST, settings.IMAP_PORT) as imap:
        imap.login(settings.IMAP_USER, settings.IMAP_PASS)
        imap.select(inbox)
        typ, data = imap.search(None, "ALL")
        ids = data[0].split()[-limit:]
        for mid in ids[::-1]:
            typ, msg_data = imap.fetch(mid, "(RFC822)")
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()
            mails.append(
                {
                    "id": mid.decode(),
                    "from": msg["From"],
                    "subject": msg["Subject"],
                    "body": body.strip()[:500],
                }
            )
    return mails
