""" This module contains the MovieLocalDataSource abstract base class. """

from abc import ABC, abstractmethod
from src.infrastructure.data_sources.local.local_movie import LocalMovie


class MovieLocalDataSource(ABC):
    """An abstract base class for movie local data sources.

    This class defines the interface for movie local data sources.
    Subclasses should implement the methods defined here.
    """

    @abstractmethod
    def get_movie_by_id(self, movie_id: int) -> LocalMovie:
        """Get a movie by its ID.

        Args:
            id (int): The ID of the movie.

        Returns:
            Movie: The movie object.

        Raises:
            MovieNotFoundException: If the movie with the given ID is not found.
        """

    @abstractmethod
    def get_movies_by_title(self, title: str) -> list[LocalMovie]:
        """Get movies by title.

        Args:
            title (str): The title of the movies.

        Returns:
            list[Movie]: A list of movie objects.
        """

    @abstractmethod
    def get_movies_by_release_year(self, release_year: int) -> list[LocalMovie]:
        """Get movies by release year.

        Args:
            release_year (int): The release year of the movies.

        Returns:
            list[Movie]: A list of movie objects.
        """
