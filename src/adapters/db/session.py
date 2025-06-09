from sqlmodel import create_engine, Session
from ..settings_loader import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={{"check_same_thread": False}})

def SessionLocal():
    return Session(engine)
