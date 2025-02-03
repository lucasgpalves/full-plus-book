from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.schemas.book_schemas import (
    BookSummarySchema,
    BookViewSchema
)
from app.services.book_service import BookService

print('Loading book router')

service = BookService()

router = APIRouter(
    prefix='/books'
)

@router.get('/', response_model=List[BookSummarySchema])
async def all_books():
    return await service.get_all_books()

@router.get('/{book_id}', response_model=BookViewSchema)
async def by_id_book(book_id: int):
    book = await service.get_by_id_book(book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail='Book not found'
        )
    return book