from repository.book_loan_repository import BookLoanRepository
from dto.book_loan_dto import BookLoanDTO
import random


class BookLoanSeeder:
    def __init__(self) -> None:
        self.book_loan_repository = BookLoanRepository()

    def get_data(self):
        return [
            {"borrowing_date": "2021-01-01", "return_date": "2021-01-08"},
            {"borrowing_date": "2021-01-02", "return_date": "2021-01-09"},
            {"borrowing_date": "2021-01-03", "return_date": "2021-01-10"},
            {"borrowing_date": "2021-01-04", "return_date": "2021-01-11"},
            {"borrowing_date": "2021-01-05", "return_date": "2021-01-12"},
            {"borrowing_date": "2021-01-06", "return_date": "2021-01-13"},
            {"borrowing_date": "2021-01-07", "return_date": "2021-01-14"},
            {"borrowing_date": "2021-01-08", "return_date": "2021-01-15"},
            {"borrowing_date": "2021-01-09", "return_date": "2021-01-16"},
            {"borrowing_date": "2021-01-10", "return_date": "2021-01-17"},
            {"borrowing_date": "2021-01-11", "return_date": "2021-01-18"},
            {"borrowing_date": "2021-01-12", "return_date": "2021-01-19"},
            {"borrowing_date": "2021-01-13", "return_date": "2021-01-20"},
            {"borrowing_date": "2021-01-14", "return_date": "2021-01-21"},
            {"borrowing_date": "2021-01-15", "return_date": "2021-01-22"},
            {"borrowing_date": "2021-01-16", "return_date": "2021-01-23"},
            {"borrowing_date": "2021-01-17", "return_date": "2021-01-24"},
            {"borrowing_date": "2021-01-18", "return_date": "2021-01-25"},
            {"borrowing_date": "2021-01-19", "return_date": "2021-01-26"},
            {"borrowing_date": "2021-01-20", "return_date": "2021-01-27"},
            {"borrowing_date": "2021-01-21", "return_date": "2021-01-28"},
            {"borrowing_date": "2021-01-22", "return_date": "2021-01-29"},
            {"borrowing_date": "2021-01-23", "return_date": "2021-01-30"},
            {"borrowing_date": "2021-01-24", "return_date": "2021-01-31"},
            {"borrowing_date": "2021-01-25", "return_date": "2021-02-01"},
            {"borrowing_date": "2021-01-26", "return_date": "2021-02-02"},
            {"borrowing_date": "2021-01-27", "return_date": "2021-02-03"},
            {"borrowing_date": "2021-01-28", "return_date": "2021-02-04"},
            {"borrowing_date": "2021-01-29", "return_date": "2021-02-05"},
            {"borrowing_date": "2021-01-30", "return_date": "2021-02-06"},
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.book_loan_repository.add(
                BookLoanDTO(
                    borrowing_date=dto["borrowing_date"],
                    return_date=dto["return_date"],
                    book_id=random.randint(1, 20),
                    student_id=random.randint(1, 10),
                )
            )
