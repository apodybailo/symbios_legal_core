import smtplib, ssl
from email.message import EmailMessage
from pathlib import Path
from src.settings_loader import get_settings  # noqa: F401

settings = get_settings()

def send_email(to_addr: str, subject: str, body: str, attachment_path: Path | None = None):
    msg = EmailMessage()
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        data = attachment_path.read_bytes()
        maintype, _, subtype = "application", None, "octet-stream"
        msg.add_attachment(
            data,
            maintype=maintype,
            subtype=subtype,
            filename=attachment_path.name,
        )

    context = ssl.create_default_context()
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)
