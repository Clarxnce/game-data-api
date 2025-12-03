from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os

app = FastAPI(title="Video Game Data API", version="1.0.0")

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

if not API_KEY:
    raise RuntimeError("MY_API_KEY is not set")


def get_genre_info():
    url = "https://api.rawg.io/api/genres"
    payload = {"key": API_KEY}
    r = requests.get(url, params=payload)
    r.raise_for_status()
    return r.json()


@app.get("/")
def root():
    return {"message": "Video Game Data API"}


@app.get("/genres")
def get_genres():
    return get_genre_info()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
