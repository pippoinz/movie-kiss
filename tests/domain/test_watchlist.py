"""
This module contains unit tests for the Watchlist class.
"""

import pytest

from src.domain.entities.watchlist import Watchlist
from src.domain.entities.movie import Movie
from src.domain.exceptions import (
    WatchlistFullException,
    MovieNotFoundException,
    MovieAlreadyInWatchlistException,
)


def test_watchlist_add_movie():
    """
    Test case to verify the functionality of adding a movie to the watchlist.
    """
    watchlist = Watchlist(1)
    movie = Movie(1, "A Special Day", 1977)
    watchlist.add_movie(movie.id)
    assert movie.id in watchlist.movies


def test_watchlist_remove_movie():
    """
    Test case to verify the functionality of removing a movie from the watchlist.
    """
    watchlist = Watchlist(1)
    movie = Movie(1, "All About Eve", 1950)
    watchlist.add_movie(movie.id)
    watchlist.remove_movie(movie.id)
    assert movie.id not in watchlist.movies


def test_watchlist_add_movie_limit_reached():
    """
    Test case to verify that an exception is raised when the watchlist limit
    is reached.
    """
    watchlist = Watchlist(watchlist_id=1, limit=2)
    movie1 = Movie(1, "2001: A Space Odyssey", 1968)
    movie2 = Movie(2, "Steamboat Bill, Jr.", 1928)
    movie3 = Movie(3, "Modern Times", 1936)
    watchlist.add_movie(movie1.id)
    watchlist.add_movie(movie2.id)
    with pytest.raises(WatchlistFullException):
        watchlist.add_movie(movie3.id)


def test_watchlist_remove_nonexistent_movie():
    """
    Test case to verify that an exception is raised when trying to remove a
    nonexistent movie from the watchlist.
    """
    watchlist = Watchlist(1)
    movie = Movie(1, "Songs from the Second Floor", 2000)
    with pytest.raises(MovieNotFoundException):
        watchlist.remove_movie(movie.id)


def test_watchlist_add_existing_movie():
    """
    Test case to verify that an exception is raised when trying to add an existing
    movie to the watchlist.
    """
    watchlist = Watchlist(1)
    movie = Movie(1, "Happy End", 1967)
    watchlist.add_movie(movie.id)
    with pytest.raises(MovieAlreadyInWatchlistException):
        watchlist.add_movie(movie.id)
