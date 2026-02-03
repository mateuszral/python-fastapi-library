import json
import random
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from utils import is_isbn_valid, is_date_valid

BOOKS_PATH = "./books.json"

try:
    with open(BOOKS_PATH, "r") as f:
        books = json.load(f)
        f.close()
except FileNotFoundError:
    books = []

app = FastAPI()

class Book(BaseModel):
    isbn: str
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
        raise HTTPException(404, f"Book with ISBN {book_id} not found.")
    
    return book

@app.post("/books", status_code=201)
def add_book(book: Book) -> dict:
    if not book.title or not book.author:
        raise HTTPException(400, "Title/author cannot be empty")
    
    if book.pages <= 0:
        raise HTTPException(400, "Number of pages must be greater than zero.")
    
    if not is_isbn_valid(book.isbn):
        raise HTTPException(400, f"ISBN {book.isbn} is invalid")
    
    
    if any(item for item in books if item["isbn"] == book.isbn):
        raise HTTPException(400, f"Book with ISBN {book.isbn} already exists.")
    
    if not is_date_valid(book.release_date):
        raise HTTPException(400, f"Release date ({book.release_date}) is not in valid format (YYYY-MM-DD)")
        
    
    json_book = jsonable_encoder(book)
    books.append(json_book)
        
    with open(BOOKS_PATH, "w") as f:
        json.dump(books, f, indent=4)
        f.close()
        
    return {"isbn": book.isbn, "message": "Book was added successfully"}