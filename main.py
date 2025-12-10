from fastapi import FastAPI


app = FastAPI(title="Video Game Data API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Video Game Data API"}

@app.get("/games")
def get_genres():
    return {"message": "Games"}

@app.get("/developers")
def get_genres():
    return {"message": "Developers"}

@app.get("/genres")
def get_genres():
    return {"message": "Genres"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
