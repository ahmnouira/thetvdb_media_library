import requests
from app.log import log_error


class Rest:
    DEBUG = False

    def __init__(self, url: str, DEBUG=False) -> None:
        self.url = url
        if DEBUG:
            self.DEBUG = DEBUG

    def post(self, url="", data: dict = {}, headers=None):
        try:
            if self.DEBUG:
                print(f"{self.url}/{url}", data)
            response = requests.post(f"{self.url}/{url}", json=data, headers=headers)
            return response.json()
        except Exception as e:
            log_error(e)

    def get(self, url="", headers=None):
        try:
            response = requests.get(f"{self.url}/{url}", headers=headers)
            return response.json()
        except Exception as e:
            log_error(e)
