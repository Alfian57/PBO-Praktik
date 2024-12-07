from repository.category_repository import CategoryRepository
from dto.category_dto import CategoryDTO
from helper.show_message import display_message
from helper.validator import Validator


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def get_all_categories(self):
        return self.category_repository.get_all()

    def add_category(self, category_dto: CategoryDTO):
        error_message = Validator.validate(
            category_dto.__dict__,
            {
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "name": "Nama Kategori",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.category_repository.add(category_dto)
        display_message("Kategori berhasil ditambahkan!", "info")

    def update_category(self, category_dto: CategoryDTO):
        error_message = Validator.validate(
            category_dto.__dict__,
            {
                "id": [Validator.required],
                "name": [Validator.required, Validator.max_length(100)],
            },
            {
                "id": "ID Kategori",
                "name": "Nama Kategori",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.category_repository.update(category_dto)
        display_message("Kategori berhasil diperbarui!", "info")

    def delete_category(self, category_dto: CategoryDTO):
        error_message = Validator.validate(
            category_dto.__dict__,
            {
                "id": [Validator.required],
            },
            {
                "id": "ID Kategori",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus kategori ini?", "question"
        )
        if not confirm:
            return

        self.category_repository.delete(category_dto.id)
        display_message("Kategori berhasil dihapus!", "info")
