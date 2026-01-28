from fastapi import FastAPI, HTTPException

from books import books


app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to library"

@app.get("/books")
def get_all_books(limit: int = 10, offset: int = 0) -> list:
    return books[offset:limit]

@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict | bool:
    book = next((item for item in books if item["isbn"] == book_id), False)
    
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ISBN {book_id} not found.")
    
    return book
