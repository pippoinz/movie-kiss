"""
This module contains the DefaultMovieRepository class, which represents a default movie 
repository.
"""

from typing import List
from src.domain.interfaces.movie_repository import MovieRepository
from src.domain.entities.movie import Movie
from src.domain.exceptions import MovieNotFoundException, MovieAlreadyExistsException


class DefaultMovieRepository(MovieRepository):
    """
    This class represents a default movie repository, with in-memory storage.
    """

    def __init__(self):
        """
        Initializes an instance of the DefaultMovieRepository class.

        It initializes an empty list to store movies.
        """
        self._movies: List[Movie] = []

    def get_movie_by_id(self, movie_id: int) -> Movie:
        """
        Retrieves a movie by its ID.

        Args:
            movie_id (int): The ID of the movie to retrieve.

        Returns:
            Movie: The movie with the specified ID.

        Raises:
            MovieNotFoundException: If no movie with the specified ID is found.
        """
        for movie in self._movies:
            if movie.id == movie_id:
                return movie
        raise MovieNotFoundException(f"Movie with ID {movie_id} not found.")

    def add_movie(self, movie: Movie) -> None:
        """
        Adds a movie to the repository.

        Args:
            movie (Movie): The movie to add to the repository.

        Raises:
            MovieAlreadyExistsException: If a movie with the same ID already exists in the
            repository.
        """
        if any(existing_movie.id == movie.id for existing_movie in self._movies):
            raise MovieAlreadyExistsException(
                f"Movie with ID {movie.id} already exists in the repository."
            )

        self._movies.append(movie)

    def remove_movie(self, movie: Movie) -> None:
        """
        Removes a movie from the repository.

        Args:
            movie (Movie): The movie to remove from the repository.

        Raises:
            MovieNotFoundException: If the movie is not found in the repository.
        """
        if movie not in self._movies:
            raise MovieNotFoundException(
                f"Movie with ID {movie.id} not found in the repository."
            )

        self._movies.remove(movie)
