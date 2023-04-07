from pydantic import BaseModel

class ItemMercadoLivreBase(BaseModel):
    id: int
    nome: str
    preco: float
    # fonte: str

class ItemMercadoLivreRequest(ItemMercadoLivreBase):
    ...

class ItemMercadoLivreResponse(ItemMercadoLivreBase):
    id: int

    class Config:
        orm_mode = True

class ItemPrezunic(BaseModel):
    id: int
    nome: str
    preco: float
    # fonte: str

class ItemPrezunicRequest(ItemPrezunic):
    ...

class ItemPrezunicResponse(ItemPrezunic):
    id: int

    class Config:
        orm_mode = True
