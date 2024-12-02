from app.db import DB


class ClassRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, name: str):
        sql = "INSERT INTO class (name) VALUES (%s)"
        self.db.execute(sql, (name,))

    def get_all(self):
        sql = "SELECT * FROM class"
        return self.db.fetch_all(sql)

    def get_by_id(self, id: int):
        sql = "SELECT * FROM class WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def update(self, id: int, name: str):
        sql = "UPDATE class SET name = %s WHERE id = %s"
        self.db.execute(sql, (name, id))

    def delete(self, id: int):
        sql = "DELETE FROM class WHERE id = %s"
        self.db.execute(sql, (id,))
