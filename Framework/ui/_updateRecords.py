from tkinter import *
from threading import Thread

class UpdateRecords(Frame):
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
        self.records_count = 100
        self.initFrame()

    def initFrame(self):

        # ------------- Title Frame --------------------------------
        self.title_Frame = Frame(
            self._master,
            height = self._master['height']*0.14,
            width = self._master['width']*0.9,
            bg = self.col_page_bg,
        )
        self.title_Frame.place(relx=0.5, rely=0.18, anchor="s")
        self.frame_list.append((self.title_Frame))

        self.title_lbl = Label(
            self.title_Frame,
            text = "Editorial",
            anchor = 'w',
            font = ("Montserrat", 40),
            width = 8,
            bg = self.col_page_bg,
            fg = self.col_fg,
        )
        self.title_lbl.place(relx=0.6, rely=0.4, anchor='e')

        # ------------- Search Frame --------------------------------
        self.search_Frame = Frame(
            self._master,
            height = 55,
            width = self._master['width'] * 0.9,
            bg = self.col_page_bg
            # bg = 'cyan',
        )
        self.search_Frame.place(relx=0.5, rely=0.2, anchor='n')
        self.frame_list.append(self.search_Frame)

        search_Label = Label(
            self.search_Frame,
            text = "Search Keyword: ",
            font = "Montserrat 11",
            bg = self.col_page_bg,
            fg = self.col_fg
        )
        search_Label.place(relx=0.005, rely=0.2, anchor='w')
        search_Label.focus_force()

        self.search_String = StringVar()
        search_Entry = Entry(
            self.search_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=20,
            font="Montserrat 13",
            justify='left',
            textvariable=self.search_Frame
        )
        search_Entry.place(relx=0.01, rely=0.7, anchor='w')

        # ------------- Edit Frame --------------------------------
        self.edit_Frame = Frame(
            self._master,
            height = 280,
            width = self._master['width'] * 0.9,
            bg = self.col_page_bg
        )
        self.edit_Frame.place(relx=0.5, rely=0.34, anchor='n')
        self.frame_list.append(self.edit_Frame)
        x = 0.0
        self.username_check_Var = BooleanVar()
        self.username_Check = Checkbutton(
            self.edit_Frame,
            text='Username : ',
            font=("Montserrat", 12),
            width = 15,
            variable=self.username_check_Var,
            onvalue=TRUE,
            offvalue=FALSE,
            bg=self.col_page_bg,
            fg=self.col_fg,
            selectcolor=self.col_bg,
            activebackground=self.col_page_bg,
            activeforeground=self.col_selected_fg,
            command=self.changeStatus
        )
        self.username_Check.place(relx=0.2+x, rely=0, anchor='n')

        self.username_String = StringVar()
        self.username_Entry = Entry(
            self.edit_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=27,
            font="Montserrat 15",
            justify='left',
            state = 'disabled',
            textvariable=self.username_String
        )
        self.username_Entry.place(relx=0.435+x, rely=0.12, anchor='n')

        self.email_check_Var = BooleanVar()
        self.email_Check = Checkbutton(
            self.edit_Frame,
            text='Email : ',
            width=15,
            font=("Montserrat", 12),
            variable=self.email_check_Var,
            onvalue=TRUE,
            offvalue=FALSE,
            bg=self.col_page_bg,
            fg=self.col_fg,
            selectcolor=self.col_bg,
            activebackground=self.col_page_bg,
            activeforeground=self.col_selected_fg,
            command=self.changeStatus
        )
        self.email_Check.place(relx=0.16+x, rely=0.27, anchor='n')

        self.email_String = StringVar()
        self.email_Entry = Entry(
            self.edit_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=27,
            font="Montserrat 15",
            justify='left',
            state='readonly',
            textvariable=self.email_String
        )
        self.email_Entry.place(relx=0.435+x, rely=0.39, anchor='n')


        self.password_check_Var = BooleanVar()
        self.password_Check = Checkbutton(
            self.edit_Frame,
            text='Password : ',
            width=15,
            font=("Montserrat", 12),
            variable=self.password_check_Var,
            onvalue=TRUE,
            offvalue=FALSE,
            bg=self.col_page_bg,
            fg=self.col_fg,
            selectcolor=self.col_bg,
            activebackground=self.col_page_bg,
            activeforeground=self.col_selected_fg,
            command=self.changeStatus
        )
        self.password_Check.place(relx=0.193+x, rely=0.52, anchor='n')

        self.confirm_Label = Label(
            self.edit_Frame,
            text="Confirm : ",
            font="Montserrat 11",
            bg=self.col_page_bg,
            fg=self.col_fg
        )
        self.confirm_Label.place(relx=0.53+x, rely=0.535, anchor='n')

        self.password_String = StringVar()
        self.password_Entry = Entry(
            self.edit_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=13,
            font="Montserrat 15",
            justify='left',
            state='readonly',
            textvariable=self.password_String
        )
        self.password_Entry.place(relx=0.425+x, rely=0.64, anchor='ne')

        self.confirm_String = StringVar()
        self.confirm_Entry = Entry(
            self.edit_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=13,
            font="Montserrat 15",
            justify='left',
            state='readonly',
            textvariable=self.confirm_String
        )
        self.confirm_Entry.place(relx=0.8+x, rely=0.64, anchor='ne')

    def changeStatus(self):
        self.username_Entry.config(
            state = "normal" if self.username_check_Var else "disabled"
        )


    def close(self):
        for frame in self.frame_list:
            frame.destroy()