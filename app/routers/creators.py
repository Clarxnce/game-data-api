from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Creator

router = APIRouter(prefix="/creators", tags=["creators"])

@router.get("")
def get_creators(db: Session = Depends(get_db)):
    creators = db.query(Creator).all()

    formatted_creators = []
    for creator in creators:
        formatted_creators.append({
            "id": creator.creator_id,
            "name": creator.name,
            "slug": creator.slug,
            "games_count": creator.games_count
        })
    return {"Creators": formatted_creators}

@router.get("/{creator_id}")
def get_creator(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()

    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")

    return {
        "id": creator.creator_id,
        "name": creator.name,
        "slug": creator.slug,
        "games_count": creator.games_count
    }