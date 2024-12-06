from app.db import DB
from dto.admin_dto import AdminDTO


class AdminRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, admin_dto: AdminDTO) -> None:
        sql = "INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)"
        self.db.execute(sql, (admin_dto.name, admin_dto.email, admin_dto.password))

    def get_all(self) -> list[AdminDTO]:
        sql = "SELECT * FROM admins"
        result = self.db.fetch_all(sql)
        return [AdminDTO(**row) for row in result]

    def get_by_id(self, id: int) -> AdminDTO:
        sql = "SELECT * FROM admins WHERE id = %s"
        result = self.db.fetch_one(sql, (id,))
        return AdminDTO(**result) if result else None

    def get_by_email(self, email: str) -> AdminDTO:
        sql = "SELECT * FROM admins WHERE email = %s"
        result = self.db.fetch_one(sql, (email,))
        return AdminDTO(**result) if result else None

    def update(self, id: int, admin_dto: AdminDTO) -> None:
        sql = "UPDATE admins SET name = %s, email = %s, password = %s WHERE id = %s"
        self.db.execute(sql, (admin_dto.name, admin_dto.email, admin_dto.password, id))

    def delete(self, id: int) -> None:
        sql = "DELETE FROM admins WHERE id = %s"
        self.db.execute(sql, (id,))
