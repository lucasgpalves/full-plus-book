import uvicorn
from fastapi import FastAPI

from app.routes import book

app = FastAPI()

app.include_router(book.router)

def main():
    print('\033[93m Starting server in http://localhost:8000 ... \033[00m')

    uvicorn.run(
        app,
        host="localhost",
        port=8000,
    )