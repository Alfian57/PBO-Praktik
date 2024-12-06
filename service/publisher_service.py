from repository.publisher_repository import PublisherRepository
from dto.publisher_dto import PublisherDTO
from helper.show_message import display_message


class PublisherService:
    def __init__(self):
        self.publisher_repository = PublisherRepository()

    def get_all_publishers(self):
        return self.publisher_repository.get_all()

    def add_publisher(self, publisher_dto: PublisherDTO):
        if not publisher_dto.name:
            display_message("Nama penerbit tidak boleh kosong!", "error")
            return

        self.publisher_repository.add(publisher_dto)
        display_message("Penerbit berhasil ditambahkan!", "info")

    def update_publisher(self, publisher_dto: PublisherDTO):
        if not publisher_dto.id:
            display_message("Pilih penerbit yang ingin diperbarui!", "error")
            return

        if not publisher_dto.name:
            display_message("Nama penerbit tidak boleh kosong!", "error")
            return

        self.publisher_repository.update(publisher_dto)
        display_message("Penerbit berhasil diperbarui!", "info")

    def delete_publisher(self, publisher_dto: PublisherDTO):
        if not publisher_dto.id:
            display_message("Pilih penerbit yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus penerbit ini?", "question"
        )
        if not confirm:
            return

        self.publisher_repository.delete(publisher_dto.id)
        display_message("Penerbit berhasil dihapus!", "info")
