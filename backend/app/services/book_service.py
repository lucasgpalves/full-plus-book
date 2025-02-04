from typing import List, Optional

from fastapi import Depends

from app.schemas.book_schemas import (
    BookCreateSchema, 
    BookSummarySchema,
    BookUpdateSchema, 
    BookViewSchema,
)
from app.schemas.note_schemas import NoteViewSchema
from app.repositories.relational_db.book_repository import BookRepositoryRelational

class BookService:

    def __init__(self, repository: BookRepositoryRelational = Depends()) -> None:
        self.repository = repository

    async def get_all_books(self) -> List[BookSummarySchema]:
        books = self.repository.find_all()
        return [books.model_dump()]

    async def get_book_by_id(self, id: int) -> Optional[BookViewSchema]:
        data = self.repository.find_by_id(id)
        book = BookViewSchema(
            name=data.name,
            author=data.author,
            atual_page=data.atual_page,
            pages=data.pages,
            notes=[NoteViewSchema(**note.__dict__) for note in data.notes] if data.notes else []
        )

        return book

    async def create_book(self, book: BookCreateSchema) -> None:
        self.repository.create(book)

    async def update_book_by_id(self, id: int, updated_book: BookUpdateSchema) -> None:
        book_to_update = self.repository.find_by_id(id)

        if not book_to_update:
            return None
        
        book_to_update.name = updated_book.name
        book_to_update.author = updated_book.author
        book_to_update.atual_pages = updated_book.author
        book_to_update.pages = updated_book.pages

        self.repository.update(id, updated_book)

    async def delete_book_by_id(self, id: int) -> None:
        book = self.repository.find_by_id()
        
        self.repository.delete()