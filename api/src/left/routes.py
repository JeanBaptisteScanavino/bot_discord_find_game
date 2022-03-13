from ..core.use_cases.retrieve_game_list import RetrieveGameList
from ..right.in_memory.games_repository import InMemoryGamesRepository

def create_routes(app,dependencies):

    @app.get("/games")
    async def retrieve_games():
        return  RetrieveGameList(dependencies['game_repository']).exec()
