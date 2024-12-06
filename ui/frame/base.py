import tkinter as tk
from tkinter import ttk
from constant.ui_constant import UIConstants as const


class Base:
    def __init__(self, master, title, columns):
        self.master = master
        self.title = title
        self.columns = columns

        self.frame = tk.Frame(master, bg=const.COLOR_MAIN_BG)
        self.title_label = None
        self.tree = None

    def create_layout(self):
        self.title_label = tk.Label(
            self.master,
            text=self.title,
            font=(const.FONT_MAIN, const.FONT_SIZE_TITLE),
            bg=const.COLOR_MAIN_BG,
        )
        self.title_label.pack(pady=const.PADDING_LARGE)

    def create_treeview(self, data):
        columns_with_actions = self.columns
        self.tree = ttk.Treeview(
            self.master, columns=columns_with_actions, show="headings"
        )
        self.tree.pack(fill="both", expand=True)

        for col in columns_with_actions:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for item in data:
            if isinstance(item, dict):
                self.tree.insert("", "end", values=list(row.values()))
                row = item
            elif isinstance(item, tuple):
                row = item
                self.tree.insert("", "end", values=row)
            else:
                row = item.__dict__
                self.tree.insert("", "end", values=list(row.values()))
