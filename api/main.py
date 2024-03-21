from typing import List, Optional
from sqlalchemy.orm import Session
from api.database.models import Item
from sqlalchemy.exc import InterfaceError
from api.database.repositories import ItemRepository
from api.database.database import engine, Base, get_db
from api.database.schemas import ItemRequest, ItemResponse
from fastapi import FastAPI, Depends, HTTPException, status, Response

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/v2/create-item", response_model=ItemResponse, status_code=status.HTTP_409_CONFLICT)
def create(items: List[ItemRequest], db: Session = Depends(get_db)):
    db_items = []
    for item in items:
        db_item = ItemRepository.create(db, Item(**item.dict()))
        db_items.append(db_item)
    return Response(status_code=status.HTTP_201_CREATED)

@app.get("/api/v2/item/", response_model=list[ItemResponse])
def find(db: Session = Depends(get_db), id: int = None, fonte: str = None ):     
    itens = ItemRepository.find(db, id, fonte)
    return [ItemResponse.from_orm(item) for item in itens]

@app.delete("/api/v2/delete-item/", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int = None, fonte: str = None, db: Session = Depends(get_db)):
    if id is None and fonte is None:
        raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND, detail="Argumentos necessários"
                    )
    ItemRepository.delete(db, id, fonte)
    return Response(status_code=status.HTTP_204_NO_CONTENT)