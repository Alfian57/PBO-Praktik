from repository.student_repository import StudentRepository
from dto.student_dto import StudentDTO
import random


class StudentSeeder:
    def __init__(self) -> None:
        self.student_repository = StudentRepository()

    def get_data(self):
        return [
            {
                "nis": "11111",
                "name": "Gading",
                "phone_number": "08123456789",
                "address": "Jl. Gading",
            },
            {
                "nis": "11112",
                "name": "Rizki",
                "phone_number": "08123456789",
                "address": "Jl. Rizki",
            },
            {
                "nis": "11113",
                "name": "Rizal",
                "phone_number": "08123456789",
                "address": "Jl. Rizal",
            },
            {
                "nis": "11114",
                "name": "Arfan",
                "phone_number": "08123456789",
                "address": "Jl. Arfan",
            },
            {
                "nis": "11115",
                "name": "Fikri",
                "phone_number": "08123456789",
                "address": "Jl. Fikri",
            },
            {
                "nis": "11116",
                "name": "Rasyid",
                "phone_number": "08123456789",
                "address": "Jl. Rasyid",
            },
            {
                "nis": "11117",
                "name": "Rangga",
                "phone_number": "08123456789",
                "address": "Jl. Rangga",
            },
            {
                "nis": "11118",
                "name": "Kunaka",
                "phone_number": "08123456789",
                "address": "Jl. Kunaka",
            },
            {
                "nis": "11119",
                "name": "Rizal",
                "phone_number": "08123456789",
                "address": "Jl. Rizal",
            },
            {
                "nis": "11120",
                "name": "Satya",
                "phone_number": "08123456789",
                "address": "Jl. Satya",
            },
        ]

    def run(self) -> None:
        data = self.get_data()

        for dto in data:
            self.student_repository.add(
                StudentDTO(
                    nis=dto["nis"],
                    name=dto["name"],
                    phone_number=dto["phone_number"],
                    address=dto["address"],
                    class_id=random.randint(1, 25),
                )
            )
