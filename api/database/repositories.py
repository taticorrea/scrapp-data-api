from typing import List  
from sqlalchemy.orm import Session
from api.database.models import ItemPrezunic

class ItemPrezunicRepository:
    @staticmethod
    def find_all(db: Session) -> list[ItemPrezunic]:
        return db.query(ItemPrezunic).all()

    @staticmethod
    def save(db: Session, ItemPrezunic: ItemPrezunic) -> list[ItemPrezunic]:
        if ItemPrezunic.id:
            db.merge(ItemPrezunic)
        else:
            db.add(ItemPrezunic)
        db.commit()
        return ItemPrezunic

    @staticmethod
    def delete_by_id(db: Session, id: str) -> None:
        itens = db.query(ItemPrezunic).filter(ItemPrezunic.id == id).first()
        if ItemPrezunic is not None:
            db.delete(itens)
            db.commit()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(ItemPrezunic).filter(ItemPrezunic.id == id).first() is not None