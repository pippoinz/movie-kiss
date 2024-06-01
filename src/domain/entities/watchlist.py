from src.domain.entities.movie import Movie
from src.domain.exceptions import WatchlistFullException
from src.domain.exceptions import MovieNotFoundException
from src.domain.exceptions import MovieAlreadyInWatchlistException


class Watchlist:
    """
    A class to represent a watchlist of movies.

    """

    def __init__(self, limit: int = 3):
        """
        Constructs all the necessary attributes for the watchlist object.

        Parameters
        ----------
        limit : int, optional
            maximum number of movies allowed in the watchlist (default is 3)
        """

        self._movies = []
        self._limit = limit

    @property
    def movies(self):
        """
        Returns the tuple of movies in the watchlist.

        Returns
        -------
        tuple
            the tuple of movies in the watchlist
        """
        return tuple(self._movies)

    def add_movie(self, movie: Movie):
        """
        Adds a movie to the watchlist if the limit is not reached

        Parameters
        ----------
        movie : Movie
            The movie object to add to the watchlist.

        Raises
        ------
        MovieAlreadyInWatchlistException
            If the movie is already in the watchlist.
        WatchlistFullException
            If the watchlist is full and cannot add more movies.
        """
        if len(self._movies) < self._limit:
            if movie not in self._movies:
                self._movies.append(movie)
            else:
                raise MovieAlreadyInWatchlistException(
                    "Movie is already in the watchlist."
                )
        else:
            raise WatchlistFullException("Watchlist is full. Cannot add more movies.")

    def remove_movie(self, movie: Movie):
        """
        Removes a movie from the watchlist if it exists, otherwise raises an exception.

        Parameters
        ----------
        movie : Movie
            a movie to remove from the watchlist

        Raises
        ------
        MovieNotFoundException
            if the movie does not exist in the watchlist
        """
        if movie in self._movies:
            self._movies.remove(movie)
        else:
            raise MovieNotFoundException("Movie does not exist in the watchlist.")
