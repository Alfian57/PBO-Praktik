import tkinter as tk
from service.login_service import LoginService
from dto.admin_dto import AdminDTO
from constant.ui_constant import UIConstants as const
from ui.app import App
from tkinter import ttk


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}")
        self.root.configure(bg="white")
        self.container = tk.Frame(root, bg="white")
        self.container.pack(expand=True)
        self.admin_service = LoginService()

        self.show_login_window()

    def show_login_window(self):
        self.clear_window()
        self.container = tk.Frame(self.root, bg="white")
        self.container.pack(expand=True)
        self.email_placeholder = "Enter your email"

        self.password_placeholder = "Enter your password"
        self.icon_canvas = tk.Canvas(
            self.container, width=120, height=120, bg="white", highlightthickness=0
        )
        # Lingkaran luar
        self.icon_canvas.create_oval(10, 10, 110, 110, outline="#000000", width=2)

        # Lingkaran dalam (kepala)
        self.icon_canvas.create_oval(40, 30, 80, 70, outline="#000000", width=2)

        # Bahu (menggunakan dua garis melengkung)
        self.icon_canvas.create_arc(
            30,
            70,
            90,
            130,
            start=0,
            extent=180,
            style="arc",
            outline="#000000",
            width=2,
        )

        self.icon_canvas.pack(pady=20)
        tk.Label(
            self.container,
            text="LOGIN",
            bg="white",
            font=(const.FONT_LOGIN, const.FONT_LOGIN_TITLE, "bold"),
            fg="#333",
        ).pack()

        self.email_frame = tk.Frame(self.container, bg="white")
        self.email_frame.pack(pady=15, fill="x", padx=50)
        tk.Label(
            self.email_frame,
            text="📧",
            font=(const.FONT_LOGIN, const.FONT_LOGIN_IKON),
            bg="white",
        ).pack(side="left", padx=10)
        self.email_entry = tk.Entry(
            self.email_frame,
            font=const.FONT_LOGIN_SMALL,
            relief="flat",
            bg="#f4f4f4",
            highlightthickness=1,
            highlightbackground="#373651",
            highlightcolor="#00c3ff",
            fg="grey",
            width=30,
        )
        self.email_entry.insert(0, self.email_placeholder)
        self.email_entry.bind("<FocusIn>", self.clear_placeholder_email)
        self.email_entry.bind("<FocusOut>", self.add_placeholder_email)
        self.email_entry.pack(side="left", expand=True, fill="x", ipady=8)

        self.password_frame = tk.Frame(self.container, bg="white")
        self.password_frame.pack(pady=15, fill="x", padx=50)
        tk.Label(
            self.password_frame,
            text="🔒",
            font=(const.FONT_LOGIN, const.FONT_LOGIN_IKON),
            bg="white",
        ).pack(side="left", padx=10)
        self.password_entry = tk.Entry(
            self.password_frame,
            font=const.FONT_LOGIN_SMALL,
            relief="flat",
            bg="#f4f4f4",
            highlightthickness=1,
            highlightbackground="#373651",
            highlightcolor="#00c3ff",
            fg="grey",
            width=30,
        )
        self.password_entry.insert(0, self.password_placeholder)
        self.password_entry.bind("<FocusIn>", self.clear_placeholder_password)
        self.password_entry.bind("<FocusOut>", self.add_placeholder_password)
        self.password_entry.pack(side="left", expand=True, fill="x", ipady=8)

        tk.Label(self.container, text="").pack(side="left", padx=8)
        self.login_button = tk.Button(
            self.container,
            text="LOGIN",
            bg="#00c3ff",
            fg="white",
            font=const.FONT_LOGIN_SMALL,
            command=self.login,
            relief="flat",
            activebackground="#009fdb",
            cursor="hand2",
        )
        self.login_button.pack(pady=15, fill="x", padx=50)

    def clear_placeholder_email(self, event):
        if self.email_entry.get() == self.email_placeholder:
            self.email_entry.delete(0, "end")
            self.email_entry.config(fg="black")

    def add_placeholder_email(self, event):
        if not self.email_entry.get():
            self.email_entry.insert(0, self.email_placeholder)
            self.email_entry.config(fg="grey")

    # Placeholder Methods for Password
    def clear_placeholder_password(self, event):
        if self.password_entry.get() == self.password_placeholder:
            self.password_entry.delete(0, "end")
            self.password_entry.config(show="*", fg="black")

    def add_placeholder_password(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, self.password_placeholder)
            self.password_entry.config(show="", fg="grey")

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
