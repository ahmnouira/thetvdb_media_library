from thetvdb import TheTVDB

client = TheTVDB()

token = client.login()
movie = client.movie(371655)


print(movie)
