from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Publisher
from app.schemas.schemas import Publisher as PublisherSchema

router = APIRouter(prefix="/publishers", tags=["publishers"])

@router.get("")
def get_publishers(db: Session = Depends(get_db)):
    publishers = db.query(Publisher).all()

    formatted_publishers = []
    for publisher in publishers:
        formatted_publishers.append({
            "id": publisher.publisher_id,
            "name": publisher.name,
            "slug": publisher.slug,
            "games_count": publisher.games_count
        })
    return {"Publishers": formatted_publishers}

@router.get("/{publisher_id}")
def get_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.publisher_id == publisher_id).first()

    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")

    return {
        "id": publisher.publisher_id,
        "name": publisher.name,
        "slug": publisher.slug,
        "games_count": publisher.games_count
    }