class Movie:
    """
    A class to represent a movie.

    """

    def __init__(self, title: str, release_year: int):
        """
        Initializes a new instance of the Movie class.

        Args:
            title (str): The title of the movie.
            release_year (int): The release year of the movie.
        """
        self._title = title
        self._release_year = release_year

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
