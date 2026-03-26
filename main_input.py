from app_db import AppDB
from thetvdb import TheTVDB

client = TheTVDB()
db = AppDB()
id = ""

while not id.isdigit():
    id = input("Enter movie id: ")


def get_movies_api(movies: []):
    client.login()
    for id in movies:
        movie = client.movie(id)
        print(movie)
        db.inset_movie(movie)


get_movies_api([id])
