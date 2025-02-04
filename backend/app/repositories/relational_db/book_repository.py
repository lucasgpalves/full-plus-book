from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

from fastapi import Depends
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.book import Book
from app.models.exception import BookNotFound
from app.repositories.abstraction.book_repository import AbstractBookRepository
from app.schemas.book_schemas import (
    BookCreateSchema,
    BookUpdateSchema
)
class BookRepositoryRelational(AbstractBookRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_all_books(self) -> List[Book]:
        stmt = select(Book).order_by(Book.id)
        data = (await self.session.execute(stmt)).scalars().all()
        return data
    
    async def find_by_id(self, id: int) -> Optional[Book]:
        stmt = select(Book).where(Book.id == id)
        data = (await self.session.execute(stmt)).scalars().first()
        return data
    
    async def create(self, data: BookCreateSchema ) -> None:
        self.session.add(data)
        self.session.commit()

    async def update(self, id: int, data: BookUpdateSchema) -> None:
        
        stmt = update(Book).where(Book.id == id).values(data)
        res = await self.session.execute(stmt)
        if res.rowcount == 0:
            raise BookNotFound(id)
 

    
    async def delete(self, id: int) -> None:
        data = self.session.query(Book).filter(Book.id == id).first()
        if data:
            self.session.delete(data)
            self.session.commit()
            return 1
        return None