from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    schema = GenreSchema(many=True)
    def get(self):
        return self.schema.dump(genre_service.get()), 200


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    schema = GenreSchema()
    def get(self, genre_id: int):
        return self.schema.dump(genre_service.get(genre_id)), 200
