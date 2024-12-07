from repository.book_repository import BookRepository
from repository.publisher_repository import PublisherRepository
from repository.category_repository import CategoryRepository
from dto.book_dto import BookDTO
from helper.show_message import display_message
from helper.validator import Validator


class BookService:
    def __init__(self):
        self.book_repository = BookRepository()
        self.category_repository = CategoryRepository()
        self.publisher_repository = PublisherRepository()

    def get_all_categories(self):
        return self.category_repository.get_all()

    def get_all_publishers(self):
        return self.publisher_repository.get_all()

    def get_all_books(self):
        return self.book_repository.get_all_with_category_and_publisher()

    def add_book(self, book_dto: BookDTO):
        error_message = Validator.validate(
            book_dto.__dict__,
            {
                "title": [Validator.required, Validator.max_length(100)],
                "isbn": [Validator.required, Validator.max_length(25)],
                "category_id": [Validator.required],
                "publisher_id": [Validator.required],
                "publish_year": [Validator.required, Validator.year],
            },
            {
                "title": "Judul",
                "isbn": "ISBN",
                "category_id": "Kategori",
                "publisher_id": "Penerbit",
                "publish_year": "Tahun Terbit",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.book_repository.add(book_dto)
        display_message("Buku berhasil ditambahkan!", "info")

    def update_book(self, book_dto: BookDTO):
        error_message = Validator.validate(
            book_dto.__dict__,
            {
                "id": [Validator.required],
                "title": [Validator.required, Validator.max_length(100)],
                "isbn": [Validator.required, Validator.max_length(25)],
                "category_id": [Validator.required],
                "publisher_id": [Validator.required],
                "publish_year": [Validator.required, Validator.year],
            },
            {
                "id": "ID",
                "title": "Judul",
                "isbn": "ISBN",
                "category_id": "Kategori",
                "publisher_id": "Penerbit",
                "publish_year": "Tahun Terbit",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.book_repository.update(book_dto)
        display_message("Buku berhasil diperbarui!", "info")

    def delete_book(self, book_dto: BookDTO):
        error_message = Validator.validate(
            book_dto.__dict__, {"id": [Validator.required]}, {"id": "ID"}
        )

        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus buku ini?", "question"
        )
        if not confirm:
            return

        self.book_repository.delete(book_dto.id)
        display_message("Buku berhasil dihapus!", "info")
