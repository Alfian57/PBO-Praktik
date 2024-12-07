import tkinter as tk
from service.login_service import LoginService
from dto.admin_dto import AdminDTO
from constant.ui_constant import UIConstants as const
from ui.app import App


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}")

        self.admin_service = LoginService()

        self.show_login_window()

    def show_login_window(self):
        self.clear_window()
        tk.Label(
            self.root, text="Login Admin", font=(const.FONT_MAIN, const.FONT_SIZE_TITLE)
        ).pack(pady=const.PADDING_LARGE)

        tk.Label(
            self.root, text="Email", font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL)
        ).pack()
        self.email_entry = tk.Entry(
            self.root, font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL)
        )
        self.email_entry.pack(pady=const.PADDING_SMALL)

        tk.Label(
            self.root, text="Password", font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL)
        ).pack()
        self.password_entry = tk.Entry(
            self.root, show="*", font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL)
        )
        self.password_entry.pack(pady=const.PADDING_SMALL)

        tk.Button(
            self.root,
            text="Login",
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            command=self.login,
        ).pack(pady=const.PADDING_MEDIUM)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        admin_dto = AdminDTO(email=email, password=password)

        if self.admin_service.validate_login(admin_dto):
            self.show_dashboard()

    def show_dashboard(self):
        self.clear_window()
        App(self.root)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
