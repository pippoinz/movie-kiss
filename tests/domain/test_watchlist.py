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
    watchlist = Watchlist()
    movie = Movie("A Special Day", 1977)
    watchlist.add_movie(movie)
    assert movie in watchlist.movies


def test_watchlist_remove_movie():
    """
    Test case to verify the functionality of removing a movie from the watchlist.
    """
    watchlist = Watchlist()
    movie = Movie("All About Eve", 1950)
    watchlist.add_movie(movie)
    watchlist.remove_movie(movie)
    assert movie not in watchlist.movies


def test_watchlist_add_movie_limit_reached():
    """
    Test case to verify that an exception is raised when the watchlist limit is reached.
    """
    watchlist = Watchlist(limit=2)
    movie1 = Movie("2001: A Space Odyssey", 1968)
    movie2 = Movie("Steamboat Bill, Jr.", 1928)
    movie3 = Movie("Modern Times", 1936)
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    with pytest.raises(WatchlistFullException):
        watchlist.add_movie(movie3)


def test_watchlist_remove_nonexistent_movie():
    """
    Test case to verify that an exception is raised when trying to remove a nonexistent movie from the watchlist.
    """
    watchlist = Watchlist()
    movie = Movie("Songs from the Second Floor", 2000)
    with pytest.raises(MovieNotFoundException):
        watchlist.remove_movie(movie)


def test_watchlist_add_existing_movie():
    """
    Test case to verify that an exception is raised when trying to add an existing movie to the watchlist.
    """
    watchlist = Watchlist()
    movie = Movie("Happy End", 1967)
    watchlist.add_movie(movie)
    with pytest.raises(MovieAlreadyInWatchlistException):
        watchlist.add_movie(movie)
