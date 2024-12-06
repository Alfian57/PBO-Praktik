from app.db import DB
from dto.book_dto import BookDTO


class BookRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, book_dto: BookDTO) -> None:
        sql = "INSERT INTO books (title, isbn, category_id, publisher_id, publish_year) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(
            sql,
            (
                book_dto.title,
                book_dto.isbn,
                book_dto.category_id,
                book_dto.publisher_id,
                book_dto.publish_year,
            ),
        )

    def get_all(self) -> list[BookDTO]:
        sql = "SELECT books.id, books.title, books.isbn, books.publish_year, books.created_at, books.category_id, books.publisher_id FROM books"

        result = self.db.fetch_all(sql)
        return [
            BookDTO(
                id=row[0],
                title=row[1],
                isbn=row[2],
                publish_year=row[3],
                created_at=row[4],
                category_id=row[5],
                publisher_id=row[6],
            )
            for row in result
        ]

    def get_all_with_category_and_publisher(self) -> list[BookDTO]:
        sql = """
        SELECT b.id, b.title, b.isbn, b.publish_year, b.category_id, b.publisher_id, c.name AS category, p.name AS publisher
        FROM books b
        JOIN categories c ON b.category_id = c.id
        JOIN publishers p ON b.publisher_id = p.id
        """
        result = self.db.fetch_all(sql)
        return [
            BookDTO(
                id=row[0],
                title=row[1],
                isbn=row[2],
                publish_year=row[3],
                category_name=row[6],
                publisher_name=row[7],
            )
            for row in result
        ]

    def get_by_id(self, id: int) -> BookDTO:
        sql = "SELECT * FROM books WHERE id = %s"
        result = self.db.fetch_one(sql, (id,))
        return BookDTO(**result) if result else None

    def update(self, book_dto: BookDTO) -> None:
        sql = "UPDATE books SET title = %s, isbn = %s, category_id = %s, publisher_id = %s, publish_year = %s WHERE id = %s"
        self.db.execute(
            sql,
            (
                book_dto.title,
                book_dto.isbn,
                book_dto.category_id,
                book_dto.publisher_id,
                book_dto.publish_year,
                book_dto.id,
            ),
        )

    def delete(self, id: int) -> None:
        sql = "DELETE FROM books WHERE id = %s"
        self.db.execute(sql, (id,))
