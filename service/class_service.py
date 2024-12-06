from repository.class_repository import ClassRepository
from dto.class_dto import ClassDTO
from helper.show_message import display_message


class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()

    def get_all_classes(self):
        return self.class_repository.get_all()

    def add_class(self, class_dto: ClassDTO):
        if not class_dto.name:
            display_message("Nama kelas tidak boleh kosong!", "error")
            return

        self.class_repository.add(class_dto)
        display_message("Kelas berhasil ditambahkan!", "info")

    def update_class(self, class_dto: ClassDTO):
        if not class_dto.id:
            display_message("Pilih kelas yang ingin diperbarui!", "error")
            return

        if not class_dto.name:
            display_message("Nama kelas tidak boleh kosong!", "error")
            return

        self.class_repository.update(class_dto)
        display_message("Kelas berhasil diperbarui!", "info")

    def delete_class(self, class_dto: ClassDTO):
        if not class_dto.id:
            display_message("Pilih kelas yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus kelas ini?", "question"
        )
        if not confirm:
            return

        self.class_repository.delete(class_dto.id)
        display_message("Kelas berhasil dihapus!", "info")
