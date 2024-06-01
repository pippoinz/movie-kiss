"""
This module contains custom exception classes for the domain.
"""


class WatchlistFullException(Exception):
    """
    Exception raised when the watchlist is full and a movie cannot be added.
    """


class MovieAlreadyInWatchlistException(Exception):
    """
    Exception raised when a movie is already in the watchlist.
    """


class MovieNotFoundException(Exception):
    """
    Exception raised when a movie is not found in the watchlist.
    """
