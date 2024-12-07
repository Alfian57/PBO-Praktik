from repository.category_repository import CategoryRepository
from dto.category_dto import CategoryDTO


class CategorySeeder:
    def __init__(self) -> None:
        self.category_repository = CategoryRepository()

    def get_data(self):
        return [
            {"name": "Fiksi"},
            {"name": "Non-Fiksi"},
            {"name": "Komik"},
            {"name": "Novel"},
            {"name": "Pendidikan"},
            {"name": "Sejarah"},
            {"name": "Biografi"},
            {"name": "Agama"},
            {"name": "Teknologi"},
            {"name": "Kesehatan"},
            {"name": "Olahraga"},
            {"name": "Hobi"},
            {"name": "Kuliner"},
            {"name": "Travel"},
            {"name": "Fashion"},
            {"name": "Musik"},
            {"name": "Film"},
            {"name": "Seni"},
            {"name": "Politik"},
            {"name": "Ekonomi"},
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.category_repository.add(
                CategoryDTO(
                    name=dto["name"],
                )
            )
