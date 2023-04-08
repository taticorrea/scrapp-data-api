from pydantic import BaseModel

class ItemPrezunicBase(BaseModel):
    id: int
    nome: str
    preco: float

class ItemPrezunicRequest(ItemPrezunicBase):
    ...

class ItemPrezunicResponse(ItemPrezunicBase):
    id: int

    class Config:
        orm_mode = True

class ItemMercadoLivreBase(BaseModel):
    id: int
    nome: str
    preco: float

class ItemMercadoLivreRequest(ItemMercadoLivreBase):
    ...

class ItemMercadoLivreResponse(ItemMercadoLivreBase):
    id: int

    class Config:
        orm_mode = True