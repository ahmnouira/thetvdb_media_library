import datetime
import mysql.connector


class Database:
    def __init__(
        self, user="root", password="", database="", local: bool = True
    ) -> None:

        if local:
            self.db = mysql.connector.connect(
                host="localhost",  # inside a container
                user=user,
                password=password,
                database=database,
            )

        self.cursor = self.db.cursor(dictionary=True)

    def exec(self, sql: str, params=()):
        self.cursor.execute(sql, params=params)
        return self.cursor.fetchall()

    def exec_close(self, sql: str):
        self.exec(sql)
        self.cursor.close()

    def all(self, table: str):
        self.exec(f"SELECT * FROM %s", (table))

    def save(self, data: dict):
        pass

    def get(self, id):
        return {}

    def delete(self, id):
        return {}

    def clean(self):
        items = self.coll

    def close_all(self):
        self.cursor.close()
        self.db.close()
