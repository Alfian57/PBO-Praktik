from repository.publisher_repository import PublisherRepository
from dto.publisher_dto import PublisherDTO
from helper.show_message import display_message
from helper.validator import Validator


class PublisherService:
    def __init__(self):
        self.publisher_repository = PublisherRepository()

    def get_all_publishers(self):
        return self.publisher_repository.get_all()

    def add_publisher(self, publisher_dto: PublisherDTO):
        error_message = Validator.validate(
            publisher_dto.__dict__,
            {
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "name": "Nama Penerbit",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.publisher_repository.add(publisher_dto)
        display_message("Penerbit berhasil ditambahkan!", "info")

    def update_publisher(self, publisher_dto: PublisherDTO):
        error_message = Validator.validate(
            publisher_dto.__dict__,
            {
                "id": [Validator.required],
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "id": "ID Penerbit",
                "name": "Nama Penerbit",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.publisher_repository.update(publisher_dto)
        display_message("Penerbit berhasil diperbarui!", "info")

    def delete_publisher(self, publisher_dto: PublisherDTO):
        error_message = Validator.validate(
            publisher_dto.__dict__,
            {
                "id": [Validator.required],
            },
            {
                "id": "ID Penerbit",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus penerbit ini?", "question"
        )
        if not confirm:
            return

        self.publisher_repository.delete(publisher_dto.id)
        display_message("Penerbit berhasil dihapus!", "info")
