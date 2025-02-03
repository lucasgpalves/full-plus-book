from typing import List

from fastapi import Depends

from app.schemas.book_schemas import BookSummarySchema, BookViewSchema
from app.repositories.book_repository import BookRepository

class BookService:

    def __init__(self, repository: BookRepository = Depends()) -> None:
        self.repository = repository

    async def get_all_books(self) -> List[BookSummarySchema]:
        books = self.repository.find_all_books()
        return [books.model_dump()]
        # BookRepository.find_all_books()

    async def get_by_id_book(self) -> BookViewSchema:
        book = self.repository
        return []
