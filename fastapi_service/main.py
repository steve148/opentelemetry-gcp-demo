import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RootResponse(BaseModel):
    message: str


class Book(BaseModel):
    url: str
    name: str


@app.get("/")
def root() -> list[Book]:
    response = requests.get("https://www.anapioficeandfire.com/api/books")
    response.raise_for_status()
    data = response.json()
    return [Book(url=book["url"], name=book["name"]) for book in data]
