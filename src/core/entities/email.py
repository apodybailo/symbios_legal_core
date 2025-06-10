from sqlmodel import SQLModel, Field
from typing import Optional
class Email(SQLModel, table=True):
    id: str = Field(primary_key=True)
    subject: Optional[str] = None
    from_addr: Optional[str] = None
    body: str
