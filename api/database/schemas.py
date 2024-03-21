from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    item: str
    preco: float
    fonte: str

class ItemRequest(Item):
    pass

class ItemResponse(Item):
    id: int

    class Config:
        orm_mode = True