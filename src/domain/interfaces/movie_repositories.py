"""
This module contains the movie repository interfaces.
"""

from abc import ABC, abstractmethod
from src.domain.entities.movie import Movie


class AbstractMovieRepository(ABC):
    # pylint: disable=too-few-public-methods
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


class ReadableMovieRepository(AbstractMovieRepository):
    # pylint: disable=too-few-public-methods
    """A readable movie repository.

    This class represents a readable movie repository, which provides read-only access to movies.
    """


class WritableMovieRepository(ReadableMovieRepository):
    """A writable movie repository.

    This class represents a writable movie repository, which allows adding and removing movies.
    """

    @abstractmethod
    def add_movie(self, movie: Movie) -> None:
        """Add a movie to the repository.

        Args:
            movie (Movie): The movie object to add.

        Returns:
            None
        """

    @abstractmethod
    def remove_movie(self, movie: Movie) -> None:
        """Remove a movie from the repository.

        Args:
            movie (Movie): The movie object to remove.

        Returns:
            None

        """
