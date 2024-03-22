from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str
    mercado_id: int

class ItemRequest(Item):
    pass

class ItemResponse(Item):
    id: int

    class Config:
        orm_mode = True

class Mercado(BaseModel):
    id: int
    nome: str

class MercadoRequest(Mercado):
    pass

class MercadoResponse(Mercado):
    id: int

    class Config:
        orm_mode = True

# class Preco(BaseModel):
#     valor: float
#     item_id: int
#     mercado_id: int

# class PrecoRequest(Preco):
#     pass

# class PrecoResponse(Preco):
#     id: int
#     item: Item
#     mercado: Mercado

#     class Config:
#         orm_mode = True

# class Categoria(BaseModel):
#     nome: str
#     descricao: Optional[str] = None

# class CategoriaRequest(Categoria):
#     pass

# class CategoriaResponse(Categoria):
#     id: int

#     class Config:
#         orm_mode = True        