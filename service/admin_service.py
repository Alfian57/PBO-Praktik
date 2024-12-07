from repository.admin_repository import AdminRepository
from dto.admin_dto import AdminDTO
from helper.show_message import display_message
from bcrypt import checkpw


class AdminService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    def validate_login(self, admin_dto: AdminDTO):
        admin_data = self.admin_repository.find_by_email(admin_dto.email)
        if not admin_data:
            display_message("Email tidak ditemukan!", "error")
            return False

        _, _, _, password_hash = admin_data
        if not checkpw(
            admin_dto.password.encode("utf-8"), password_hash.encode("utf-8")
        ):
            display_message("Password salah!", "error")
            return False

        return True
