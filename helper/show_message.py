from tkinter import messagebox


def display_message(message, type):
    if type == "info":
        messagebox.showinfo("Informasi", message)
    elif type == "error":
        messagebox.showerror("Error", message)
    elif type == "question":
        return messagebox.askquestion("Konfirmasi", message) == "yes"
