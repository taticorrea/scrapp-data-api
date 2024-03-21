from api.database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Item(Base):
    __tablename__ = "itens"

    id: int = Column(Integer, primary_key=True, index=True)
    item: str = Column(String(200))
    preco: float = Column(Float)
    fonte: str = Column(String(100))
    categoria_id = relationship('Categoria', back_populates='itens')
    mercado = relationship('mercado', back_populates='nome')

class Mercado(Base):
    __tablename__ = "mercados"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200))
    localizacao: str = Column(String(100))
    itens = relationship('Item', back_populates='mercado')
    precos = relationship('Preco', back_populates='mercado')

# class Preco(Base):
#     __tablename__ = "precos"
    
#     id = Column(Integer, primary_key=True, index=True)
#     valor = Column(Float)
#     item_id = Column(Integer, ForeignKey('itens.id'))
#     mercado_id = Column(Integer, ForeignKey('mercados.id'))
#     item = relationship('Item', back_populates='preco')
#     mercado = relationship('Mercado', back_populates='precos')

# class Categoria(Base):
#     __tablename__ = "categorias"

#     id: int = Column(Integer, primary_key=True, index=True)
#     nome: str = Column(String(200))
#     descricao: str = Column(String(100))
#     itens = relationship('Item', back_populates='categoria_id')