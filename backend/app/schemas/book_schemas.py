from typing import List, Optional
from pydantic import BaseModel

from app.schemas.note_schemas import NoteViewSchema

class BookSummarySchema(BaseModel):
    name: str
    atual_page: int
    pages: int

class BookCreateSchema(BaseModel):
    name: str
    author:str
    pages: int

class BookUpdateSchema(BaseModel):
    name: str
    author:str
    pages: int

class BookViewSchema(BaseModel):
    name: str
    author:str
    atual_page: int
    pages: int
    notes: Optional[List[NoteViewSchema]]