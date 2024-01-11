from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
def read_root():
    return {"Hello":"Word!"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:Union[str, None] = None):
    return {"item_id": item_id, "q":q }

@app.get("/operaciones")
def operaciones(op1:float, op2:float):
    return {"suma": op1 + op2,
            "diferencia": op1 - op2,
            "producto": op1 * op2,
            "cociente": op1 / op2}

