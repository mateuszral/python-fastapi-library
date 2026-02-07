# Python FastAPI Library

Small example REST API for managing a simple books collection using FastAPI.

## Features
- List, search, sort and paginate books
- Get a random book
- Add, update and delete books (stored in `books.json`)

## Requirements
- Python 3.8+
- `fastapi`, `uvicorn`, `pydantic`

Install dependencies (recommended inside a virtualenv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pydantic
```

## Run

Start the app with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000/ and interactive docs at http://127.0.0.1:8000/docs

## Data model

Books are represented with the following fields (Pydantic `Book` model in `models.py`):

```json
{
  "isbn": "string",
  "title": "string",
  "author": "string",
  "pages": 123,
  "release_date": "YYYY-MM-DD"
}
```

The data is persisted in `books.json` located at the project root.

## API Endpoints

- GET `/` — welcome message
- GET `/books` — list books
  - Query params: `limit` (int), `offset` (int), `order_by` (title|author|pages|release_date|isbn), `order_type` (ASC|DESC)

- GET `/books/random` — returns a random book

- GET `/books/search?search_phrase=...` — search by title or author (case-insensitive)

- GET `/books/{book_id}` — get book by ISBN (integer/string without dashes)

- POST `/books` — add a book
  - Body: JSON matching the `Book` model. Example:

```bash
curl -X POST "http://127.0.0.1:8000/books" -H "Content-Type: application/json" \
  -d '{"isbn":"9783161484100","title":"My Book","author":"Me","pages":100,"release_date":"2020-01-01"}'
```

- DELETE `/books/{book_id}` — delete book by ISBN

- PUT `/books/{book_id}` — partial update
  - Body: JSON object with fields to update (keys -> new values). Example:

```bash
curl -X PUT "http://127.0.0.1:8000/books/9783161484100" -H "Content-Type: application/json" \
  -d '{"title":"Updated title","pages":150}'
```

## Notes & Validation
- ISBNs are normalized by stripping dashes and spaces; the app validates ISBN format using `utils.is_isbn_valid`.
- `release_date` must be in `YYYY-MM-DD` format (validated by `utils.is_date_valid`).
- On create/update/delete operations the `books.json` file is rewritten.

## Troubleshooting
- If the app can't find `books.json`, it starts with an empty list and will create the file on first write.

## Next steps
- Add automated tests, a requirements file, and input examples in `books.json`.