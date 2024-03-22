from api.database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class ItemModel(Base):
    __tablename__ = "itens"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200))
    preco: float = Column(Float)
    categoria: str = Column(String(200))
    mercado_id = Column(Integer, ForeignKey('mercados.id'))
    
    mercado = relationship('MercadoModel', back_populates='itens')

class MercadoModel(Base):
    __tablename__ = "mercados"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200))
    
    itens = relationship('ItemModel', back_populates='mercado')

# class Categoria(Base):
#     __tablename__ = "categorias"

#     id: int = Column(Integer, primary_key=True, index=True)
#     nome: str = Column(String(200))
#     descricao: str = Column(String(100))
#     itens = relationship('Item', back_populates='categoria_id')