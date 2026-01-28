from fastapi import FastAPI, HTTPException
import random

from books import books


app = FastAPI()

@app.get("/")
def read_root() -> str:
    return "Welcome to library"

@app.get("/books")
def get_all_books(limit: int = 10, offset: int = 0) -> list:
    return books[offset : offset + limit]

@app.get("/books/random")
def get_random_book() -> dict:
    random_number = random.randint(0, len(books) - 1)
    return books[random_number]

@app.get("/books/search")
def search_books(search_phrase: str) -> list[dict]:
    return [result for result in books if search_phrase.lower() in result["title"].lower() or search_phrase.lower() in result["author"].lower()]
    
@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict | bool:
    book = next((item for item in books if item["isbn"] == book_id), False)
    
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ISBN {book_id} not found.")
    
    return book
