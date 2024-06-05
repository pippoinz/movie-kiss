""" 
This module contains the Watchlist class which represents a watchlist of movies.
"""

from typing import List

from domain.exceptions import (
    MovieAlreadyExistsException,
    MovieNotFoundException,
    WatchlistFullException,
)


class Watchlist:
    """
    A class to represent a watchlist of movies.
    """

    def __init__(self, watchlist_id: int, limit: int = 3):
        """
        Constructs all the necessary attributes for the watchlist object.

        Parameters
        ----------
        watchlist_id : int
            The ID of the watchlist.
        limit : int, optional
            The maximum number of movies allowed in the watchlist (default is 3).
        """

        self._id = watchlist_id
        self._movies = []
        self._limit = limit

    @property
    def id(self) -> int:
        """
        Gets the ID of the watchlist.

        Returns
        -------
        int
            The ID of the watchlist.
        """

        return self._id

    @property
    def movies(self) -> List[int]:
        """
        Returns the list of movie IDs in the watchlist.

        Returns
        -------
        List[int]
            The list of movie IDs in the watchlist.
        """
        return self._movies

    def add_movie(self, movie_id: int):
        """
        Adds a movie to the watchlist if the limit is not reached.

        Parameters
        ----------
        movie_id : int
            The ID of the movie to add to the watchlist.

        Raises
        ------
        MovieAlreadyExistsException
            If the movie is already in the watchlist.
        WatchlistFullException
            If the watchlist is full and cannot add more movies.
        """
        if len(self._movies) < self._limit:
            if movie_id not in self._movies:
                self._movies.append(movie_id)
            else:
                raise MovieAlreadyExistsException("Movie is already in the watchlist.")
        else:
            raise WatchlistFullException("Watchlist is full. Cannot add more movies.")

    def remove_movie(self, movie_id: int):
        """
        Removes a movie from the watchlist if it exists, otherwise raises an exception.

        Parameters
        ----------
        movie_id : int
            The ID of the movie to remove from the watchlist.

        Raises
        ------
        MovieNotFoundException
            If the movie does not exist in the watchlist.
        """
        if movie_id in self._movies:
            self._movies.remove(movie_id)
        else:
            raise MovieNotFoundException("Movie does not exist in the watchlist.")
