from api.database.database import Base
from sqlalchemy import Column, Integer, String, Float

class Item(Base):
    __tablename__ = "itens"

    id: int = Column(Integer, primary_key=True, index=True)
    item: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    fonte: str = Column(String(200), nullable=True)