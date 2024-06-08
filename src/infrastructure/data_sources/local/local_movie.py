""" This module contains the LocalMovie class. """


class LocalMovie:
    """
    Represents a movie stored locally.
    """

    def __init__(self, movie_id: str, title: str, release_year: int):
        """
        Initializes a LocalMovie object with the given movie ID, title, and release year.

        Args:
            movie_id (str): The unique identifier of the movie.
            title (str): The title of the movie.
            release_year (int): The year the movie was released.
        """
        self._id = movie_id
        self._title = title
        self._release_year = release_year

    @property
    def movie_id(self) -> str:
        """
        Returns the movie ID.

        Returns:
            str: The movie ID.
        """
        return self._id

    @property
    def title(self) -> str:
        """
        Returns the title of the movie.

        Returns:
            str: The title of the movie.
        """
        return self._title

    @property
    def release_year(self) -> int:
        """
        Returns the release year of the movie.

        Returns:
            int: The release year of the movie.
        """
        return self._release_year
