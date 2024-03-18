from typing import List, Optional
from pydantic import BaseModel

class ItemPrezunicBase(BaseModel):
    id: int
    item: str
    preco: float
    fonte: str

class ItemPrezunicRequest(ItemPrezunicBase):
    pass

class ItemPrezunicResponse(ItemPrezunicBase):
    id: int

    class Config:
        orm_mode = True

# class ItemMercadoLivreBase(BaseModel):
#     id: int
#     nome: str
#     preco: float

# class ItemMercadoLivreRequest(ItemMercadoLivreBase):
#     ...

# class ItemMercadoLivreResponse(ItemMercadoLivreBase):
#     id: int

#     class Config:
#         orm_mode = True