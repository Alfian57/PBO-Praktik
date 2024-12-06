from repository.student_repository import StudentRepository
from repository.class_repository import ClassRepository
from dto.student_dto import StudentDTO
from helper.show_message import display_message


class StudentService:
    def __init__(self):
        self.student_repository = StudentRepository()
        self.class_repository = ClassRepository()

    def get_all_classes(self):
        return self.class_repository.get_all()

    def get_all_students_with_class(self):
        return self.student_repository.get_all_with_class()

    def add_student(self, studentDto: StudentDTO):
        if (
            not studentDto.name
            or not studentDto.nis
            or not studentDto.phone_number
            or not studentDto.address
            or not studentDto.class_id
        ):
            display_message("Data siswa tidak boleh kosong!", "error")
            return

        self.student_repository.add(studentDto)
        display_message("siswa berhasil ditambahkan!", "info")

    def update_student(self, studentDto: StudentDTO):
        if not studentDto.id:
            display_message("Pilih siswa yang ingin diperbarui!", "error")
            return

        if (
            not studentDto.name
            or not studentDto.nis
            or not studentDto.phone_number
            or not studentDto.address
            or not studentDto.class_id
        ):
            display_message("Data siswa tidak boleh kosong!", "error")
            return

        self.student_repository.update(studentDto)
        display_message("siswa berhasil diperbarui!", "info")

    def delete_student(self, studentDto: StudentDTO):
        if not studentDto.id:
            display_message("Pilih siswa yang ingin dihapus!", "error")
            return

        confirm = display_message(
            "Apakah Anda yakin ingin menghapus siswa ini?", "question"
        )
        if not confirm:
            return

        self.student_repository.delete(studentDto.id)
        display_message("siswa berhasil dihapus!", "info")
