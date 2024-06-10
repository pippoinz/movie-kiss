"""This module contains unit tests for the LocalMovie class."""

import pytest
from src.infrastructure.data_sources.local.local_movie import LocalMovie

# pylint: disable=redefined-outer-name


@pytest.fixture
def local_movie():
    """
    Fixture for creating a LocalMovie object.

    Returns:
        LocalMovie: An instance of the LocalMovie class.
    """
    return LocalMovie(1, "Seven Samurai", 1954)


def test_local_movie_attributes(local_movie):
    """
    Test case to verify the attributes of a local movie.

    Args:
        local_movie (LocalMovie): An instance of the LocalMovie class.

    Raises:
        AssertionError: If any of the attribute values do not match the expected values.

    """
    assert local_movie.movie_id == 1
    assert local_movie.title == "Seven Samurai"
    assert local_movie.release_year == 1954


def test_local_movie_immutable(local_movie):
    """
    Test case to verify that the 'movie_id' attribute of a local movie object is immutable.

    Args:
        local_movie: An instance of the LocalMovie class.

    Raises:
        AttributeError: If an attempt is made to modify the 'movie_id' attribute.

    """
    with pytest.raises(AttributeError):
        local_movie.movie_id = 2


def test_local_movie_equality(local_movie):
    """
    Test the equality of the local_movie object with another LocalMovie object.

    Args:
        local_movie (LocalMovie): The local_movie object to be tested.
    """
    other_movie = LocalMovie(1, "Seven Samurai", 1954)
    assert local_movie == other_movie


def test_local_movie_inequality(local_movie):
    """
    Test case to check the inequality of a local movie object with another movie object.

    Args:
        local_movie: The local movie object to be tested.
    """
    other_movie = LocalMovie(2, "Stray Dog", 1949)
    assert local_movie != other_movie
