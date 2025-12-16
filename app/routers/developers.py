from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Developer
from app.schemas.schemas import Developer as DeveloperSchema

router = APIRouter(prefix="/developers", tags=["developers"])

@router.get("")
def get_developers(db: Session = Depends(get_db)):
    developers = db.query(Developer).all()

    formatted_developers = []
    for developer in developers:
        formatted_developers.append({
            "id": developer.developer_id,
            "name": developer.name,
            "slug": developer.slug,
            "games_count": developer.games_count
        })
    return {"Developers": formatted_developers}

@router.get("/{developer_id}")
def get_developer(developer_id: int, db: Session = Depends(get_db)):
    developer = db.query(Developer).filter(Developer.developer_id == developer_id).first()

    if not developer:
        raise HTTPException(status_code=404, detail="Developer not found")

    return {
        "id": developer.developer_id,
        "name": developer.name,
        "slug": developer.slug,
        "games_count": developer.games_count
    }