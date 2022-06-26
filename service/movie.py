# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, mid=None, **kwargs):
        return self.movie_dao.get(mid, **kwargs)

    def create_movie(self, data):
        return self.movie_dao.create(data)

    def update_movie_full(self, movie_id, data):
        movie = self.get_movies(movie_id)
        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]
        self.movie_dao.update(movie)
        return movie

    def update_movie_partial(self, movie_id, data):
        movie = self.get_movies(movie_id)
        if 'title' in data:
            movie.title = data["title"]
        elif 'description' in data:
            movie.description = data["description"]
        elif 'trailer' in data:
            movie.trailer = data["trailer"]
        elif 'year' in data:
            movie.year = data["year"]
        elif 'rating' in data:
            movie.rating = data["rating"]
        elif 'genre_id' in data:
            movie.genre_id = data["genre_id"]
        elif 'director_id' in data:
            movie.director_id = data["director_id"]
        self.movie_dao.update(movie)
        return movie

    def delete(self, mid):
        self.movie_dao.delete(mid)
