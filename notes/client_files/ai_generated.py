import requests
import mysql.connector

# TVDB API Config
API_URL = "https://api4.thetvdb.com/v4"
API_KEY = "YOUR_TVDB_API_KEY"
PIN = "YOUR_TVDB_PIN"

# 1. Login to get Bearer Token
login_data = {"apikey": API_KEY, "pin": PIN}
response = requests.post(f"{API_URL}/login", json=login_data)
token = response.json()["data"]["token"]
headers = {"Authorization": f"Bearer {token}"}

# 2. Fetch Movie Data (Example: Using TVDB Movie ID)
movie_id = "123456"  # Replace with actual TVDB ID
movie_url = f"{API_URL}/movies/{movie_id}/extended"
movie_response = requests.get(movie_url, headers=headers)
movie_data = movie_response.json()["data"]

# Extract metadata
title = movie_data["name"]
runtime = movie_data.get("runtime", 0)
release_date = movie_data.get("released", None)

# 3. Insert into MySQL
db = mysql.connector.connect(
    host="localhost", user="yourusername", password="yourpassword", database="movie_db"
)
cursor = db.cursor()

query = "INSERT INTO movies (tvdb_id, title, runtime, released) VALUES (%s, %s, %s, %s)"
values = (movie_id, title, runtime, release_date)

cursor.execute(query, values)
db.commit()
print(f"Inserted: {title}")

# Close connections
cursor.close()
db.close()
