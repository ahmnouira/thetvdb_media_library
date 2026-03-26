from thetvdb import TheTVDB

client = TheTVDB()

token = client.login()
movie = client.movie(1995)


print(movie)
