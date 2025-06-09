from sqlmodel import SQLModel
from src.adapters.db.session import engine
from src.core.entities import Client, Case, Contract, Lawsuit

def init():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init()
