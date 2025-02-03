from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book_schemas import BookCreateSchema, BookUpdateSchema

class AbstractBookRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Book]:
        """"""

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Book]:
        """"""

    @abstractmethod
    def create(self, data: BookCreateSchema) -> None:
        """"""

    @abstractmethod
    def update(self, id: int, data: BookUpdateSchema) -> None:
        """"""

    @abstractmethod
    def delete(self) -> None:
        """"""