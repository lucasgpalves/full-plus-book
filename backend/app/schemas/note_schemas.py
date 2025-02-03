from pydantic import BaseModel
from datetime import datetime

class NoteViewSchema(BaseModel):
    description: str

class NoteCreateSchema(BaseModel):
    book_id: int
    date: datetime
    description: str