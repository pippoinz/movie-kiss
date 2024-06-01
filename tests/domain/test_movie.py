"""
This module contains unit tests for the Movie class.
"""

from src.domain.entities.movie import Movie


def test_movie_title():
    """
    Test case for the `title` property of the Movie class.
    """
    movie = Movie("Sunrise: A Song of Two Humans", 1927)
    assert movie.title == "Sunrise: A Song of Two Humans"


def test_movie_release_year():
    """
    Test case for the `release_year` property of the Movie class.
    """
    movie = Movie("Singin' in the Rain", 1952)
    assert movie.release_year == 1952
