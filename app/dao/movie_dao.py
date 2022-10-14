from app.dao.models.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        model = Movie(**data)
        self.session.add(model)
        self.session.commit()

    def update(self, model):
        self.session.add(model)
        self.session.commit()

    def delete(self, uid):
        model = self.get_one(uid)
        self.session.delete(model)
        self.session.commit()
