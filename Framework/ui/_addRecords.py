from tkinter import *
from threading import Thread

class AddRecords(Frame):
    def __init__(self, parent_frame):
        self._master = parent_frame
        super().__init__(self._master)
        self.label = Label(self._master, text = "Add Records...")
        self.label.place(relx=0.5, rely=0.5, anchor='n')

    def close(self):
        widget_list = [self.label]
        for widget in widget_list:
            widget.destroy()

    def __del__(self):
        print("Add Frame Ended")