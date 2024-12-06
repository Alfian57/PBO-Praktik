from app.db import DB
from dto.student_dto import StudentDTO


class StudentRepository:
    def __init__(self) -> None:
        self.db = DB.get_instance()

    def add(self, student_dto: StudentDTO) -> None:
        sql = "INSERT INTO students (nis, name, phone_number, address, class_id) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(
            sql,
            (
                student_dto.nis,
                student_dto.name,
                student_dto.phone_number,
                student_dto.address,
                student_dto.class_id,
            ),
        )

    def get_all(self) -> list[StudentDTO]:
        sql = "SELECT * FROM students"
        result = self.db.fetch_all(sql)
        return [
            StudentDTO(
                id=row[0],
                nis=row[1],
                name=row[2],
                phone_number=row[4],
                address=row[5],
                class_id=row[6],
            )
            for row in result
        ]

    def get_all_with_class(self) -> list[StudentDTO]:
        sql = "SELECT s.id, s.nis, s.name, s.phone_number, s.address, s.class_id, c.name as class_name FROM students s JOIN class c ON s.class_id = c.id"
        result = self.db.fetch_all(sql)
        return [
            StudentDTO(
                id=row[0],
                nis=row[1],
                name=row[2],
                phone_number=row[3],
                address=row[4],
                class_id=row[5],
                class_name=row[6],
            )
            for row in result
        ]

    def get_by_nis(self, nis: str) -> StudentDTO:
        sql = "SELECT * FROM students WHERE nis = %s"
        return self.db.fetch_one(sql, (nis,))

    def get_by_id(self, id: int) -> StudentDTO:
        sql = "SELECT * FROM students WHERE id = %s"
        return self.db.fetch_one(sql, (id,))

    def update(self, student_dto: StudentDTO) -> None:
        sql = "UPDATE students SET nis = %s, name = %s, phone_number = %s, address = %s, class_id = %s WHERE id = %s"
        self.db.execute(
            sql,
            (
                student_dto.nis,
                student_dto.name,
                student_dto.phone_number,
                student_dto.address,
                student_dto.class_id,
                student_dto.id,
            ),
        )

    def delete(self, id: int) -> None:
        sql = "DELETE FROM students WHERE id = %s"
        self.db.execute(sql, (id,))
