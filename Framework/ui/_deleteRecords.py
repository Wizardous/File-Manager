from tkinter import *


class DeleteRecords(Frame):
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
            text="Recycle",
            anchor='w',
            font=("Montserrat", 30),
            width=15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        self.title_lbl.place(relx=0.83, rely=0.4, anchor='e')

        # ------------- Input Frame --------------------------------
        self.input_Frame = Frame(
            self._master,
            height=self._master['height'] * 0.7,
            width=self._master['width'] * 0.9,
            bg=self.col_page_bg
        )
        self.input_Frame.place(relx=0.5, rely=0.22, anchor="n")
        self.frame_list.append((self.input_Frame))

        question_Label = Label(
            self.input_Frame,
            text="Deleting the record using :",
            anchor='w',
            font=("Montserrat", 13),
            width=25,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        question_Label.place(relx=0.03, rely=0.0, anchor='nw')

        self.radio_Var = StringVar()

        self.username_Radio = Radiobutton(
            self.input_Frame,
            text = 'Username',
            font=("Montserrat", 12),
            variable = self.radio_Var,
            value = "Username",
            bg = self.col_page_bg,
            fg = self.col_fg,
            selectcolor = self.col_bg,
            activebackground = self.col_page_bg,
            activeforeground = self.col_selected_fg,
            command=self.changeLabel
        )
        self.username_Radio.place(relx=0.1, rely=0.1, anchor='nw')
        self.username_Radio.select()

        self.email_Radio = Radiobutton(
            self.input_Frame,
            text='Email',
            font=("Montserrat", 12),
            variable=self.radio_Var,
            value="Email",
            bg=self.col_page_bg,
            fg=self.col_fg,
            selectcolor=self.col_bg,
            activebackground=self.col_page_bg,
            activeforeground=self.col_selected_fg,
            command = self.changeLabel
        )
        self.email_Radio.place(relx=0.4, rely=0.1, anchor='nw')

        self.fieldVar = StringVar()
        fieldName_Label = Label(
            self.input_Frame,
            text="Enter the Username : ",
            textvariable = self.fieldVar,
            anchor='w',
            font=("Montserrat", 13),
            width=30,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        fieldName_Label.place(relx=0.03, rely=0.33, anchor='w')
        self.changeLabel()

        self.field_String = StringVar()
        self.field_Entry = Entry(
            self.input_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=28,
            font="Montserrat 15",
            justify='left',
            textvariable=self.field_String
        )
        self.field_Entry.place(relx=0.039, rely=0.43, anchor='w')

        delete_Btn = Button(
            self.input_Frame,
            text="Delete",
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            # command = self.delete_Event,
        )
        delete_Btn.place(relx=0.05, rely=0.65, anchor='w')

    def changeLabel(self):
        self.fieldVar.set(f"Enter the {self.radio_Var.get()} :")

    def close(self):
        for frame in self.frame_list:
            frame.destroy()

