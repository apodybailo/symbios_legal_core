from sqlmodel import SQLModel
from src.adapters.db.session import engine

def init():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init()
