from app.db import DB


class BookRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(
        self,
        title: str,
        isbn: str,
        category_id: int,
        publisher_id: int,
        publish_year: int,
    ):
        sql = "INSERT INTO books (title, isbn, category_id, publisher_id, publish_year) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(sql, (title, isbn, category_id, publisher_id, publish_year))

    def get_all(self):
        sql = "SELECT * FROM books"
        return self.db.fetch_all(sql)

    def get_by_id(self, id: int):
        sql = "SELECT * FROM books WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def update(
        self,
        id: int,
        title: str,
        isbn: str,
        category_id: int,
        publisher_id: int,
        publish_year: int,
    ):
        sql = "UPDATE books SET title = %s, isbn = %s, category_id = %s, publisher_id = %s, publish_year = %s WHERE id = %s"
        self.db.execute(sql, (title, isbn, category_id, publisher_id, publish_year, id))

    def delete(self, id: int):
        sql = "DELETE FROM books WHERE id = %s"
        self.db.execute(sql, (id,))
