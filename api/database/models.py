from api.database.database import Base
from sqlalchemy import Column, Integer, String, Float

class ItemPrezunic(Base):
    __tablename__ = "prezunic"

    id: int = Column(Integer, primary_key=True, index=True)
    item: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    fonte: str = Column(String(200), nullable=True)