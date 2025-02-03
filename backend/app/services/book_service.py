from typing import List, Optional

from fastapi import Depends

from app.schemas.book_schemas import BookSummarySchema, BookViewSchema
from app.schemas.note_schemas import NoteViewSchema
from app.repositories.relational_db.book_repository import BookRepositoryRelational

class BookService:

    def __init__(self, repository: BookRepositoryRelational = Depends()) -> None:
        self.repository = repository

    async def get_all_books(self) -> List[BookSummarySchema]:
        books = self.repository.find_all()
        return [books.model_dump()]

    async def get_by_id_book(self, id: int) -> Optional[BookViewSchema]:
        data = self.repository.find_by_id(id)
        book = BookViewSchema(
            name=data.name,
            author=data.author,
            atual_page=data.atual_page,
            pages=data.pages,
            notes=[NoteViewSchema(**note.__dict__) for note in data.notes] if data.notes else []
        )

        return book
