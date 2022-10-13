from flask_restx import Resource, Namespace

# TODO: сервисы

movies_ns = Namespace('movies')

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        try:
            return "", 200
        except Exception as e:
            return str(e), 404

    def put(self, id: int):
        return "", 204

    def patch(self, id: int):
        return "", 204

    def delete(self, id: int):
        return "", 204