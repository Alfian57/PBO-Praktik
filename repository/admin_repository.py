from app.db import DB


class AdminRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, name: str, email: str, password: str):
        sql = "INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)"
        self.db.execute(sql, (name, email, password))

    def get_all(self):
        sql = "SELECT * FROM admins"
        return self.db.fetch_all(sql)

    def get_by_id(self, id: int):
        sql = "SELECT * FROM admins WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def get_by_email(self, email: str):
        sql = "SELECT * FROM admins WHERE email = %s"
        return self.db.fetch_one(sql, (email,))

    def update(self, id: int, name: str, email: str, password: str):
        sql = "UPDATE admins SET name = %s, email = %s, password = %s WHERE id = %s"
        self.db.execute(sql, (name, email, password, id))

    def delete(self, id: int):
        sql = "DELETE FROM admins WHERE id = %s"
        self.db.execute(sql, (id,))
