# Тут создаем DAO и сервисы, чтобы импортировать их например во вьюшках
from app.database import db
from app.dao.movie_dao import MovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.director_dao import DirectorDAO

movie_dao = MovieDAO(db.session)
# movie_service = BookService(dao=book_dao)

genre_dao = GenreDAO(db.session)
# genre_service = BookService(dao=book_dao)

director_dao = DirectorDAO(db.session)
# director_service = BookService(dao=book_dao)