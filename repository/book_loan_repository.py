from app.db import DB
from dto.book_loan_dto import BookLoanDTO


class BookLoanRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance().get_instance()

    def add(self, book_loan_dto: BookLoanDTO) -> None:
        sql = "INSERT INTO book_loans (student_id, book_id, borrowing_date, return_date) VALUES (%s, %s, %s, %s)"
        self.db.execute(
            sql,
            (
                book_loan_dto.student_id,
                book_loan_dto.book_id,
                book_loan_dto.borrowing_date,
                book_loan_dto.return_date,
            ),
        )

    def get_all(self) -> list[BookLoanDTO]:
        sql = "SELECT * FROM book_loans"
        results = self.db.fetch_all(sql)
        return [BookLoanDTO(*result) for result in results]

    def get_all_with_student_and_book(self) -> list[BookLoanDTO]:
        sql = """
            SELECT book_loans.id, books.title, students.name, book_loans.borrowing_date, book_loans.return_date
            FROM book_loans
            JOIN students ON book_loans.student_id = students.id
            JOIN books ON book_loans.book_id = books.id
        """
        results = self.db.fetch_all(sql)
        return [
            BookLoanDTO(
                id=result[0],
                book_name=result[1],
                student_name=result[2],
                borrowing_date=result[3],
                return_date=result[4],
            )
            for result in results
        ]

    def get_by_id(self, id: int) -> BookLoanDTO:
        sql = "SELECT * FROM book_loans WHERE id = %s"
        result = self.db.fetch_one(sql, (id,))
        return BookLoanDTO(*result) if result else None

    def get_by_student_id(self, student_id: int) -> list[BookLoanDTO]:
        sql = "SELECT * FROM book_loans WHERE student_id = %s"
        results = self.db.fetch_all(sql, (student_id,))
        return [BookLoanDTO(*result) for result in results]

    def get_by_book_id(self, book_id: int) -> list[BookLoanDTO]:
        sql = "SELECT * FROM book_loans WHERE book_id = %s"
        results = self.db.fetch_all(sql, (book_id,))
        return [BookLoanDTO(*result) for result in results]

    def update(self, book_loan_dto: BookLoanDTO) -> None:
        sql = "UPDATE book_loans SET student_id = %s, book_id = %s, borrowing_date = %s, return_date = %s WHERE id = %s"
        self.db.execute(
            sql,
            (
                book_loan_dto.student_id,
                book_loan_dto.book_id,
                book_loan_dto.borrowing_date,
                book_loan_dto.return_date,
                book_loan_dto.id,
            ),
        )

    def delete(self, id: int) -> None:
        sql = "DELETE FROM book_loans WHERE id = %s"
        self.db.execute(sql, (id,))
