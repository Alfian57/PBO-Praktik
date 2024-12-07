from repository.admin_repository import AdminRepository
from dto.admin_dto import AdminDTO
from helper.show_message import display_message
from bcrypt import checkpw
from helper.validator import Validator


class LoginService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    def validate_login(self, admin_dto: AdminDTO) -> bool:
        error_message = Validator.validate(
            admin_dto.__dict__,
            {
                "email": [Validator.required, Validator.email],
                "password": [Validator.required],
            },
            {"email": "Email", "password": "Password"},
        )
        if error_message:
            display_message(error_message, "error")
            return False

        admin_data = self.admin_repository.get_by_email(admin_dto.email)

        if not admin_data:
            display_message("Email tidak ditemukan!", "error")
            return False

        if not checkpw(
            admin_dto.password.encode("utf-8"), admin_data.password.encode("utf-8")
        ):
            display_message("Password salah!", "error")
            return False

        display_message("Login berhasil!", "info")
        return True
