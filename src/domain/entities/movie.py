"""
This module contains the Movie class which represents a movie.
"""


class Movie:
    """
    A class to represent a movie.
    """

    def __init__(self, movie_id: int, title: str, release_year: int):
        """
        Initializes a new instance of the Movie class.

        Args:
            movie_id (int): The ID of the movie.
            title (str): The title of the movie.
            release_year (int): The release year of the movie.
        """
        self._id = movie_id
        self._title = title
        self._release_year = release_year

    @property
    def id(self) -> int:
        """
        Gets the ID of the movie.

        Returns:
            int: The ID of the movie.
        """
        return self._id

    @property
    def title(self) -> str:
        """
        Gets the title of the movie.

        Returns:
            str: The title of the movie.
        """
        return self._title

    @property
    def release_year(self) -> int:
        """
        Gets the release year of the movie.

        Returns:
            int: The release year of the movie.
        """
        return self._release_year
