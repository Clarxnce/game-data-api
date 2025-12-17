from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Game

router = APIRouter(prefix="/games", tags=["games"])

@router.get("")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()

    formatted_games = []
    for game in games:
        formatted_games.append({
            "id": game.game_id,
            "name": game.name,
            "slug": game.slug,
            "release_date": game.released,
            "community_rating": game.rating,
            "metacritic_score": game.metacritic_score,
            "esrb_rating": game.esrb_rating
        })
    return {"Games": formatted_games}

@router.get("/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()

    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    genres = []
    platforms = []
    for genre in game.genres:
        genres.append(genre.name)
    for platform in game.platforms:
        platforms.append(platform.name)

    return {
        "id": game.game_id,
            "name": game.name,
            "slug": game.slug,
            "release_date": game.released,
            "genres": genres,
            "platforms": platforms,
            "community_rating": game.rating,
            "metacritic_score": game.metacritic_score,
            "esrb_rating": game.esrb_rating
    }