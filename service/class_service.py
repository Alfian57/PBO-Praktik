from repository.class_repository import ClassRepository
from dto.class_dto import ClassDTO
from helper.show_message import display_message
from helper.validator import Validator


class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()

    def get_all_classes(self):
        return self.class_repository.get_all()

    def add_class(self, class_dto: ClassDTO):
        error_message = Validator.validate(
            class_dto.__dict__,
            {
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "name": "Nama Kelas",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.class_repository.add(class_dto)
        display_message("Kelas berhasil ditambahkan!", "info")

    def update_class(self, class_dto: ClassDTO):
        error_message = Validator.validate(
            class_dto.__dict__,
            {
                "id": [Validator.required],
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "id": "ID Kelas",
                "name": "Nama Kelas",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.class_repository.update(class_dto)
        display_message("Kelas berhasil diperbarui!", "info")

    def delete_class(self, class_dto: ClassDTO):
        error_message = Validator.validate(
            class_dto.__dict__,
            {
                "id": [Validator.required],
            },
            {
                "id": "ID Kelas",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus kelas ini?", "question"
        )
        if not confirm:
            return

        self.class_repository.delete(class_dto.id)
        display_message("Kelas berhasil dihapus!", "info")
