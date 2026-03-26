# ----------------------
# GET MOVIES WITHOUT DATA
# ----------------------
# cursor.execute("SELECT id, TVDBID FROM movies WHERE description IS NULL")
# movies = cursor.fetchall()


movies = []

for movie in movies:
    tvdb_id = movie["TVDBID"]

    data = {}

    try:
        movie_data = data["data"]

        title = movie_data.get("name")
        overview = movie_data.get("overview")
        year = movie_data.get("year")

        # UPDATE DATABASE
        update_query = """
        UPDATE movies
        SET title=%s, description=%s, year=%s
        WHERE id=%s
        """

        # cursor.execute(update_query, (title, overview, year, movie["id"]))
        # db.commit()

        print(f"Updated: {title}")

    except Exception as e:
        print(f"Error for ID {tvdb_id}: {e}")
