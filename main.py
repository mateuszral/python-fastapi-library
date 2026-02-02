from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

from books import books
from utils import is_isbn_valid, is_date_valid

app = FastAPI()

class Book(BaseModel):
    isbn: int
    title: str
    author: str
    pages: int
    release_date: str

@app.get("/")
def read_root() -> str:
    return "Welcome to library"

@app.get("/books")
def get_all_books(limit: int = 10, offset: int = 0) -> list[Book]:
    return books[offset : offset + limit]

@app.get("/books/random")
def get_random_book() -> Book:
    return random.choice(books)

@app.get("/books/search")
def get_book(search_phrase: str) -> list[Book]:
    return [result for result in books if search_phrase.lower() in result["title"].lower() or search_phrase.lower() in result["author"].lower()]
    
@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book | bool:
    book = next((item for item in books if item["isbn"] == book_id), False)
    
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ISBN {book_id} not found.")
    
    return book

@app.post("/books")
def add_book(book: Book) -> Book | bool:
    if not book.title or not book.author:
        raise HTTPException(status_code=400, detail="Title/author cannot be empty")
    
    if book.pages <= 0:
        raise HTTPException(status_code=400, detail="Number of pages must be greater than zero.")
    
    if not is_isbn_valid(book.isbn) or book.isbn < 0:
        raise HTTPException(status_code=400, detail=f"ISBN {book.isbn} is invalid")
    
    
    if any(item for item in books if item["isbn"] == book.isbn):
        raise HTTPException(status_code=400, detail=f"Book with ISBN {book.isbn} already exists.")
    
    if not is_date_valid(book.release_date):
        raise HTTPException(status_code=400, detail=f"Release date ({book.release_date}) is not in valid format (YYYY-MM-DD)")
        
    books.append(book)
    return book
