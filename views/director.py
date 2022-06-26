from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)
    def get(self):
        return self.schema.dump(director_service.get()), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    schema = DirectorSchema()
    def get(self, director_id: int):
        return self.schema.dump(director_service.get(director_id)), 200
