from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Platform
from app.schemas.schemas import Platform as PlatformSchema

router = APIRouter(prefix="/platforms", tags=["platforms"])

@router.get("")
def get_platforms(db: Session = Depends(get_db)):
    platforms = db.query(Platform).all()

    formatted_platforms = []
    for platform in platforms:
        formatted_platforms.append({
            "id": platform.platform_id,
            "name": platform.name,
            "slug": platform.slug,
            "games_count": platform.games_count
        })
    return {"Platforms": formatted_platforms}

@router.get("/{platform_id}")
def get_platform(platform_id: int, db: Session = Depends(get_db)):
    platform = db.query(Platform).filter(Platform.platform_id == platform_id).first()

    if not platform:
        raise HTTPException(status_code=404, detail="Platform not found")

    return {
        "id": platform.platform_id,
        "name": platform.name,
        "slug": platform.slug,
        "games_count": platform.games_count
    }