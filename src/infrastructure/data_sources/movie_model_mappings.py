from src.domain.entities.movie import Movie
from src.infrastructure.data_sources.local.local_movie import LocalMovie


class MovieModelMappings:
    @staticmethod
    def to_entity(local_movie: LocalMovie) -> Movie:
        if local_movie is None:
            return None

        return Movie(
            movie_id=local_movie.movie_id,
            title=local_movie.title,
            release_year=local_movie.release_year,
        )
