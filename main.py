from tkinter import *
import tkinter as tk
from threading import Thread

from api.login import Login
from ui.login import Login_form


def main():
    login_obj = Login()
    root = tk.Tk()
    login_frame = Login_form(root, login_obj)
    root.mainloop()
    pass

if __name__ == "__main__":
    main()