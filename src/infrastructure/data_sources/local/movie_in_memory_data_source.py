""" This module contains the MovieInMemoryDataSource class. """

from typing import List
from src.infrastructure.data_sources.local.movie_local_data_source import (
    MovieLocalDataSource,
)
from src.infrastructure.data_sources.local.local_movie import LocalMovie


class MovieInMemoryDataSource(MovieLocalDataSource):
    def __init__(self):
        self._movies = []

    def get_movie_by_id(self, movie_id: int) -> LocalMovie:
        for movie in self._movies:
            if movie.movie_id == movie_id:
                return movie
        return None

    def get_movies_by_title(self, title: str) -> List[LocalMovie]:
        return [movie for movie in self._movies if title in movie.title]

    def get_movies_by_release_year(self, release_year: int) -> List[LocalMovie]:
        return [movie for movie in self._movies if movie.release_year == release_year]
