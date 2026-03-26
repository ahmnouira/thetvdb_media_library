CREATE_MOVIES_QUERY = """
    CREATE TABLE movies (
    mid INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    release_year VARCHAR(25),
    size VARCHAR(15),
    file_name VARCHAR(150),
    poster_file VARCHAR(150),
    video_codec VARCHAR(25),
    audio_codec VARCHAR(25),
    runtime VARCHAR(10),
    language VARCHAR(25),
    genre VARCHAR(50),
    imdb_link VARCHAR(250),
    tvdb_link VARCHAR(250),
    tmdb_link VARCHAR(250),
    mdblist_link VARCHAR(250),
    trakt_link VARCHAR(250),
    rt_link VARCHAR(250),
    description VARCHAR(250)
) 
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""".strip()


INSERT_MOVIE_QUERY = "INSERT INTO movies (mid, name, runtime, release_year, tvdb_link, poster_file) VALUES (%s, %s, %s, %s, %s, %s)"
