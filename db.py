import datetime
import mysql.connector

from app.log import log_error


class Database:
    def __init__(
        self, user="root", password="", database="", local: bool = True
    ) -> None:

        if local:
            self.database = database
            try:
                self.db = mysql.connector.connect(
                    host="localhost",  # inside a container
                    user=user,
                    password=password,
                    database=database,
                )
            except Exception as e:
                log_error(e)  # To do try to create database automatically

        self.cursor = self.db.cursor(dictionary=True)

    def exec(self, sql: str, params=()):
        self.cursor.execute(sql, params=params)
        return self.cursor.fetchall()

    def exec_insert(self, sql: str, params=()):
        self.cursor.execute(sql, params=params)
        self.db.commit()

    def exec_close(self, sql: str):
        self.exec(sql)
        self.cursor.close()

    def use(self):
        self.exec(f"USE {self.database}")

    def show_databases(self):
        return self.exec("SHOW DATABASES")

    def show_tables(self):
        return self.exec(f"SHOW TABLES")

    def show_columns(self, table: str):
        return self.exec("SHOW COLUMNS FROM %s", [table])

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
