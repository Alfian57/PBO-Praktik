from app.db import DB
from dto.category_dto import CategoryDTO


class CategoryRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, category: CategoryDTO) -> None:
        sql = "INSERT INTO categories (name, created_at) VALUES (%s, %s)"
        self.db.execute(sql, (category.name, category.created_at))

    def get_all(self) -> list[CategoryDTO]:
        sql = "SELECT id, name, created_at FROM categories"
        rows = self.db.fetch_all(sql)
        return [CategoryDTO(id=row[0], name=row[1], created_at=row[2]) for row in rows]

    def get_by_id(self, id: int) -> CategoryDTO:
        sql = "SELECT id, name, created_at FROM categories WHERE id = %s"
        row = self.db.fetch_one(sql, (id,))
        if row:
            return CategoryDTO(id=row[0], name=row[1], created_at=row[2])
        return None

    def update(self, category: CategoryDTO) -> None:
        sql = "UPDATE categories SET name = %s WHERE id = %s"
        self.db.execute(sql, (category.name, category.id))

    def delete(self, id: int) -> None:
        sql = "DELETE FROM categories WHERE id = %s"
        self.db.execute(sql, (id,))
