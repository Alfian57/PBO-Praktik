from repository.admin_repository import AdminRepository
from dto.admin_dto import AdminDTO
import bcrypt


class AdminSeeder:
    def __init__(self) -> None:
        self.admin_repository = AdminRepository()

    def get_data(self):
        return [
            {"name": "Admin", "email": "admin@gmail.com", "password": "password"},
            {"name": "Alfian", "email": "alfian@gmail.com", "password": "password"},
            {"name": "Rasyid", "email": "rasyid@gmail.com", "password": "password"},
            {"name": "Arfan", "email": "arfan@gmail.com", "password": "password"},
            {"name": "Rangga", "email": "rangga@gmail.com", "password": "password"},
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.admin_repository.add(
                AdminDTO(
                    name=dto["name"],
                    email=dto["email"],
                    password=bcrypt.hashpw(
                        dto["password"].encode(), bcrypt.gensalt()
                    ).decode(),
                )
            )
