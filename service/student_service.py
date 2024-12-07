from repository.student_repository import StudentRepository
from repository.class_repository import ClassRepository
from dto.student_dto import StudentDTO
from helper.show_message import display_message
from helper.validator import Validator


class StudentService:
    def __init__(self):
        self.student_repository = StudentRepository()
        self.class_repository = ClassRepository()

    def get_all_classes(self):
        return self.class_repository.get_all()

    def get_all_students_with_class(self):
        return self.student_repository.get_all_with_class()

    def add_student(self, studentDto: StudentDTO):
        error_message = Validator.validate(
            studentDto.__dict__,
            {
                "name": [Validator.required, Validator.max_length(100)],
                "nis": [Validator.required, Validator.length(5)],
                "phone_number": [Validator.required, Validator.max_length(25)],
                "address": [Validator.required],
                "class_id": [Validator.required],
            },
            {
                "name": "Nama",
                "nis": "NIS",
                "phone_number": "Nomor Telepon",
                "address": "Alamat",
                "class_id": "Kelas",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.student_repository.add(studentDto)
        display_message("siswa berhasil ditambahkan!", "info")

    def update_student(self, studentDto: StudentDTO):
        error_message = Validator.validate(
            studentDto.__dict__,
            {
                "name": [Validator.required, Validator.max_length(100)],
                "nis": [Validator.required, Validator.length(5)],
                "phone_number": [Validator.required, Validator.max_length(25)],
                "address": [Validator.required],
                "class_id": [Validator.required],
            },
            {
                "name": "Nama",
                "nis": "NIS",
                "phone_number": "Nomor Telepon",
                "address": "Alamat",
                "class_id": "Kelas",
            },
        )
        if error_message:
            display_message(error_message, "error")
            return

        self.student_repository.update(studentDto)
        display_message("siswa berhasil diperbarui!", "info")

    def delete_student(self, studentDto: StudentDTO):
        error_message = Validator.validate(
            studentDto.__dict__,
            {"id": [Validator.required]},
            {"id": "ID"},
        )
        if error_message:
            display_message(error_message, "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus siswa ini?", "question"
        )
        if not confirm:
            return

        self.student_repository.delete(studentDto.id)
        display_message("siswa berhasil dihapus!", "info")
