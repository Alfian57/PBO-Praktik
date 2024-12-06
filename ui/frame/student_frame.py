import tkinter as tk
from tkinter import Frame
from ui.frame.base import Base
from constant.ui_constant import UIConstants as const
from service.student_service import StudentService
from dto.student_dto import StudentDTO


class StudentFrame(Base):

    def __init__(self, master: Frame, student_service: StudentService):
        columns = ["ID", "NIS", "Nama", "No Telepon", "Alamat", "Kelas"]
        super().__init__(master, "Manajemen Siswa", columns)
        self.student_service = student_service
        self.selected_item = None

        # Placeholder untuk tombol
        self.add_button = None
        self.update_button = None
        self.delete_button = None

        # Placeholder untuk form
        self.classses = self.student_service.get_all_classes()

        # Mapping dictionaries
        self.classses_map = {item.name: item.id for item in self.classses}

    def render(self):
        # Hapus widget sebelumnya
        for widget in self.master.winfo_children():
            widget.destroy()

        # Buat layout dasar
        self.create_layout()

        # Form Tambah/Update Siswa
        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=const.PADDING_MEDIUM, anchor="w")

        name_label = tk.Label(
            form_frame,
            text="Nama Siswa:",
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

        nis_label = tk.Label(
            form_frame,
            text="NIS:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        nis_label.grid(
            row=1,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.nis_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.nis_entry.grid(
            row=1,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        phone_label = tk.Label(
            form_frame,
            text="No Telepon:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        phone_label.grid(
            row=2,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.phone_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.phone_entry.grid(
            row=2,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        address_label = tk.Label(
            form_frame,
            text="Alamat:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        address_label.grid(
            row=3,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        self.address_entry = tk.Entry(
            form_frame,
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        self.address_entry.grid(
            row=3,
            column=1,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        class_label = tk.Label(
            form_frame,
            text="Kelas:",
            font=(const.FONT_MAIN, const.FONT_SIZE_NORMAL),
        )
        class_label.grid(
            row=4,
            column=0,
            padx=const.PADDING_SMALL,
            pady=const.PADDING_SMALL,
            sticky="w",
        )

        # For class dropdown
        class_options = list(self.classses_map.keys())
        self.class_var = tk.StringVar(value=class_options[0] if class_options else "")
        self.class_dropdown = tk.OptionMenu(form_frame, self.class_var, *class_options)
        self.class_dropdown.grid(
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
            command=self.add_student,
        )
        self.add_button.pack(side="left", padx=const.PADDING_SMALL)

        self.update_button = tk.Button(
            button_frame,
            text="Perbarui",
            bg=const.COLOR_EDIT_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.update_student,
        )
        self.update_button.pack_forget()

        self.delete_button = tk.Button(
            button_frame,
            text="Hapus",
            bg=const.COLOR_DELETE_BUTTON_BG,
            fg=const.COLOR_BUTTON_TEXT,
            font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
            relief=const.BUTTON_RELIEF,
            command=self.delete_student,
        )
        self.delete_button.pack_forget()

        # Buat tabel
        categories = self.student_service.get_all_students_with_class()
        self.create_treeview(categories)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0], "values")
            if item_data:
                self.selected_item = int(item_data[0])
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, item_data[2])
                self.nis_entry.delete(0, tk.END)
                self.nis_entry.insert(0, item_data[1])
                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, item_data[3])
                self.address_entry.delete(0, tk.END)
                self.address_entry.insert(0, item_data[4])
                self.class_var.set(item_data[5])

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

    def add_student(self):
        name = self.name_entry.get().strip()
        nis = self.nis_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        class_id = self.classses_map[self.class_var.get()]

        studentDto = StudentDTO(
            name=name, nis=nis, phone_number=phone, address=address, class_id=class_id
        )
        self.student_service.add_student(studentDto)

        self.reset_buttons()
        self.render()

    def update_student(self):
        name = self.name_entry.get().strip()
        nis = self.nis_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        class_id = self.classses_map[self.class_var.get()]

        studentDto = StudentDTO(
            id=self.selected_item,
            name=name,
            nis=nis,
            phone_number=phone,
            address=address,
            class_id=class_id,
        )
        self.student_service.update_student(studentDto)

        self.reset_buttons()
        self.render()

    def delete_student(self):
        studentDto = StudentDTO(id=self.selected_item)
        self.student_service.delete_student(studentDto)

        self.reset_buttons()
        self.render()
