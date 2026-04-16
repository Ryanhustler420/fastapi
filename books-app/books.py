from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Home Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Civics"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Science"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Six", "category": "Math"},
]

@app.get("/books/mybooks")
async def all_books():
    return BOOKS

@app.get("/books/{title}")
async def get_book(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book