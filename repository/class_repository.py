from app.db import DB
from dto.class_dto import ClassDTO


class ClassRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, class_dto: ClassDTO) -> None:
        sql = "INSERT INTO class (name) VALUES (%s)"
        self.db.execute(sql, (class_dto.name,))

    def get_all(self) -> list[ClassDTO]:
        sql = "SELECT * FROM class"
        rows = self.db.fetch_all(sql)
        return [ClassDTO(id=row[0], name=row[1], created_at=row[2]) for row in rows]

    def get_by_id(self, id: int) -> ClassDTO:
        sql = "SELECT * FROM class WHERE id = %s"
        row = self.db.fetch_one(sql, (id,))
        if row:
            return ClassDTO(id=row[0], name=row[1], created_at=row[2])
        return None

    def update(self, class_dto: ClassDTO) -> None:
        sql = "UPDATE class SET name = %s WHERE id = %s"
        self.db.execute(sql, (class_dto.name, class_dto.id))

    def delete(self, id: int) -> None:
        sql = "DELETE FROM class WHERE id = %s"
        self.db.execute(sql, (id,))
