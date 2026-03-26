from app.config import APP_NAME
from app.log import log_info
from db import Database
from queries import CREATE_MOVIES_QUERY, INSERT_MOVIE_QUERY


class AppDB:

    def __init__(self, DEBUG=False) -> None:
        self.__db = Database(password="root", database=APP_NAME)
        self.DEBUG = DEBUG
        self.__db.use()

    def movies(self):
        q = "SELECT * FROM movies"
        return self.__db.exec(q)

    def movie_ids(self):
        q = "SELECT mid FROM movies"
        return self.__db.exec(q)

    def inset_movie(self, data: dict):
        values = tuple(data.values())
        self.__db.exec_insert(INSERT_MOVIE_QUERY, values)

    def tables(self):
        data = self.__db.show_tables()
        if self.DEBUG:
            log_info(data)

    def test(self):
        data = self.__db.show_databases()
        log_info(data)

    def movies_cols(self):
        data = self.__db.show_columns("movies")
        if self.DEBUG:
            log_info(data)

    def create_movies_table(self):
        self.__db.exec(CREATE_MOVIES_QUERY)
