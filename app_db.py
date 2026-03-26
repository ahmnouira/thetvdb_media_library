from app.config import APP_NAME
from db import Database


class AppDB:
    __db = Database(password="root", database=APP_NAME)

    def movies(self):
        q = "SELECT mid FROM movies"
        self.__db.exec(q)
