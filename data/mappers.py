"""
Convert RAWG JSON to ORM models
"""

from app.models.models import Game, Developer, Genre, Publisher, Platform, Creator
from typing import List
import requests
from datetime import date


def convert_game_data(data) -> List[Game]:
    game_models = []
    while data is not None and len(game_models) < 500:
        games = data["results"]
        for game in games:
            esrb = game.get("esrb_rating") or {}
            game_model = Game(
                game_id=game["id"],
                name=game["name"],
                slug=game["slug"],
                released=date(*map(int, game["released"].split("-"))),
                rating=game["rating"],
                metacritic_score=game["metacritic"],
                esrb_rating=esrb.get("name")
            )

            game_models.append(game_model)
            print(f"{game_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        #fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return game_models

def get_game_relationship_data(data: dict) -> dict:
    game_platform_groups = {}
    game_genre_groups = {}

    while data is not None and len(game_platform_groups) < 500:
        games = data["results"]
        for game in games:
            game_id = game["id"]
            genre_ids = []
            platform_ids = []
            platforms = game["platforms"]
            for platform in platforms:
                platform_id = platform["platform"]["id"]
                platform_ids.append(platform_id)
            genres = game["genres"]
            for genre in genres:
                genre_id = genre["id"]
                genre_ids.append(genre_id)

            game_platform_groups[game_id] = platform_ids
            game_genre_groups[game_id] = genre_ids
            print(f"Platform and Genre relationships built for {game['name']}")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return {
        "Game_Platforms" : game_platform_groups,
        "Game_Genres" : game_genre_groups
    }

def convert_developer_data(data: dict) -> List[Developer]:
    developer_models = []

    while data is not None and len(developer_models) < 500:
        developers = data["results"]
        for developer in developers:
            developer_model = Developer(
                developer_id = developer["id"],
                name = developer["name"],
                slug = developer["slug"],
                games_count = developer["games_count"]
            )

            developer_models.append(developer_model)
            print(f"{developer_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return developer_models

def convert_genre_data(data: dict) -> List[Genre]:
    genre_models = []

    while data is not None:
        genres = data["results"]
        for genre in genres:
            genre_model = Genre(
                genre_id=genre["id"],
                name=genre["name"],
                slug=genre["slug"],
                games_count=genre["games_count"]
            )

            genre_models.append(genre_model)
            print(f"{genre_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return genre_models

def convert_platform_data(data: dict) -> List[Platform]:
    platform_models = []

    while data is not None:
        platforms = data["results"]
        for platform in platforms:
            platform_model = Platform(
                platform_id=platform["id"],
                name=platform["name"],
                slug=platform["slug"],
                games_count=platform["games_count"]
            )

            platform_models.append(platform_model)
            print(f"{platform_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return platform_models

def convert_publisher_data(data: dict) -> List[Publisher]:
    publisher_models = []
    unique_ids = set()

    while data is not None and len(publisher_models) < 500:
        publishers = data["results"]
        for publisher in publishers:
            if publisher["id"] in unique_ids:
                continue
            publisher_model = Publisher(
                publisher_id=publisher["id"],
                name=publisher["name"],
                slug=publisher["slug"],
                games_count=publisher["games_count"]
                )

            publisher_models.append(publisher_model)
            unique_ids.add(publisher["id"])
            print(f"{publisher_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return publisher_models

def convert_creator_data(data: dict) -> List[Creator]:
    creator_models = []
    unique_ids = set()

    while data is not None and len(creator_models) < 499:
        creators = data["results"]
        for creator in creators:
            if creator["id"] in unique_ids:
                continue
            creator_model = Creator(
                creator_id=creator["id"],
                name=creator["name"],
                slug=creator["slug"],
                games_count=creator["games_count"]
            )

            creator_models.append(creator_model)
            unique_ids.add(creator["id"])
            print(f"{creator_model.name} model created.")

        next_url = data["next"]
        if not next_url:
            break

        # fetch the next page
        response = requests.get(next_url)
        response.raise_for_status()
        data = response.json()

    return creator_models

