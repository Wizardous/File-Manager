from tkinter import *
import tkinter as tk
import Framework.ui._handlers as handle

from Framework.ui.login import Login_form

def main():
    handle.root = tk.Tk()
    handle.login_frame = Login_form(handle.root)
    handle.root.mainloop()
    pass

if __name__ == "__main__":
    main()