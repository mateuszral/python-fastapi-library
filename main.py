from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import random

from books import books


def is_date_valid(date: str) -> bool:
    is_date_correct = None
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        is_date_correct = True
    except ValueError:
        is_date_correct = False
        
    return is_date_correct

def is_isbn_valid(isbn: int) -> bool:
    sum = 0
    for index, digit in enumerate(str(isbn)[:-1]):
        if index % 2 == 0:
            sum += int(digit)
        else:
            sum += int(digit) * 3
            
    return (sum + (isbn % 10)) % 10 == 0

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
    random_number = random.randint(0, len(books) - 1)
    return books[random_number]

@app.get("/books/search")
def search_books(search_phrase: str) -> list[Book]:
    return [result for result in books if search_phrase.lower() in result["title"].lower() or search_phrase.lower() in result["author"].lower()]
    
@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book | bool:
    book = next((item for item in books if item["isbn"] == book_id), False)
    
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ISBN {book_id} not found.")
    
    return book

@app.post("/books")
def create_book(book: Book) -> Book | bool:
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
