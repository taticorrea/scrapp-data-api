from typing import List
from sqlalchemy.orm import Session
from api.database.models import ItemPrezunic
from api.database.database import engine, Base, get_db
from api.database.repositories import ItemPrezunicRepository
from fastapi import FastAPI, Depends, HTTPException, status, Response
from api.database.schemas import ItemPrezunicRequest, ItemPrezunicResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/prezunic/add_itens", response_model=ItemPrezunicResponse, status_code=status.HTTP_201_CREATED)
def create(items: List[ItemPrezunicRequest], db: Session = Depends(get_db)):
    db_items = []
    for item in items:
        # print(type(item))
        print(item)
        db_item = ItemPrezunicRepository.save(db, ItemPrezunic(**item.dict()))
        db_items.append(db_item)
    return Response(status_code=status.HTTP_201_CREATED)

@app.get("/api/prezunic/list_itens", response_model=list[ItemPrezunicResponse])
def find_all(db: Session = Depends(get_db)):
    itens_prezunic = ItemPrezunicRepository.find_all(db)
    return [ItemPrezunicResponse.from_orm(item) for item in itens_prezunic]

@app.delete("/api/prezunic/delete_item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ItemPrezunicRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado"
        )
    ItemPrezunicRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.delete("/api/prezunic/delete_all/", status_code=status.HTTP_204_NO_CONTENT)
# def delete_all(db: Session = Depends(get_db)):
#     ItemPrezunicRepository.delete_all(db)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.post("/api/mercadolivre/add_itens", response_model=ItemMercadoLivreResponse, status_code=status.HTTP_201_CREATED)
# def create(request: ItemMercadoLivreRequest, db: Session = Depends(get_db)):
#     item = ItemMercadoLivreRepository.save(db, ItemMercadoLivre(**request.dict()))
#     return ItemMercadoLivreResponse.from_orm(item)

# @app.get("/api/mercadolivre/list_itens", response_model=list[ItemMercadoLivreResponse])
# def find_all(db: Session = Depends(get_db)):
#     itens = ItemMercadoLivreRepository.find_all(db)
#     return [ItemMercadoLivreResponse.from_orm(item) for item in itens]

# @app.delete("/api/mercadolivre/delete_item/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_by_id(id: int, db: Session = Depends(get_db)):
#     if not ItemMercadoLivreRepository.exists_by_id(db, id):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado"
#         )
#     ItemMercadoLivreRepository.delete_by_id(db, id)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)