from typing import List, Optional
from sqlalchemy.orm import Session
from api.database.models import Item

class ItemRepository:

    @staticmethod
    def find(db: Session, id: int = None, fonte: str = None) -> Item:
        if id is not None:
            itens = db.query(Item).filter(Item.id == id)
        elif fonte is not None:
            itens = db.query(Item).filter(Item.fonte == fonte)
        else:
            itens = db.query(Item).all()
        return itens

    @staticmethod
    def delete(db: Session, id: int = None, fonte: str = None) -> None:
        if id is not None:
            itens = db.query(Item).filter(Item.id == id)
            itens.delete()
            db.commit()
        elif fonte is not None:
            itens = db.query(Item).filter(Item.fonte == fonte)
            itens.delete()
            db.commit()
        else:
            print('fodeu')

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Item).filter(Item.id == id).first() is not None
    
    @staticmethod
    def exists_by_font(db: Session, fonte: str) -> bool:
        return db.query(Item).filter(Item.fonte == fonte).first() is not None     
    
    @staticmethod
    def create(db: Session, Item: Item) -> list[Item]:
        if Item.id:
            db.merge(Item)
        else:
            db.add(Item)
        db.commit()
        return Item


    # @staticmethod
    # def find_all(db: Session) -> list[Item]:
    #     return db.query(Item).all()
    
    # @staticmethod
    # def delete_by_id(db: Session, id: int) -> None:
    #     itens = db.query(Item).filter(Item.id == id)
    #     itens.delete()
    #     db.commit()   


    # @staticmethod
    # def delete_all(db: Session) -> None:
    #     itens = db.query(Item).all()
    #     db.delete(itens)
    #     db.commit()