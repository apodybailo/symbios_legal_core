from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str

class ClientRead(ClientCreate):
    id: int
    class Config:
        orm_mode = True
