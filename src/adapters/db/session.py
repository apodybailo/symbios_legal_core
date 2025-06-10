from sqlmodel import create_engine
from src.settings_loader import get_settings  # переконайся, що це absolute-import

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

def SessionLocal():
    from sqlmodel import Session
    return Session(engine)