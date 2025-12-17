from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from decimal import Decimal

class DeveloperBase(BaseModel):
    id: int
    name: str
    slug: str
    games_count: int

    class Config:
        from_attributes = True

class Developer(DeveloperBase):
    pass

class GenreBase(BaseModel):
    id: int
    name: str
    slug: str
    games_count: int

    class Config:
        from_attributes = True

class Genre(GenreBase):
    pass

class PlatformBase(BaseModel):
    id: int
    name: str
    slug: str
    games_count: int

    class Config:
        from_attributes = True


class Platform(PlatformBase):
    pass

class PublisherBase(BaseModel):
    id: int
    name: str
    slug: str
    games_count: int

    class Config:
        from_attributes = True

class Publisher(PublisherBase):
    pass

class CreatorBase(BaseModel):
    id: int
    name: str
    slug: str
    games_count: int

    class Config:
        from_attributes = True

class Creator(CreatorBase):
    pass


class GameBase(BaseModel):
    id: int
    name: str
    slug: str
    genre: List[Genre]
    release_date: date
    rating: Decimal
    metacritic_score: int
    esrb_rating: Optional[str]

    class Config:
        from_attributes = True

class Game(GameBase):
    pass