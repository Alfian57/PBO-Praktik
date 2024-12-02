from app.db import DB


class BookLoanRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, student_id: int, book_id: int, borrowing_date: str, return_date: str):
        sql = "INSERT INTO book_loans (student_id, book_id, borrowing_date, return_date) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql, (student_id, book_id, borrowing_date, return_date))

    def get_all(self):
        sql = "SELECT * FROM book_loans"
        return self.db.fetch_all(sql)

    def get_by_id(self, id: int):
        sql = "SELECT * FROM book_loans WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def get_by_student_id(self, student_id: int):
        sql = "SELECT * FROM book_loans WHERE student_id = %s"
        return self.db.fetch_all(sql, (student_id,))

    def get_by_book_id(self, book_id: int):
        sql = "SELECT * FROM book_loans WHERE book_id = %s"
        return self.db.fetch_all(sql, (book_id,))

    def update(
        self,
        id: int,
        student_id: int,
        book_id: int,
        borrowing_date: str,
        return_date: str,
    ):
        sql = "UPDATE book_loans SET student_id = %s, book_id = %s, borrowing_date = %s, return_date = %s WHERE id = %s"
        self.db.execute(sql, (student_id, book_id, borrowing_date, return_date, id))

    def delete(self, id: int):
        sql = "DELETE FROM book_loans WHERE id = %s"
        self.db.execute(sql, (id,))
