from tkinter import *
from threading import Thread

class AddRecords(Frame):
    def __init__(self, parent_frame):
        self._master = parent_frame
        super().__init__(self._master)

        self.col_bg = '#2b2b3d'
        self.col_fg = '#05ff7e'
        self.entry_bg = '#1e1e2b'
        self.col_btn_clicked = "#323247"
        self.col_btn_default = "#36364d"

        self.col_page_bg = "#3f3f5a"
        self.col_list_bg = "#34344b"
        self.col_list_fg = "#00cc63"
        self.col_selected_bg = "#2a2a3c"
        self.col_selected_fg = "#99ff99"

        self.frame_list = []
        self.initFrame()

    def initFrame(self):

        # ------------- Title Frame --------------------------------
        self.title_Frame = Frame(
            self._master,
            height=self._master['height'] * 0.14,
            width=self._master['width'] * 0.9,
            bg=self.col_page_bg,
        )
        self.title_Frame.place(relx=0.5, rely=0.18, anchor="s")
        self.frame_list.append((self.title_Frame))

        self.title_lbl = Label(
            self.title_Frame,
            text="New Record",
            anchor='w',
            font=("Montserrat", 30),
            width = 15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        self.title_lbl.place(relx=0.83, rely=0.4, anchor='e')

        # ------------- Input Frame --------------------------------
        self.input_Frame = Frame(
            self._master,
            height = self._master['height'] * 0.7,
            width = self._master['width'] * 0.9,
            bg = self.col_page_bg
        )
        self.input_Frame.place(relx=0.5, rely=0.2, anchor="n")
        self.frame_list.append((self.input_Frame))

        userName_Label = Label(
            self.input_Frame,
            text="Username :",
            anchor='w',
            font=("Montserrat", 13),
            width=15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        userName_Label.place(relx=0.42, rely=0.1, anchor='e')

        self.userName_String = StringVar()
        self.userName_Entry = Entry(
            self.input_Frame,
            bg=self.entry_bg,
            fg=self.col_fg,bd=0,
            width=28,
            font="Montserrat 15",
            justify='left',
            textvariable=self.userName_String
        )
        self.userName_Entry.place(relx=0.07, rely=0.15, anchor='nw')

        email_Label = Label(
            self.input_Frame,
            text="Email :",
            anchor='w',
            font=("Montserrat", 13),
            width=15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        email_Label.place(relx=0.42, rely=0.3, anchor='e')

        self.email_String = StringVar()
        self.email_Entry = Entry(
            self.input_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width = 28,
            font="Montserrat 15",
            justify='left',
            textvariable=self.email_String
        )
        self.email_Entry.place(relx=0.07, rely=0.35, anchor='nw')

        password_Label = Label(
            self.input_Frame,
            text="Password :",
            anchor='w',
            font=("Montserrat", 13),
            width=15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        password_Label.place(relx=0.42, rely=0.5, anchor='e')

        self.password_String = StringVar()
        self.password_Entry = Entry(
            self.input_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=13,
            font="Montserrat 15",
            show="\u2022",
            justify='left',
            textvariable=self.password_String
        )
        self.password_Entry.place(relx=0.25, rely=0.55, anchor='n')

        confirm_Label = Label(
            self.input_Frame,
            text="Confirm :",
            anchor='w',
            font=("Montserrat", 13),
            width=15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        confirm_Label.place(relx=0.82, rely=0.5, anchor='e')

        self.confirm_String = StringVar()
        self.confirm_Entry = Entry(
            self.input_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=13,
            font="Montserrat 15",
            show="\u2022",
            justify='left',
            textvariable=self.confirm_String
        )
        self.confirm_Entry.place(relx=0.65, rely=0.55, anchor='n')

        add_Btn = Button(
            self.input_Frame,
            text="Add",
            # height = ,
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            # command = self.add_Event,
        )
        add_Btn.place(relx=0.23, rely=0.8, anchor='n')
        
    def close(self):
        for frame in self.frame_list:
            frame.destroy()