"""
This module contains the movie repository interface.
"""

from abc import ABC, abstractmethod
from src.domain.entities.movie import Movie


class MovieRepository(ABC):
    """An abstract base class for movie repositories.

    This class defines the interface for movie repositories. Subclasses should implement the
    methods defined here.
    """

    @abstractmethod
    def get_movie_by_id(self, movie_id: int) -> Movie:
        """Get a movie by its ID.

        Args:
            id (int): The ID of the movie.

        Returns:
            Movie: The movie object.
        """

    @abstractmethod
    def get_movies_by_title(self, title: str) -> list[Movie]:
        """Get movies by title.

        Args:
            title (str): The title of the movies.

        Returns:
            list[Movie]: A list of movie objects.
        """

    @abstractmethod
    def get_movies_by_release_year(self, release_year: int) -> list[Movie]:
        """Get movies by release year.

        Args:
            release_year (int): The release year of the movies.

        Returns:
            list[Movie]: A list of movie objects.
        """