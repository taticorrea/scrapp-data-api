from typing import List, Optional
from sqlalchemy.orm import Session
from api.database.models import *

class ItemRepository:
    @staticmethod
    def find(db: Session, id: int = None, mercado_id: str = None) -> ItemModel:
        if id is not None:
            itens = db.query(ItemModel).filter(ItemModel.id == id)
        elif mercado_id is not None:
            itens = db.query(ItemModel).filter(ItemModel.mercado_id == mercado_id)
        else:
            itens = db.query(ItemModel).all()
        return itens

    @staticmethod
    def delete(db: Session, id: int = None, mercado_id: str = None) -> None:
        if id is not None:
            itens = db.query(ItemModel).filter(ItemModel.id == id)
            itens.delete()
            db.commit()
        elif mercado_id is not None:
            itens = db.query(ItemModel).filter(ItemModel.mercado_id == mercado_id)
            itens.delete()
            db.commit()
        else:
            print('fodeu')

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(ItemModel).filter(ItemModel.id == id).first() is not None
    
    @staticmethod
    def exists_by_font(db: Session, mercado_id: int) -> bool:
        return db.query(ItemModel).filter(ItemModel.mercado_id == mercado_id).first() is not None     
    
    @staticmethod
    def create(db: Session, ItemModel: ItemModel) -> list[ItemModel]:
        if ItemModel.id:
            db.merge(ItemModel)
        else:
            db.add(ItemModel)
        db.commit()
        return ItemModel
    
class MercadoRepository:
    @staticmethod
    def find(db: Session, MercadoModel: MercadoModel) -> MercadoModel:
        mercados = db.query(MercadoModel).all()
        return mercados

    @staticmethod
    def create(db: Session, MercadoModel: MercadoModel) -> list[MercadoModel]:
        if MercadoModel.id:
            db.merge(MercadoModel)
        else:
            db.add(MercadoModel)
        db.commit()
        return MercadoModel    