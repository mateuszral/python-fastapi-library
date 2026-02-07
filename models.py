from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    isbn: str
    title: str
    author: str
    pages: int
    release_date: str

# doesn't work
class UpdateBook(BaseModel):
    isbn: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = None
    release_date: Optional[str] = None
