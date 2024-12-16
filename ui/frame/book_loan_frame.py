import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.book_loan_service import BookLoanService
from dto.book_loan_dto import BookLoanDTO
from tkcalendar import DateEntry


class BookLoanFrame(Base):

    def __init__(self, master: Frame, book_loan_service: BookLoanService):
        columns = [
            "ID",
            "Judul Buku",
            "Nama Siswa",
            "Tanggal Peminjaman",
            "Tanggal Pengembalian",
        ]
        super().__init__(master, "Manajemen Peminjaman", columns)
        self.book_loan_service = book_loan_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.update_button = None
        self.delete_button = None

        # Placeholder untuk form
        self.books = self.book_loan_service.get_all_books()
        self.students = self.book_loan_service.get_all_students()

        # Mapping dictionaries
        self.books_map = {item.title: item.id for item in self.books}
        self.students_map = {item.name: item.id for item in self.students}

    def render(self):
        # Hapus widget sebelumnya
        for widget in self.master.winfo_children():
            widget.destroy()

        # Buat layout dasar
        self.create_layout()

        # Form Tambah/Update Kategori
        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=const.PADDING_MEDIUM, anchor="w")

        book_label = tk.Label(
            form_frame,
            text="Buku:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        book_label.grid(
            row=0,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        book_options = list(self.books_map.keys())
        self.book_var = tk.StringVar(value=book_options[0] if book_options else "")
        self.book_dropdown = tk.OptionMenu(form_frame, self.book_var, *book_options)
        self.book_dropdown.grid(
            row=0,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        student_label = tk.Label(
            form_frame,
            text="Siswa:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        student_label.grid(
            row=1,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # For class dropdown
        student_options = list(self.students_map.keys())
        self.student_var = tk.StringVar(
            value=student_options[0] if student_options else ""
        )
        self.student_dropdown = tk.OptionMenu(
            form_frame, self.student_var, *student_options
        )
        self.student_dropdown.grid(
            row=1,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        borrowing_date_label = tk.Label(
            form_frame,
            text="Tanggal Peminjaman:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        borrowing_date_label.grid(
            row=2,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.borrowing_date_entry = DateEntry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.borrowing_date_entry.grid(
            row=2,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        return_date_label = tk.Label(
            form_frame,
            text="Tanggal Pengembalian:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        return_date_label.grid(
            row=3,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.return_date_entry = DateEntry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.return_date_entry.grid(
            row=3,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=4, columnspan=2, pady=const.PADDING_MEDIUM)

        self.add_button = tk.Button(
            button_frame,
            text="Tambah",
            bg=const.COLOR_ADD_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.add_book_loan,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.update_button = tk.Button(
            button_frame,
            text="Perbarui",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.update_book_loan,
        )
        self.update_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_book_loan,
        )
        self.delete_button.pack_forget()

        # Buat tabel
        loans = self.book_loan_service.get_all_book_loan_with_student_and_book()
        self.create_treeview(loans)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.book_var.set(item_data[1])
                self.student_var.set(item_data[2])
                self.borrowing_date_entry.delete(0, tk.END)
                self.borrowing_date_entry.insert(0, item_data[3])
                self.return_date_entry.delete(0, tk.END)
                self.return_date_entry.insert(0, item_data[4])

                # Tampilkan tombol Edit dan Delete, sembunyikan Tambah
                self.add_button.pack_forget()
                self.update_button.pack(side="left", padx=const.PADDING_SMALL)
                self.delete_button.pack(side="left", padx=const.PADDING_SMALL)
            else:
                self.reset_buttons()

    def reset_buttons(self):
        self.selected_item = None
        self.book_var.set("")
        self.student_var.set("")
        self.borrowing_date_entry.delete(0, tk.END)
        self.return_date_entry.delete(0, tk.END)

        # Sembunyikan Edit dan Delete, tampilkan Tambah
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

    def add_book_loan(self):
        book = self.books_map.get(self.book_var.get().strip())
        student = self.students_map.get(self.student_var.get().strip())
        borrowing_date = self.borrowing_date_entry.get().strip()
        return_date = self.return_date_entry.get().strip()

        book_loan_dto = BookLoanDTO(
            book_id=book,
            student_id=student,
            borrowing_date=borrowing_date,
            return_date=return_date,
        )
        self.book_loan_service.add_book_loan(book_loan_dto)

        self.reset_buttons()
        self.render()

    def update_book_loan(self):
        book = self.books_map.get(self.book_var.get().strip())
        student = self.students_map.get(self.student_var.get().strip())
        borrowing_date = self.borrowing_date_entry.get().strip()
        return_date = self.return_date_entry.get().strip()

        book_loan_dto = BookLoanDTO(
            id=self.selected_item,
            book_id=book,
            student_id=student,
            borrowing_date=borrowing_date,
            return_date=return_date,
        )
        self.book_loan_service.update_book_loan(book_loan_dto)

        self.reset_buttons()
        self.render()

    def delete_book_loan(self):
        book_loan_dto = BookLoanDTO(id=self.selected_item)
        self.book_loan_service.delete_book_loan(book_loan_dto)

        self.reset_buttons()
        self.render()
