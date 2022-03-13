import os
from fastapi import FastAPI

from src.left.routes import create_routes
from src.right.in_memory.games_repository import InMemoryGamesRepository


basedir = os.path.abspath(os.path.dirname(__file__))
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

dependencies = { 'game_repository': InMemoryGamesRepository()}

create_routes(app, dependencies)
 