from sqlalchemy import Table, Column, DECIMAL, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from datetime import date
from decimal import Decimal
from typing import Optional, List

# --- Association Tables ---

game_genre = Table(
    "game_genres",
    Base.metadata,
    Column("game_id", ForeignKey("games.game_id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", ForeignKey("genres.genre_id", ondelete="CASCADE"), primary_key=True)
)

game_platform = Table(
    "game_platforms",
    Base.metadata,
    Column("game_id", ForeignKey("games.game_id", ondelete="CASCADE"), primary_key=True),
    Column("platform_id", ForeignKey("platforms.platform_id", ondelete="CASCADE"), primary_key=True)
)


# --- Core tables ---

class Game(Base):
    __tablename__ = "games"

    game_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False, index=True)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    released: Mapped[Optional[date]] = mapped_column(Date(), index=True)
    rating: Mapped[Optional[Decimal]] = mapped_column(DECIMAL(3, 2), index=True)
    metacritic_score: Mapped[Optional[int]] = mapped_column()
    esrb_rating: Mapped[Optional[str]] = mapped_column(String(15))

    # one-way relationships
    genres: Mapped[List["Genre"]] = relationship(
        "Genre",
        secondary=game_genre,
        lazy="selectin"
    )

    platforms: Mapped[List["Platform"]] = relationship(
        "Platform",
        secondary=game_platform,
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return (f"Game(id={self.game_id}, name={self.name}, slug={self.slug}, released={self.released}, rating={self.rating},"
                f"metacritic_score={self.metacritic_score}, esrb_rating={self.esrb_rating})")

class Developer(Base):
    __tablename__ = "developers"

    developer_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    games_count: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"Developer(id={self.developer_id}, name={self.name}, slug={self.slug}, games_count={self.games_count})"

class Genre(Base):
    __tablename__ = 'genres'

    genre_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    games_count: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"Genre(id={self.genre_id}, name={self.name}, slug={self.slug}, games_count={self.games_count})"

class Platform(Base):
    __tablename__ = 'platforms'

    platform_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    games_count: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"Platform(id={self.platform_id}, name={self.name}, slug={self.slug}, games_count={self.games_count})"

class Publisher(Base):
    __tablename__ = 'publishers'

    publisher_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    games_count: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"Publisher(id={self.publisher_id}, name={self.name}, slug={self.slug}, games_count={self.games_count})"

class Creator(Base):
    __tablename__ = "creators"

    creator_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(40))
    games_count: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"Creator(id={self.creator_id}, name={self.name}, slug={self.slug}, games_count={self.games_count})"

