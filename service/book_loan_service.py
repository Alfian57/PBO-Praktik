from repository.student_repository import StudentRepository
from repository.book_loan_repository import BookLoanRepository
from repository.book_repository import BookRepository
from dto.book_loan_dto import BookLoanDTO
from helper.show_message import display_message


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
        if not book_loan_dto.book_id:
            display_message("ID buku tidak boleh kosong!", "error")
            return

        if not book_loan_dto.student_id:
            display_message("ID siswa tidak boleh kosong!", "error")
            return

        self.book_loan_repository.add(book_loan_dto)
        display_message("Peminjaman buku berhasil ditambahkan!", "info")

    def update_book_loan(self, book_loan_dto: BookLoanDTO):
        if not book_loan_dto.id:
            display_message("Pilih peminjaman buku yang ingin diperbarui!", "error")
            return

        if not book_loan_dto.book_id:
            display_message("ID buku tidak boleh kosong!", "error")
            return

        if not book_loan_dto.student_id:
            display_message("ID siswa tidak boleh kosong!", "error")
            return

        self.book_loan_repository.update(book_loan_dto)
        display_message("Peminjaman buku berhasil diperbarui!", "info")

    def delete_book_loan(self, book_loan_dto: BookLoanDTO):
        if not book_loan_dto.id:
            display_message("Pilih peminjaman buku yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus peminjaman buku ini?", "question"
        )
        if not confirm:
            return

        self.book_loan_repository.delete(book_loan_dto.id)
        display_message("Peminjaman buku berhasil dihapus!", "info")
