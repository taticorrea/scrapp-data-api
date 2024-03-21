from typing import List, Optional
from sqlalchemy.orm import Session
from api.database.models import Item

class ItemRepository:
    @staticmethod
    def find(db: Session, id: Optional[int] = None, fonte: Optional[str] = None) -> Item:
        if id:
            itens = db.query(Item).filter(Item.id == id)
        elif fonte:
            itens = db.query(Item).filter(Item.fonte == fonte)
        else:
            itens = db.query(Item).all()
        return itens


    @staticmethod
    def delete(db: Session, id: int = None, fonte: str = None) -> None:
        try:
            if id:
                itens = db.query(Item).filter(Item.id == id)
                itens.delete()
                db.commit()
            elif fonte:
                itens = db.query(Item).filter(Item.fonte == fonte)
                itens.delete()
                db.commit()
        except:
            print("Falta parametros")
            pass

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        itens = db.query(Item).filter(Item.id == id)
        itens.delete()
        db.commit()        
    
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
    # def exists_by_id(db: Session, id: int) -> bool:
    #     return db.query(Item).filter(Item.id == id).first() is not None

    # @staticmethod
    # def delete_all(db: Session) -> None:
    #     itens = db.query(Item).all()
    #     db.delete(itens)
    #     db.commit()