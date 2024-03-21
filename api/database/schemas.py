from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    item: str
    preco: float
    fonte: str
    categoria: str

class ItemRequest(Item):
    pass

class ItemResponse(Item):
    id: int

    class Config:
        orm_mode = True

class Mercado(BaseModel):
    nome: str
    localizacao: Optional[str] = None

class MercadoRequest(Mercado):
    pass

class MercadoResponse(Mercado):
    id: int
    itens: List[Item] = []

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