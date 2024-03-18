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

# class ItemMercadoLivreRepository:
#     @staticmethod
#     def find_all(db: Session) -> list[ItemMercadoLivre]:
#         return db.query(ItemMercadoLivre).all()

#     @staticmethod
#     def save(db: Session, ItemMercadoLivre: ItemMercadoLivre) -> ItemMercadoLivre:
#         if ItemMercadoLivre.id:
#             db.merge(ItemMercadoLivre)
#         else:
#             db.add(ItemMercadoLivre)
#         db.commit()
#         return ItemMercadoLivre

#     @staticmethod
#     def find_by_font(db: Session, id: str) -> ItemMercadoLivre:
#         return db.query(ItemMercadoLivre).filter(ItemMercadoLivre.id == id).first()

#     @staticmethod
#     def exists_by_id(db: Session, id: int) -> bool:
#         return db.query(ItemMercadoLivre).filter(ItemMercadoLivre.id == id).first() is not None

#     @staticmethod
#     def delete_all(db: Session) -> None:
#         itens = db.query(ItemMercadoLivre).all()
#         db.delete(itens)
#         db.commit()
    
#     @staticmethod
#     def delete_by_id(db: Session, id: str) -> None:
#         itens = db.query(ItemMercadoLivre).filter(ItemMercadoLivre.id == id).first()
#         if ItemMercadoLivre is not None:
#             db.delete(itens)
#             db.commit()
