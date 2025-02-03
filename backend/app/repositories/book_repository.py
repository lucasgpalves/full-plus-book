from typing import List, Tuple, Optional

from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book

class BookRepository:

    def __init__(self, session: Session = Depends()) -> None:
        self.session = session

    def find_all_books(self) -> List[Tuple]:
        stmt = select(Book).order_by(Book.id)
        data = self.session.execute(stmt).scalars().all()
        return data
    
    def find_by_id_book(self, id: int) -> Optional[Tuple]:
        stmt = select(Book).where(Book.id == id)
        data = self.session.execute(stmt)
        return data