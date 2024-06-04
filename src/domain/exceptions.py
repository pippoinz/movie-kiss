"""
This module contains custom exception classes for the domain.
"""


class WatchlistFullException(Exception):
    """
    Exception raised when the watchlist is full and a movie cannot be added.
    """


class MovieAlreadyExistsException(Exception):
    """
    Exception raised when a movie already exists in a collection.
    """


class MovieNotFoundException(Exception):
    """
    Exception raised when a movie is not found in a collection.
    """
