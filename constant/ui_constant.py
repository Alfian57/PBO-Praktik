import tkinter as tk


class UIConstants:
    root = tk.Tk()

    # Warna
    COLOR_SIDEBAR_BG = "#2c3e50"
    COLOR_SIDEBAR_BUTTON_BG = "#34495e"
    COLOR_MAIN_BG = "#ecf0f1"
    COLOR_ADD_BUTTON_BG = "#27ae60"
    COLOR_EDIT_BUTTON_BG = "#2980b9"
    COLOR_DELETE_BUTTON_BG = "#c0392b"
    COLOR_WHITE = "white"
    COLOR_BUTTON_TEXT = "white"

    # Font
    FONT_MAIN = "Arial"
    FONT_SIZE_TITLE = 20
    FONT_SIZE_BUTTON = 12
    FONT_SIZE_NORMAL = 12

    # FONT LOGIN
    FONT_LOGIN = "Helvetica"
    FONT_LOGIN_TITLE = 28
    FONT_LOGIN_IKON = 24
    FONT_LOGIN_NORMAL = 16
    FONT_LOGIN_SMALL = 14
    FONT_LOGIN_XS = 8

    # Dimensi
    WINDOW_WIDTH = root.winfo_screenwidth()
    WINDOW_HEIGHT = root.winfo_screenheight()
    SIDEBAR_WIDTH = 200

    # Padding & Spacing
    PADDING_SMALL = 5
    PADDING_MEDIUM = 10
    PADDING_LARGE = 20

    # Button Styles
    BUTTON_RELIEF = "flat"
    BUTTON_HEIGHT = 2
    BUTTON_WIDTH = 15

    root.destroy()
