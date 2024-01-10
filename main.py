from typing import Union
from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def read_root():
    return {"Hello":"Word!"}

@app.get("/items/{item_id}")
def 