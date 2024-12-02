from app.db import DB


class PublisherRepository:
    def __init(self) -> None:
        self.db = DB.get_instance()

    def add(self, name: str):
        sql = "INSERT INTO publishers (name) VALUES (%s)"
        self.db.execute(sql, (name,))

    def get_all(self):
        sql = "SELECT * FROM publishers"
        return self.db.fetch_all(sql)

    def get_by_id(self, id: int):
        sql = "SELECT * FROM publishers WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def update(self, id: int, name: str):
        sql = "UPDATE publishers SET name = %s WHERE id = %s"
        self.db.execute(sql, (name, id))

    def delete(self, id: int):
        sql = "DELETE FROM publishers WHERE id = %s"
        self.db.execute(sql, (id,))
