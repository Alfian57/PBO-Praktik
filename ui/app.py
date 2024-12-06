import tkinter as tk
from tkinter import Tk
from ui.component.sidebar import Sidebar
from ui.frame.book_frame import BookFrame
from constant.ui_constant import UIConstants as const
from service.book_service import BookService
from service.student_service import StudentService
from service.category_service import CategoryService
from service.class_service import ClassService
from service.publisher_service import PublisherService
from service.book_loan_service import BookLoanService
from ui.frame.student_frame import StudentFrame
from ui.frame.category_frame import CategoryFrame
from ui.frame.class_frame import ClassFrame
from ui.frame.publisher_frame import PublisherFrame
from ui.frame.book_loan_frame import BookLoanFrame


class App:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Sistem Peminjaman Buku")
        self.root.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        # Setup main layout
        self.main_frame = tk.Frame(
            self.root,
            bg=const.COLOR_MAIN_BG,
            width=const.WINDOW_WIDTH - const.SIDEBAR_WIDTH,
            height=const.WINDOW_HEIGHT,
        )
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.setup_services()
        self.setup_sidebar()

    def setup_services(self):
        self.book_service = BookService()
        self.student_service = StudentService()
        self.category_service = CategoryService()
        self.class_service = ClassService()
        self.publisher_service = PublisherService()
        self.book_loan_service = BookLoanService()

    def setup_sidebar(self):
        menu_commands = {
            "Buku": self.show_books,
            "Siswa": self.show_students,
            "Kategori": self.show_categories,
            "Kelas": self.show_classes,
            "Penerbit": self.show_publishers,
            "Peminjaman": self.show_borrowing,
        }

        sidebar = Sidebar(self.root, menu_commands)
        sidebar.create()

    def show_books(self):
        book_frame = BookFrame(self.main_frame, self.book_service)
        book_frame.render()

    def show_students(self):
        student_frame = StudentFrame(self.main_frame, self.student_service)
        student_frame.render()

    def show_categories(self):
        category_frame = CategoryFrame(self.main_frame, self.category_service)
        category_frame.render()

    def show_classes(self):
        class_frame = ClassFrame(self.main_frame, self.class_service)
        class_frame.render()

    def show_publishers(self):
        publisher_frame = PublisherFrame(self.main_frame, self.publisher_service)
        publisher_frame.render()

    def show_borrowing(self):
        book_loan_frame = BookLoanFrame(self.main_frame, self.book_loan_service)
        book_loan_frame.render()
