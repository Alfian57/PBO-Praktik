from repository.publisher_repository import PublisherRepository
from dto.publisher_dto import PublisherDTO


class PublisherSeeder:
    def __init__(self) -> None:
        self.publisher_repository = PublisherRepository()

    def get_data(self):
        return [
            {"name": "Yudhistira"},
            {"name": "Gramedia"},
            {"name": "Erlangga"},
            {"name": "Kompas"},
            {"name": "Republika"},
            {"name": "Tempo"},
            {"name": "Gatra"},
            {"name": "Suara Merdeka"},
            {"name": "Jawa Pos"},
            {"name": "Koran Jakarta"},
            {"name": "Koran Sindo"},
            {"name": "Koran Merdeka"},
            {"name": "Koran Kompas"},
            {"name": "Koran Republika"},
            {"name": "Koran Tempo"},
            {"name": "Koran Gatra"},
            {"name": "Koran Suara Merdeka"},
            {"name": "Koran Jawa Pos"},
            {"name": "Koran Tribun"},
            {"name": "Koran Bali Post"},
            {"name": "Koran Rakyat Merdeka"},
            {"name": "Koran Sinar Harapan"},
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.publisher_repository.add(
                PublisherDTO(
                    name=dto["name"],
                )
            )
