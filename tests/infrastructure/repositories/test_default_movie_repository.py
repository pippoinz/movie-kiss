"""
This module contains unit tests for the DefaultMovieRepository class.
"""

import pytest
from src.infrastructure.repositories.default_movie_repository import (
    DefaultMovieRepository,
)
from src.domain.entities.movie import Movie
from src.domain.exceptions import MovieNotFoundException, MovieAlreadyExistsException


def test_get_movie_by_id():
    """
    Test case for the 'get_movie_by_id' method of the DefaultMovieRepository class.
    """
    movie_repository = DefaultMovieRepository()
    movie = Movie(1, "Hara-Kiri", 1962)
    movie_repository.add_movie(movie)

    result = movie_repository.get_movie_by_id(1)

    assert result == movie


def test_get_movie_by_id_not_found():
    """
    Test case for the 'get_movie_by_id' method of the DefaultMemoryRepository class when movie is
    not found.
    """
    movie_repository = DefaultMovieRepository()

    with pytest.raises(MovieNotFoundException):
        movie_repository.get_movie_by_id(1)


def test_add_movie():
    """
    Test case for the 'add_movie' method of the DefaultMemoryRepository class.
    """
    movie_repository = DefaultMovieRepository()
    movie = Movie(1, "City Lights", 1931)

    movie_repository.add_movie(movie)
    result = movie_repository.get_movie_by_id(1)

    assert result == movie


def test_add_movie_already_exists():
    """
    Test case for the 'add_movie' method of the DefaultMemoryRepository class when movie already
    exists.
    """
    movie_repository = DefaultMovieRepository()
    movie = Movie(1, "The Cameraman", 1928)
    movie_repository.add_movie(movie)

    with pytest.raises(MovieAlreadyExistsException):
        movie_repository.add_movie(movie)


def test_remove_movie():
    """
    Test case for the 'remove_movie' method of the DefaultMemoryRepository class.
    """
    movie_repository = DefaultMovieRepository()
    movie = Movie(1, "The Grand Illusion", 1937)
    movie_repository.add_movie(movie)

    movie_repository.remove_movie(movie)
    with pytest.raises(MovieNotFoundException):
        movie_repository.get_movie_by_id(1)


def test_remove_movie_not_found():
    """
    Test case for the 'remove_movie' method of the DefaultMemoryRepository class when movie is not
    found.
    """
    movie_repository = DefaultMovieRepository()
    movie = Movie(1, "Barry Lyndon", 1975)

    with pytest.raises(MovieNotFoundException):
        movie_repository.remove_movie(movie)
