from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="zeroday.cloud FastAPI target")


class Message(BaseModel):
    text: str


@app.get("/")
def root():
    return {"service": "fastapi", "status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: str | None = None):
    return {"item_id": item_id, "query": query}


@app.post("/echo")
def echo(message: Message):
    return message
