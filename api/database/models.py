from api.database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class ItemModel(Base):
    __tablename__ = "itens"

    id: int = Column(Integer, primary_key=True, index=True)
    item: str = Column(String(200))
    preco: float = Column(Float)
    categoria: str = Column(String(200))
    mercado_id: float = Column(Float)
    # mercado_id = Column(Integer, ForeignKey('mercados.id'))
    
    # mercado = relationship('Mercado', back_populates='itens')

# class MercadoModel(Base):
#     __tablename__ = "mercados"

#     id: int = Column(Integer, primary_key=True, index=True)
#     nome: str = Column(String(200))
#     localizacao: str = Column(String(100))
#     itens = Column(Integer, ForeignKey('itens.id'))

    
#     itens = relationship('Item', back_populates='mercado')

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