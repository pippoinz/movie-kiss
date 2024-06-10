""" This module contains the LocalMovie class. """

from dataclasses import dataclass


@dataclass(frozen=True)
class LocalMovie:
    """
    Represents a movie stored locally.

    Attributes:
        movie_id (int): The ID of the movie.
        title (str): The title of the movie.
        release_year (int): The release year of the movie.
    """

    movie_id: int
    title: str
    release_year: int
