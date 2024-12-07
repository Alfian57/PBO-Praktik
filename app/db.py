import mysql.connector
import os


class DB:

    __instance = None

    @staticmethod
    def get_instance():
        if DB.__instance is None:
            DB()
        return DB.__instance

    def __init__(self):
        if DB.__instance is not None:
            raise Exception("Kelas ini adalah singleton!")
        else:
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
            self.cursor = self.connection.cursor()
            DB.__instance = self

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
