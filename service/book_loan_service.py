from repository.student_repository import StudentRepository
from repository.book_loan_repository import BookLoanRepository
from repository.book_repository import BookRepository
from dto.book_loan_dto import BookLoanDTO
from helper.show_message import display_message
from helper.validator import Validator


class BookLoanService:
    def __init__(self):
        self.book_loan_repository = BookLoanRepository()
        self.book_repository = BookRepository()
        self.student_repository = StudentRepository()

    def get_all_students(self):
        return self.student_repository.get_all()

    def get_all_books(self):
        return self.book_repository.get_all()

    def get_all_book_loan_with_student_and_book(self):
        return self.book_loan_repository.get_all_with_student_and_book()

    def add_book_loan(self, book_loan_dto: BookLoanDTO):
        error_message = Validator.validate(
            book_loan_dto.__dict__,
            {
                "book_id": [Validator.required],
                "student_id": [Validator.required],
                "borrowing_date": [Validator.required, Validator.date],
                "return_date": [Validator.required, Validator.date],
            },
            {
                "book_id": "ID Buku",
                "student_id": "ID Siswa",
                "borrowing_date": "Tanggal Pinjam",
                "return_date": "Tanggal Kembali",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.book_loan_repository.add(book_loan_dto)
        display_message("Peminjaman buku berhasil ditambahkan!", "info")

    def update_book_loan(self, book_loan_dto: BookLoanDTO):
        error_message = Validator.validate(
            book_loan_dto.__dict__,
            {
                "id": [Validator.required],
                "book_id": [Validator.required],
                "student_id": [Validator.required],
                "borrowing_date": [Validator.required, Validator.date],
                "return_date": [Validator.required, Validator.date],
            },
            {
                "id": "ID Peminjaman",
                "book_id": "ID Buku",
                "student_id": "ID Siswa",
                "borrowing_date": "Tanggal Pinjam",
                "return_date": "Tanggal Kembali",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.book_loan_repository.update(book_loan_dto)
        display_message("Peminjaman buku berhasil diperbarui!", "info")

    def delete_book_loan(self, book_loan_dto: BookLoanDTO):
        error_message = Validator.validate(
            book_loan_dto.__dict__,
            {
                "id": [Validator.required],
            },
            {
                "id": "ID Peminjaman",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus peminjaman buku ini?", "question"
        )
        if not confirm:
            return

        self.book_loan_repository.delete(book_loan_dto.id)
        display_message("Peminjaman buku berhasil dihapus!", "info")
