from repository.book_repository import BookRepository
from repository.publisher_repository import PublisherRepository
from repository.category_repository import CategoryRepository
from dto.book_dto import BookDTO
from helper.show_message import display_message


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
        if (
            not book_dto.title
            or not book_dto.isbn
            or not book_dto.category_id
            or not book_dto.publisher_id
            or not book_dto.publish_year
        ):
            display_message("Data buku tidak boleh kosong!", "error")
            return

        self.book_repository.add(book_dto)
        display_message("Buku berhasil ditambahkan!", "info")

    def update_book(self, book_dto: BookDTO):
        if not book_dto.id:
            display_message("Pilih buku yang ingin diperbarui!", "error")
            return

        if (
            not book_dto.title
            or not book_dto.isbn
            or not book_dto.category_id
            or not book_dto.publisher_id
            or not book_dto.publish_year
        ):
            display_message("Data buku tidak boleh kosong!", "error")
            return

        self.book_repository.update(book_dto)
        display_message("Buku berhasil diperbarui!", "info")

    def delete_book(self, book_dto: BookDTO):
        if not book_dto.id:
            display_message("Pilih buku yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus buku ini?", "question"
        )
        if not confirm:
            return

        self.book_repository.delete(book_dto.id)
        display_message("Buku berhasil dihapus!", "info")
