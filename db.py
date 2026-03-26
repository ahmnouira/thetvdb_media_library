import datetime
import mysql.connector


class Database:
    def __init__(self, local: bool = True) -> None:
        if local:
            self.uri = "mongodb://admin:password@localhost:27017/"
        else:
            self.uri = "mongodb+srv://lamiarouag1998:O5EHAScDqFn4KIYW@cluster0.zoeej.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        self.db = mysql.connector.connect(
            host="localhost", user="root", password="yourpassword", database="media_db"
        )

        self.cursor = self.db.cursor(dictionary=True)
        print(self.client)

    def save(self, data: dict, predictions: list[float], duration: float, name: str):
        data = data.dict()
        data["predictions"] = predictions
        data["duration"] = duration
        data["name"] = name
        data["created_at"] = datetime.now()
        self.collection.insert_one(data)

    def all(self):
        items = []
        for item in self.collection.find():
            items.append(get_item(item))
        return items

    def get(self, id):
        return {}

    def delete(self, id):
        return {}

    def clean(self):
        items = self.coll

    def close(self):
        self.cursor.close()
        self.db.close()
