from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book
from app.repositories.abstraction.book_repository import AbstractBookRepository
from app.schemas.book_schemas import BookCreateSchema

class BookRepositoryRelational(AbstractBookRepository):

    def __init__(self, session: Session = Depends()) -> None:
        self.session = session

    def find_all_books(self) -> List[Tuple]:
        stmt = select(Book).order_by(Book.id)
        data = self.session.execute(stmt).scalars().all()
        return data
    
    def find_by_id(self, id: int) -> Optional[Tuple]:
        stmt = select(Book).where(Book.id == id)
        data = self.session.execute(stmt).scalars().first()
        return data
    
    def create(self, data: BookCreateSchema ) -> None:
        self.session.add(data)
        self.session.commit()
    
    def delete(self, id: int) -> None:
        data = self.session.query(Book).filter(Book.id == id).first()
        if data:
            self.session.delete(data)
            self.session.commit()
            return 1
        return None