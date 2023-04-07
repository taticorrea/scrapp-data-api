from api.database.database import Base
from sqlalchemy import Column, Integer, String, Float

class ItemPrezunic(Base):
    __tablename__ = "item_prezunic"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    # fonte: str = Column(String(200), nullable=False)

class ItemMercadoLivre(Base):
    __tablename__ = "item_mercadolivre"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    # fonte: str = Column(String(200), nullable=False)
