from typing import Any, List, Tuple, Optional
from abc import ABC, abstractmethod

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book_schemas import BookCreateSchema, BookUpdateSchema

class AbstractBookRepository(ABC):
    session = Any

    @abstractmethod
    def find_all(self) -> List[Book]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Book]:
        raise NotImplementedError

    @abstractmethod
    def create(self, data: BookCreateSchema) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, data: BookUpdateSchema) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists_by_id(self, id: int) -> bool:
        raise NotImplementedError