from pydantic import BaseModel

class BookSummarySchema(BaseModel):
    name: str
    atual_pages: int
    pages: int

class BookCreateSchema(BaseModel):
    # TODO
    pass

class BookViewSchema(BaseModel):
    name: str
    author:str
    atual_page: int
    pages: int
    