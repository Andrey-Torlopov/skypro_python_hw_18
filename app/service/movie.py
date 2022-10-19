from app.service_container import MovieDAO
from app.dao.models.movie import Movie


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data) -> Movie:
        return self.dao.create(data)

    def get_one(self, uid: int) -> Movie:
        return self.dao.get_one(uid)

    def get_all(self, director_id:int=None, genre_id:int=None, year:int=None) -> list[Movie]:
        return self.dao.get_all(director_id=director_id, genre_id=genre_id, year=year)

    def update(self, data, uid):
        '''Update model full and particular'''
        model = self.get_one(uid)
        model = self._update_if_possible(model, data)
        self.dao.update(model)

    def delete(self, uid: int):
        self.dao.delete(uid)

    # Private

    def _update_if_possible(self, model: Movie, data: dict[str, str]) -> Movie:
        if 'name' in data:
            model.name = data.get('name')

        if 'description' in data:
            model.description = data.get('description')

        if 'trailer' in data:
            model.trailer = data.get('trailer')

        if 'year' in data:
            model.year = data.get('year')

        if 'rating' in data:
            model.rating = data.get('rating')

        if 'genre_id' in data:
            model.genre_id = data.get('genre_id')

        if 'director_id' in data:
            model.director_id = data.get('director_id')

        return model