from fastapi import FastAPI
from app.routers import games, developers, creators, genres, platforms, publishers


app = FastAPI(title="Video Game Data API", version="1.0.0")

# Include routers
app.include_router(developers.router)
app.include_router(creators.router)
app.include_router(genres.router)
app.include_router(platforms.router)
app.include_router(publishers.router)
app.include_router(games.router)


@app.get("/")
def root():
    return {"message": "Video Game Data API"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
