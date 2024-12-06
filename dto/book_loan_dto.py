from datetime import datetime


class BookLoanDTO:
    def __init__(
        self,
        id=None,
        book_name=None,
        student_name=None,
        borrowing_date=None,
        return_date=None,
        created_at=None,
        book_id=None,
        student_id=None,
    ):
        self.id = id
        self.book_name = book_name
        self.student_name = student_name
        self.borrowing_date = borrowing_date
        self.return_date = return_date
        self.created_at = created_at or datetime.now()
        self.book_id = book_id
        self.student_id = student_id

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "student_name": self.student_name,
            "borrowing_date": self.borrowing_date,
            "return_date": self.return_date,
            "created_at": self.created_at,
            "book_id": self.book_id,
            "student_id": self.student_id,
        }
