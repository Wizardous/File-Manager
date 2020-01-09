from tkinter import *
from threading import Thread

class ViewRecords(Frame):
    def __init__(self, parent_frame):
        self._master = parent_frame
        super().__init__(self._master)
        self.label = Label(self._master, text = "Records...")
        self.label.place(relx=0.5, rely=0.3, anchor='n')
        
        

    def close(self):
        widget_list = [self.label]
        for widget in widget_list:
            widget.destroy()