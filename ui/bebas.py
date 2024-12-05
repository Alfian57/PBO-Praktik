import tkinter as tk
from tkinter import ttk


class LibraryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1100x600")
        self.root.resizable(False, False)

        # Main layout frames
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self.root, bg="#ecf0f1", width=700, height=600)
        self.main_frame.pack(side="right", fill="both", expand=True)

        # Sidebar buttons
        self.menu_buttons = {
            "Books": self.show_books,
            "Students": self.show_students,
            "Categories": self.show_categories,
            "Classes": self.show_classes,
            "Publishers": self.show_publishers,
            "Borrowing": self.show_borrowing,
        }

        for index, (name, command) in enumerate(self.menu_buttons.items()):
            btn = tk.Button(
                self.sidebar,
                text=name,
                bg="#34495e",
                fg="white",
                font=("Arial", 12),
                bd=0,
                relief="flat",
                height=2,
                width=15,
                command=command,
            )
            btn.pack(fill="x")

        # Title label in main frame
        self.title_label = tk.Label(
            self.main_frame, text="", font=("Arial", 20), bg="#ecf0f1"
        )
        self.title_label.pack(pady=20)

        # Form frame
        self.form_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        self.form_frame.pack(fill="both", expand=True)

        # Data storage (temporary for now)
        self.data = {
            "Books": [],
            "Students": [],
            "Categories": [],
            "Classes": [],
            "Publishers": [],
            "Borrowing": [],
        }

    def clear_frame(self):
        """Clear the form frame for new content."""
        for widget in self.form_frame.winfo_children():
            widget.destroy()

    def show_books(self):
        self.show_section(
            "Books", ["ID Book", "Book Title", "Author", "Publisher", "Year"]
        )

    def show_students(self):
        self.show_section("Students", ["Student ID", "Student Name", "Class"])

    def show_categories(self):
        self.show_section("Categories", ["Category Name"])

    def show_classes(self):
        self.show_section("Classes", ["Class Name", "Description"])

    def show_publishers(self):
        self.show_section("Publishers", ["Publisher Name", "Contact"])

    def show_borrowing(self):
        self.show_section(
            "Borrowing", ["Book ID", "Student ID", "Borrow Date", "Return Date"]
        )

    def show_section(self, section_name, columns):
        self.clear_frame()
        self.title_label.config(text=f"Manage {section_name}")

        # Add Button
        add_button = tk.Button(
            self.form_frame,
            text=f"Add {section_name[:-1]}",
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            command=lambda: self.open_add_form(section_name, columns),
        )
        add_button.pack(pady=10, anchor="w")

        # Treeview (table) setup
        columns_with_actions = columns + ["Actions"]
        tree = ttk.Treeview(
            self.form_frame, columns=columns_with_actions, show="headings"
        )
        tree.pack(fill="both", expand=True)

        # Setup columns
        for col in columns_with_actions:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Insert rows of data
        for item in self.data[section_name]:
            row = [item.get(key, "") for key in columns]
            tree.insert("", "end", values=row)

    def open_add_form(self, section_name, fields):
        """Open a form for adding a new item."""
        self.clear_frame()
        self.title_label.config(text=f"Add New {section_name[:-1]}")
        self.create_form(fields)

    def create_form(self, fields):
        """Generate a simple form with the provided field names."""
        self.entries = {}
        for i, field in enumerate(fields):
            label = tk.Label(
                self.form_frame, text=field, font=("Arial", 12), bg="#ecf0f1"
            )
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(self.form_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries[field] = entry

        submit_btn = tk.Button(
            self.form_frame,
            text="Submit",
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            width=10,
            command=self.submit_data,
        )
        submit_btn.grid(row=len(fields), column=1, pady=20)

    def submit_data(self):
        """Handle form submission and add data to the respective list."""
        data = {field: entry.get() for field, entry in self.entries.items()}
        category = self.title_label.cget("text").split()[
            1
        ]  # Get the category name (e.g., 'Books')
        self.data[category].append(data)
        self.show_data(category)

    def show_data(self, category):
        """Display the data in a Treeview for the given category."""
        self.clear_frame()
        columns = list(self.entries.keys())
        columns.append("Actions")

        # Treeview (table) setup
        tree = ttk.Treeview(self.form_frame, columns=columns, show="headings")
        tree.pack(fill="both", expand=True)

        # Setup columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Insert rows of data
        for item in self.data[category]:
            row = list(item.values()) + [self.create_actions_button(tree, item)]
            tree.insert("", "end", values=row)

    def create_actions_button(self, tree, item):
        """Create buttons for editing and deleting."""

        def edit():
            self.edit_data(item)

        def delete():
            category = self.title_label.cget("text").split()[1]
            self.data[category].remove(item)
            self.show_data(category)

        edit_button = tk.Button(self.form_frame, text="Edit", command=edit)
        delete_button = tk.Button(self.form_frame, text="Delete", command=delete)
        edit_button.grid(row=0, column=0)
        delete_button.grid(row=0, column=1)

        return [edit_button, delete_button]

    def edit_data(self, item):
        """Load selected data into form for editing."""
        for field, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, item[field])
        # After editing, save changes back to data (not implemented yet in this function)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementApp(root)
    root.mainloop()
