"""
This module contains the DefaultMovieRepository class, which represents a default movie 
repository.
"""

from typing import List
from src.domain.entities.movie import Movie
from src.domain.interfaces.movie_repository import MovieRepository
from src.infrastructure.data_sources.local.movie_local_data_source import (
    MovieLocalDataSource,
)
from src.infrastructure.data_sources.movie_model_mappings import (
    MovieModelMappings as Mappings,
)


class DefaultMovieRepository(MovieRepository):
    """
    This class represents a default movie repository, with a local data source.
    """

    def __init__(self, local_data_source: MovieLocalDataSource):
        """
        Initializes a DefaultMovieRepository object with the given local data source.

        Args:
            local_data_source (MovieLocalDataSource): A movie local data source.
        """
        self._local_data_source = local_data_source

    def get_movie_by_id(self, movie_id: int) -> Movie:
        """
        Get a movie by its ID.

        Args:
            movie_id (int): The ID of the movie.

        Returns:
            Movie: The movie object.

        Raises:
            MovieNotFoundException: If the movie with the given ID is not found.
        """
        local_movie = self._local_data_source.get_movie_by_id(movie_id)

        return Mappings.to_entity(local_movie)

    def get_movies_by_title(self, title: str) -> List[Movie]:
        """
        Get movies by title.

        Args:
            title (str): The title of the movies.

        Returns:
            List[Movie]: A list of movie objects.
        """
        local_movies = self._local_data_source.get_movies_by_title(title)

        return [Mappings.to_entity(local_movie) for local_movie in local_movies]

    def get_movies_by_release_year(self, release_year: int) -> List[Movie]:
        """
        Get movies by release year.

        Args:
            release_year (int): The release year of the movies.

        Returns:
            List[Movie]: A list of movie objects.
        """
        local_movies = self._local_data_source.get_movies_by_release_year(release_year)

        return [Mappings.to_entity(local_movie) for local_movie in local_movies]
