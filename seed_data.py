
"""
Dataset seeder for Video Game Data API.
Imports Games, Developers, Genres, Publishers, Platforms and Creators from RAWG API and persists into SQLite DB
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from app.database import engine, Base
from app.models.models import Game, Developer, Genre, Publisher, Platform, Creator, game_platform, game_genre
from rawg_client import get_field_data
import mappers


# Create database tables
Base.metadata.create_all(bind=engine)

# Create Session
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()



def seed_database():
    print("Seeding Video Game Data dataset")

    # Clear existing data
    try:
        print("Clearing existing data base")
        db.execute(text("DELETE FROM game_genres"))
        db.execute(text("DELETE FROM game_platforms"))
        db.execute(text("DELETE FROM games"))
        db.execute(text("DELETE FROM developers"))
        db.execute(text("DELETE FROM genres"))
        db.execute(text("DELETE FROM platforms"))
        db.execute(text("DELETE FROM publishers"))
        db.execute(text("DELETE FROM creators"))
    except Exception as e:
        print(f"Could not clear existing data: {e}")
        db.rollback()

    # Game
    print("Importing Game data...")
    rawg_game_data = get_field_data("games")
    game_rows = mappers.convert_game_data(rawg_game_data)

    for i, game in enumerate(game_rows):
        db.add(game)

        if (i+1) % 100 == 0:
            db.commit()
            print(f"Inserted {i+1} rows")

    db.commit()
    print(f"Imported {len(game_rows)} games.")

    # Developer
    print("Importing Developer data...")
    rawg_developer_data = get_field_data("developers")
    developer_rows = mappers.convert_developer_data(rawg_developer_data)

    for i, developer in enumerate(developer_rows):
        db.add(developer)

        if (i + 1) % 100 == 0:
            db.commit()
            print(f"Inserted {i + 1} rows")

    db.commit()
    print(f"Imported {len(developer_rows)} developers.")

    # Genre
    print("Importing Genre data...")
    rawg_genre_data = get_field_data("genres")
    genre_rows = mappers.convert_genre_data(rawg_genre_data)

    db.add_all(genre_rows)
    db.commit()
    print(f"Imported {len(genre_rows)} genres.")

    #Platform
    print("Importing Platform data...")
    rawg_platform_data = get_field_data("platforms")
    platform_rows = mappers.convert_platform_data(rawg_platform_data)

    db.add_all(platform_rows)
    db.commit()
    print(f"Imported {len(platform_rows)} platforms.")

    #Publisher
    print("Importing Publisher data...")
    rawg_publisher_data = get_field_data("publishers")
    publisher_rows = mappers.convert_publisher_data(rawg_publisher_data)

    for i, publisher in enumerate(publisher_rows):
        db.add(publisher)

        if (i + 1) % 100 == 0:
            db.commit()
            print(f"Inserted {i + 1} rows")

    db.commit()
    print(f"Imported {len(publisher_rows)} publishers.")

    # Creator
    print("Importing Creator data...")
    rawg_creator_data = get_field_data("creators")
    creator_rows = mappers.convert_creator_data(rawg_creator_data)

    for i, creator in enumerate(creator_rows):
        db.add(creator)

        if (i + 1) % 100 == 0:
            db.commit()
            print(f"Inserted {i + 1} rows")

    db.commit()
    print(f"Imported {len(creator_rows)} creators.")

    # Game-Platforms
    game_platform_data = mappers.get_game_relationship_data(rawg_game_data)["Game_Platforms"]
    game_platform_relationships = 0
    for k,v in game_platform_data.items():
        game_id = k
        platform_ids = v
        for i in platform_ids:
            stmt = game_platform.insert().values(
                game_id=game_id,
                platform_id=i
            )
            db.execute(stmt)
            game_platform_relationships += 1

    db.commit()

    # Game-Genres
    game_genre_data = mappers.get_game_relationship_data(rawg_game_data)["Game_Genres"]
    game_genre_relationships = 0
    for k,v in game_genre_data.items():
        game_id = k
        genre_ids = v
        for i in genre_ids:
            stmt = game_genre.insert().values(
                game_id=game_id,
                genre_id=i
            )
            db.execute(stmt)
            game_genre_relationships += 1

    db.commit()

    print("\n=== SEEDING COMPLETE ===")
    print(f"Games: {len(game_rows)}")
    print(f"Developers: {len(developer_rows)}")
    print(f"Genres: {len(genre_rows)}")
    print(f"Platforms: {len(platform_rows)}")
    print(f"Publishers: {len(publisher_rows)}")
    print(f"Creators: {len(creator_rows)}")
    print(f"Game-Platform relationships: {game_platform_relationships}")
    print(f"Game-Genre relationships: {game_genre_relationships}")

if __name__ == "__main__":
    seed_database()

