from app.db import DB
from dto.publisher_dto import PublisherDTO


class PublisherRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, publisher_dto: PublisherDTO) -> None:
        sql = "INSERT INTO publishers (name) VALUES (%s)"
        self.db.execute(sql, (publisher_dto.name,))

    def get_all(self) -> list[PublisherDTO]:
        sql = "SELECT * FROM publishers"
        rows = self.db.fetch_all(sql)
        return [PublisherDTO(id=row[0], name=row[1], created_at=row[2]) for row in rows]

    def get_by_id(self, id: int) -> PublisherDTO:
        sql = "SELECT * FROM publishers WHERE id = %s"
        row = self.db.fetch_one(sql, (id,))
        if row:
            return PublisherDTO(id=row[0], name=row[1], created_at=row[2])
        return None

    def update(self, publisher_dto: PublisherDTO) -> None:
        sql = "UPDATE publishers SET name = %s WHERE id = %s"
        self.db.execute(sql, (publisher_dto.name, publisher_dto.id))

    def delete(self, id: int) -> None:
        sql = "DELETE FROM publishers WHERE id = %s"
        self.db.execute(sql, (id,))
