from app.db import DB
from dto.admin_dto import AdminDTO


class AdminRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, admin_dto: AdminDTO) -> None:
        sql = "INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)"
        self.db.execute(sql, (admin_dto.name, admin_dto.email, admin_dto.password))

    def get_all(self) -> list[AdminDTO]:
        sql = "SELECT id, name, email, created_at FROM admins"
        result = self.db.fetch_all(sql)
        return [
            AdminDTO(id=row[0], name=row[1], email=row[2], created_at=row[3])
            for row in result
        ]

    def get_by_id(self, id: int) -> AdminDTO:
        sql = "SELECT id, name, email, created_at FROM admins WHERE id = %s"
        result = self.db.fetch_one(sql, (id,))
        return (
            AdminDTO(
                id=result[0], name=result[1], email=result[2], created_at=result[3]
            )
            if result
            else None
        )

    def get_by_email(self, email: str) -> AdminDTO:
        sql = "SELECT id, name, email, created_at FROM admins WHERE email = %s"
        result = self.db.fetch_one(sql, (email,))
        return (
            AdminDTO(
                id=result[0], name=result[1], email=result[2], created_at=result[3]
            )
            if result
            else None
        )

    def update(self, id: int, admin_dto: AdminDTO) -> None:
        sql = "UPDATE admins SET name = %s, email = %s, password = %s WHERE id = %s"
        self.db.execute(sql, (admin_dto.name, admin_dto.email, admin_dto.password, id))

    def delete(self, id: int) -> None:
        sql = "DELETE FROM admins WHERE id = %s"
        self.db.execute(sql, (id,))
