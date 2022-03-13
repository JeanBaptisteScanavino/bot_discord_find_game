import pytest
from .retrieve_game_list import RetrieveGameList
from ...right.in_memory.games_repository import InMemoryGamesRepository


def test_when_i_want_to_retrieve_all_games_i_retrieve_it():
    # ARRANGE
    fake_dependencies = { 'game_repository': InMemoryGamesRepository()}
    fake_game_repository = fake_dependencies['game_repository']
    # ACT
    result = RetrieveGameList(fake_game_repository).exec()
    # ASSERT
    assert result == ['Mario', 'Sonic', 'Alex Kidd']