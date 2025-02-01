from pydantic import BaseModel
from .note import Note

class Book(BaseModel):
    name: str
    author: str
    pages: str
    notes: list[Note]