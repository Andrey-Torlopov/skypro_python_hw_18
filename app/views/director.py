from flask_restx import Resource, Namespace

# TODO: сервисы

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return "", 200


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id: int):
        return "", 200
        # try:
        #     data = db.session.query(models.Director).filter(models.Director.id == id).one()
        #     return genre_scheme.dupm(data), 200
        # except Exception as e:
        #     return str(e), 404