from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()


@router.get("/", response_model=list[ItemResponse])
async def get_items(db: Session = Depends(get_db)):
    return []


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    raise HTTPException(status_code=404, detail="Item not found")
