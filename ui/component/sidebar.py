import tkinter as tk
from constant.ui_constant import UIConstants as const


class Sidebar:
    def __init__(self, master, menu_commands):
        self.master = master
        self.menu_commands = menu_commands
        self.sidebar = None

    def create(self):
        self.sidebar = tk.Frame(
            self.master,
            bg=const.COLOR_SIDEBAR_BG,
            width=const.SIDEBAR_WIDTH,
            height=const.WINDOW_HEIGHT,
        )
        self.sidebar.pack(side="left", fill="y")

        for name, command in self.menu_commands.items():
            btn = tk.Button(
                self.sidebar,
                text=name,
                bg=const.COLOR_SIDEBAR_BUTTON_BG,
                fg=const.COLOR_BUTTON_TEXT,
                font=(const.FONT_MAIN, const.FONT_SIZE_BUTTON),
                bd=0,
                relief=const.BUTTON_RELIEF,
                height=const.BUTTON_HEIGHT,
                width=const.BUTTON_WIDTH,
                command=command,
            )
            btn.pack(fill="x")
