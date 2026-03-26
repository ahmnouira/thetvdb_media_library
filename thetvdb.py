from rest import Rest


class TheTVDB:
    token = ""

    def __init__(self, api="https://api4.thetvdb.com/v4", api_key=None) -> None:
        self.__client = Rest(api)
        self.api_key = api_key if api_key else "8481ad97-d671-45a1-95ee-277241e6d328"

    def __to_movie(self, data: dict):
        title = data.get("name")
        year = data.get("year")

        return {
            "id": data.get("id"),
            "image": data.get("image"),
            "title": title,
            "slug": data.get("slug"),
            "year": year,
        }

    def login(self):
        data = self.__client.post("login", {"apikey": self.api_key})
        if data:
            self.token = data["data"]["token"]
            return self.token

    def get_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}

    def __get(self, url: str):
        data = self.__client.get(url, headers=self.get_headers())
        if data and "data" in data:
            return self.__to_movie(data["data"])

    def movies(self):
        data = self.__client.get("movies", headers=self.get_headers())
        if data:
            return data["data"]

    def movie(self, id: str):
        return self.__get(f"movies/{id}")

    def movie_by_slub(self, slug: str):
        return self.__get(f"movies/{slug}")
