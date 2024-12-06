import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.book_service import BookService
from dto.book_dto import BookDTO


class BookFrame(Base):

    def __init__(self, master: Frame, book_service: BookService):
        columns = [
            "ID",
            "Judul",
            "ISBN",
            "Kategori",
            "Penerbit",
            "Tahun Terbit",
            "Dibuat Pada",
        ]
        super().__init__(master, "Manajemen Buku", columns)
        self.book_service = book_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.update_button = None
        self.delete_button = None

        # Placeholder untuk form
        self.categories = self.book_service.get_all_categories()
        self.publishers = self.book_service.get_all_publishers()

        # Mapping dictionaries
        self.category_map = {category.name: category.id for category in self.categories}
        self.publisher_map = {
            publisher.name: publisher.id for publisher in self.publishers
        }

    def render(self):
        # Hapus widget sebelumnya
        for widget in self.master.winfo_children():
            widget.destroy()

        # Buat layout dasar
        self.create_layout()

        # Form Tambah/Update Penerbit
        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=const.PADDING_MEDIUM, anchor="w")

        title_label = tk.Label(
            form_frame,
            text="Judul:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        title_label.grid(
            row=0,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.title_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.title_entry.grid(
            row=0,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        isbn_label = tk.Label(
            form_frame,
            text="ISBN:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        isbn_label.grid(
            row=1,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.isbn_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.isbn_entry.grid(
            row=1,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        category_label = tk.Label(
            form_frame,
            text="Kategori:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        category_label.grid(
            row=2,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # For category dropdown
        category_options = list(self.category_map.keys())
        self.category_var = tk.StringVar(
            value=category_options[0] if category_options else ""
        )
        self.category_dropdown = tk.OptionMenu(
            form_frame, self.category_var, *category_options
        )
        self.category_dropdown.grid(
            row=2,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        publisher_label = tk.Label(
            form_frame,
            text="Penerbit:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        publisher_label.grid(
            row=3,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # For publisher dropdown
        publisher_options = list(self.publisher_map.keys())
        self.publisher_var = tk.StringVar(
            value=publisher_options[0] if publisher_options else ""
        )
        self.publisher_dropdown = tk.OptionMenu(
            form_frame, self.publisher_var, *publisher_options
        )
        self.publisher_dropdown.grid(
            row=3,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        year_label = tk.Label(
            form_frame,
            text="Tahun Terbit:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        year_label.grid(
            row=4,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.year_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.year_entry.grid(
            row=4,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=5, columnspan=2, pady=const.PADDING_MEDIUM)

        self.add_button = tk.Button(
            button_frame,
            text="Tambah",
            bg=const.COLOR_ADD_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.add_book,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.update_button = tk.Button(
            button_frame,
            text="Perbarui",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.update_book,
        )
        self.update_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_book,
        )
        self.delete_button.pack_forget()

        # Buat tabel
        books = self.book_service.get_all_books()
        self.create_treeview(books)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, item_data[1])
                self.isbn_entry.delete(0, tk.END)
                self.isbn_entry.insert(0, item_data[2])
                self.category_var.set(item_data[3])
                self.publisher_var.set(item_data[4])
                self.year_entry.delete(0, tk.END)
                self.year_entry.insert(0, item_data[5])

                # Tampilkan tombol Edit dan Delete, sembunyikan Tambah
                self.add_button.pack_forget()
                self.update_button.pack(side="left", padx=const.PADDING_SMALL)
                self.delete_button.pack(side="left", padx=const.PADDING_SMALL)
            else:
                self.reset_buttons()

    def reset_buttons(self):
        self.selected_item = None
        self.title_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.category_var.set("")
        self.publisher_var.set("")
        self.year_entry.delete(0, tk.END)

        # Sembunyikan Edit dan Delete, tampilkan Tambah
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

    def add_book(self):
        title = self.title_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        category = self.category_map.get(self.category_var.get().strip())
        publisher = self.publisher_map.get(self.publisher_var.get().strip())
        year = self.year_entry.get().strip()
        bookDto = BookDTO(
            title=title,
            isbn=isbn,
            category_id=category,
            publisher_id=publisher,
            publish_year=year,
        )
        self.book_service.add_book(bookDto)

        self.reset_buttons()
        self.render()

    def update_book(self):
        title = self.title_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        category = self.category_map.get(self.category_var.get().strip())
        publisher = self.publisher_map.get(self.publisher_var.get().strip())
        year = self.year_entry.get().strip()
        bookDto = BookDTO(
            id=self.selected_item,
            title=title,
            isbn=isbn,
            category_id=category,
            publisher_id=publisher,
            publish_year=year,
        )
        self.book_service.update_book(bookDto)

        self.reset_buttons()
        self.render()

    def delete_book(self):
        bookDto = BookDTO(id=self.selected_item)
        self.book_service.delete_book(bookDto)

        self.reset_buttons()
        self.render()
