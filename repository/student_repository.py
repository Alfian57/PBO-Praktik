from app.db import DB


class StudentRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(
        self,
        nis: str,
        name: str,
        password: str,
        phone_number: str,
        address: str,
        class_id: int,
    ):
        sql = "INSERT INTO students (nis, name, password, phone_number, address, class_id) VALUES (%s, %s, %s, %s, %s, %s)"
        self.db.execute(sql, (nis, name, password, phone_number, address, class_id))

    def get_all(self):
        sql = "SELECT * FROM students"
        return self.db.fetch_all(sql)

    def get_by_nis(self, nis: str):
        sql = "SELECT * FROM students WHERE nis = %s"
        return self.db.fetch_one(sql, (nis,))

    def get_by_id(self, id: int):
        sql = "SELECT * FROM students WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def update(
        self,
        id: int,
        nis: str,
        name: str,
        password: str,
        phone_number: str,
        address: str,
        class_id: int,
    ):
        sql = "UPDATE students SET nis = %s, name = %s, password = %s, phone_number = %s, address = %s, class_id = %s WHERE id = %s"
        self.db.execute(sql, (nis, name, password, phone_number, address, class_id, id))

    def delete(self, id: int):
        sql = "DELETE FROM students WHERE id = %s"
        self.db.execute(sql, (id,))
