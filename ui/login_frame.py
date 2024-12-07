import tkinter as tk
from service.admin_service import AdminService
from dto.admin_dto import AdminDTO


class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry("300x250")
        self.admin_service = AdminService()
        self.show_login_window()

    def show_login_window(self):
        self.clear_window()
        tk.Label(self.root, text="Login Admin", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Email", font=("Arial", 12)).pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 12))
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Password", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login).pack(
            pady=10
        )

    def show_main_window(self):
        self.clear_window()
        tk.Label(self.root, text="Selamat Datang!", font=("Arial", 16)).pack(pady=20)
        tk.Button(
            self.root, text="Logout", font=("Arial", 12), command=self.logout
        ).pack(pady=10)

    def logout(self):
        from helper.show_message import display_message

        confirm = display_message("Apakah Anda yakin ingin logout?", "question")
        if confirm:
            display_message("Anda telah logout.", "info")
            self.show_login_window()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not email or not password:
            from helper.show_message import display_message

            display_message("Email dan Password wajib diisi!", "error")
            return

        admin_dto = AdminDTO(email, password)
        if self.admin_service.validate_login(admin_dto):
            from helper.show_message import display_message

            display_message("Login berhasil!", "info")
            self.show_main_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
