import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.publisher_service import PublisherService
from dto.publisher_dto import PublisherDTO


class PublisherFrame(Base):

    def __init__(self, master: Frame, publisher_service: PublisherService):
        columns = ["ID", "Nama", "Dibuat Pada"]
        super().__init__(master, "Manajemen Penerbit", columns)
        self.publisher_service = publisher_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.update_button = None
        self.delete_button = None

    def render(self):
        # Hapus widget sebelumnya
        for widget in self.master.winfo_children():
            widget.destroy()

        # Buat layout dasar
        self.create_layout()

        # Form Tambah/Update Penerbit
        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=const.PADDING_MEDIUM, anchor="w")

        name_label = tk.Label(
            form_frame,
            text="Nama Penerbit:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        name_label.grid(
            row=0,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.name_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.name_entry.grid(
            row=0,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=1, columnspan=2, pady=const.PADDING_MEDIUM)

        self.add_button = tk.Button(
            button_frame,
            text="Tambah",
            bg=const.COLOR_ADD_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.add_publisher,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.update_button = tk.Button(
            button_frame,
            text="Perbarui",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.update_publisher,
        )
        self.update_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_publisher,
        )
        self.delete_button.pack_forget()

        # Buat tabel
        publishers = self.publisher_service.get_all_publishers()
        self.create_treeview(publishers)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, item_data[1])

                # Tampilkan tombol Edit dan Delete, sembunyikan Tambah
                self.add_button.pack_forget()
                self.update_button.pack(side="left", padx=const.PADDING_SMALL)
                self.delete_button.pack(side="left", padx=const.PADDING_SMALL)
            else:
                self.reset_buttons()

    def reset_buttons(self):
        self.selected_item = None
        self.name_entry.delete(0, tk.END)

        # Sembunyikan Edit dan Delete, tampilkan Tambah
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

    def add_publisher(self):
        name = self.name_entry.get().strip()
        publisher_dto = PublisherDTO(name=name)
        self.publisher_service.add_publisher(publisher_dto)

        self.reset_buttons()
        self.render()

    def update_publisher(self):
        name = self.name_entry.get().strip()
        publisher_dto = PublisherDTO(id=self.selected_item, name=name)
        self.publisher_service.update_publisher(publisher_dto)

        self.reset_buttons()
        self.render()

    def delete_publisher(self):
        publisher_dto = PublisherDTO(id=self.selected_item)
        self.publisher_service.delete_publisher(publisher_dto)

        self.reset_buttons()
        self.render()
