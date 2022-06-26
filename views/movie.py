# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask import request
from flask.helpers import make_response
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from service.movie import *

# настройка конфигурации


# неймспейсы
from implemented import movie_service

movie_ns = Namespace("movies")


# api для фильмов
@movie_ns.route('/')
class MoviesView(Resource):
    # получааем данные (реализован поиск по director_id, genre_id)
    schema = MovieSchema(many=True)

    def get(self):
        movie = self.schema.dump(movie_service.get_movies(**request.args))
        return movie, 200

    # добавляем в базу
    def post(self):
        new_movie = movie_service.create_movie(request.json)
        resp = make_response("", 200)
        resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp


# api для фильма
@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    # поиск по id
    schema = MovieSchema()

    def get(self, movie_id: int):
        movie = self.schema.dump(movie_service.get_movies(movie_id))
        return movie, 200

    # частичное изменение данных
    def patch(self, movie_id: int):
        data = request.json
        return self.schema.dump(movie_service.update_movie_partial(movie_id, data)), 200

    # полное изменение
    def put(self, movie_id: int):
        return self.schema.dump(movie_service.update_movie_full(movie_id, request.json))

    # удаление данных по id
    def delete(self, movie_id: int):
        movie_service.delete(movie_id)
        return 204
