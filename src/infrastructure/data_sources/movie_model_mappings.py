"""This module contains the MovieModelMappings class."""

from src.domain.entities.movie import Movie
from src.infrastructure.data_sources.local.local_movie import LocalMovie


class MovieModelMappings:
    # pylint: disable=too-few-public-methods
    """A class that provides mappings between movie models and movie entities."""

    @staticmethod
    def to_entity(local_movie: LocalMovie) -> Movie:
        """
        Converts a local movie model to a movie entity.

        Args:
            local_movie (LocalMovie): The local movie model to convert.

        Returns:
            Movie: The converted movie entity.
        """
        if local_movie is None:
            return None

        return Movie(
            movie_id=local_movie.movie_id,
            title=local_movie.title,
            release_year=local_movie.release_year,
        )
