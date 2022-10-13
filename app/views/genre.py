from flask_restx import Resource, Namespace

# TODO: сервисы

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id: int):
        return "", 200