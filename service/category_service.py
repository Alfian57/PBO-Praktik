from repository.category_repository import CategoryRepository
from dto.category_dto import CategoryDTO
from helper.show_message import display_message


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def get_all_categories(self):
        return self.category_repository.get_all()

    def add_category(self, category_dto: CategoryDTO):
        if not category_dto.name:
            display_message("Nama kategori tidak boleh kosong!", "error")
            return

        self.category_repository.add(category_dto)
        display_message("Kategori berhasil ditambahkan!", "info")

    def update_category(self, category_dto: CategoryDTO):
        if not category_dto.id:
            display_message("Pilih kategori yang ingin diperbarui!", "error")
            return

        if not category_dto.name:
            display_message("Nama kategori tidak boleh kosong!", "error")
            return

        self.category_repository.update(category_dto)
        display_message("Kategori berhasil diperbarui!", "info")

    def delete_category(self, category_dto: CategoryDTO):
        if not category_dto.id:
            display_message("Pilih kategori yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus kategori ini?", "question"
        )
        if not confirm:
            return

        self.category_repository.delete(category_dto.id)
        display_message("Kategori berhasil dihapus!", "info")
