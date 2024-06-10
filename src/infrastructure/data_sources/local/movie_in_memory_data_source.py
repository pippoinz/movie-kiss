""" This module contains the MovieInMemoryDataSource class. """

from typing import List
from src.domain.exceptions import MovieNotFoundException
from src.infrastructure.data_sources.local.movie_local_data_source import (
    MovieLocalDataSource,
)
from src.infrastructure.data_sources.local.local_movie import LocalMovie


class MovieInMemoryDataSource(MovieLocalDataSource):
    """
    In-memory data source for movies.

    This class provides methods to retrieve movies from an in-memory list.
    """

    def __init__(self):
        self._movies = []

    def get_movie_by_id(self, movie_id: int) -> LocalMovie:
        """
        Retrieve a movie by its ID.

        Args:
            movie_id (int): The ID of the movie.

        Returns:
            LocalMovie: The movie object if found.
        Raises:
            MovieNotFoundException: If the movie with the given ID is not found.
        """
        for movie in self._movies:
            if movie.movie_id == movie_id:
                return movie

        raise MovieNotFoundException(f"Movie with ID {movie_id} not found")

    def get_movies_by_title(self, title: str) -> List[LocalMovie]:
        """
        Retrieve movies by title.

        Args:
            title (str): The title of the movies to retrieve.

        Returns:
            List[LocalMovie]: A list of movies with matching titles.
        """
        return [movie for movie in self._movies if title in movie.title]

    def get_movies_by_release_year(self, release_year: int) -> List[LocalMovie]:
        """
        Retrieve movies by release year.

        Args:
            release_year (int): The release year of the movies to retrieve.

        Returns:
            List[LocalMovie]: A list of movies released in the specified year.
        """
        return [movie for movie in self._movies if movie.release_year == release_year]
