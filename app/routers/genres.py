from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Genre
from app.schemas.schemas import Genre as GenreSchema

router = APIRouter(prefix="/genres", tags=["genres"])

@router.get("")
def get_genres(db: Session = Depends(get_db)):
    genres = db.query(Genre).all()

    formatted_genres = []
    for genre in genres:
        formatted_genres.append({
            "id": genre.genre_id,
            "name": genre.name,
            "slug": genre.slug,
            "games_count": genre.games_count
        })
    return {"Genres": formatted_genres}

@router.get("/{genre_id}")
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.genre_id == genre_id).first()

    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    return {
        "id": genre.genre_id,
        "name": genre.name,
        "slug": genre.slug,
        "games_count": genre.games_count
    }