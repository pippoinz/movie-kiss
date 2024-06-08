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
    def add_movie(self, movie: Movie) -> None:
        """
        Adds a movie to the repository.

        Args:
            movie (Movie): The movie to add to the repository.
        """

    def remove_movie(self, movie: Movie) -> None:
        """
        Removes a movie from the repository.

        Args:
            movie (Movie): The movie to remove from the repository.
        """
