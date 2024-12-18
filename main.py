import tkinter as tk
from dotenv import load_dotenv
from app.db import DB
from ui.login import Login

# TOLONG BACA README.md UNTUK SETUP PROJECTNYA


def init():
    load_dotenv()


def main():
    root = tk.Tk()
    Login(root)
    root.mainloop()


def cleanup():
    db = DB.get_instance()
    db.close()


if __name__ == "__main__":
    init()
    main()
    cleanup()
