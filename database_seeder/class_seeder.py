from repository.class_repository import ClassRepository
from dto.class_dto import ClassDTO


class ClassSeeder:
    def __init__(self) -> None:
        self.class_repository = ClassRepository()

    def get_data(self):
        return [
            {"name": "Informatika A"},
            {"name": "Informatika B"},
            {"name": "Informatika C"},
            {"name": "Informatika D"},
            {"name": "Informatika E"},
            {"name": "Sistem Informasi A"},
            {"name": "Sistem Informasi B"},
            {"name": "Sistem Informasi C"},
            {"name": "Sistem Informasi D"},
            {"name": "Sistem Informasi E"},
            {"name": "Psikologi A"},
            {"name": "Psikologi B"},
            {"name": "Psikologi C"},
            {"name": "Psikologi D"},
            {"name": "Psikologi E"},
            {"name": "Hukum A"},
            {"name": "Hukum B"},
            {"name": "Hukum C"},
            {"name": "Hukum D"},
            {"name": "Hukum E"},
            {"name": "Teknik Sipil A"},
            {"name": "Teknik Sipil B"},
            {"name": "Teknik Sipil C"},
            {"name": "Teknik Sipil D"},
            {"name": "Teknik Sipil E"},
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.class_repository.add(
                ClassDTO(
                    name=dto["name"],
                )
            )
