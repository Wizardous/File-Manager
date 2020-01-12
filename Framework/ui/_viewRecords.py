from tkinter import *
from threading import Thread

class ViewRecords(Frame):
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
        self.__populate_list()

    def __populate_list(self):
        for i in range(100):
            record = ' Wizardous' + str(i)
            self.rec_list.insert(END, record)
        pass

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
            text = "Overview",
            anchor = 'w',
            font = ("Montserrat", 40),
            width = 8,
            bg = self.col_page_bg,
            fg = self.col_fg,
        )
        self.title_lbl.place(relx=0.6, rely=0.4, anchor='e')


        # ------------- List Frame --------------------------------
        self.list_Frame = Frame(
            self._master,
            height = self._master['height']*0.6,
            width = self._master['width']*0.9,
            bg = 'grey'
        )
        self.list_Frame.place(relx=0.5, rely=0.2, anchor='n')
        self.frame_list.append(self.list_Frame)

        self.rec_list = Listbox(
            self.list_Frame,
            height = 8,
            width = 37,
            font=("Montserrat", 15),
            bd = 0,
            bg = self.col_list_bg,
            fg = self.col_list_fg,
            selectbackground = self.col_selected_bg,
            selectforeground = self.col_selected_fg,
            highlightbackground = self.col_page_bg,
            highlightcolor = self.col_page_bg
        )
        self.rec_list.pack(side=LEFT, fill=BOTH)


        scrollBar = Scrollbar(
            self.list_Frame,
        )
        scrollBar.pack(side=RIGHT, fill='y')

        scrollBar.config(command=self.rec_list.yview)
        self.rec_list.config(yscrollcommand=scrollBar.set)

        # ------------- Search Frame --------------------------------
        self.search_Frame = Frame(
            self._master,
            height = 35,
            width = self._master['width'] * 0.9,
            bg = self.col_page_bg
            # bg = 'cyan',
        )
        self.search_Frame.place(relx=0.5, rely=0.7, anchor='n')
        self.frame_list.append(self.search_Frame)

        search_Label = Label(
            self.search_Frame,
            text = "Search Keyword: ",
            font = "Montserrat 11",
            bg = self.col_page_bg,
            fg = self.col_fg
        )
        search_Label.place(relx=0.29, rely=0.45, anchor='w')

        self.search_String = StringVar()
        search_Entry = Entry(
            self.search_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=18,
            font="Montserrat 13",
            justify='right',
            textvariable=self.search_Frame
        )
        search_Entry.place(relx=0.58, rely=0.12, anchor='nw')


        # ------------- View Frame --------------------------------
        self.viewBtn_Frame = Frame(
            self._master,
            height = 50,
            width = self._master['width'] * 0.9,
            bg = self.col_page_bg
        )
        self.viewBtn_Frame.place(relx=0.5, rely=0.82, anchor='n')
        self.frame_list.append(self.viewBtn_Frame)

        self.count_lbl = Label(
            self.viewBtn_Frame,
            text = f"Total Records : {self.records_count}",
            anchor='w',
            font=("Montserrat", 11),
            width=20,
            bg=self.col_page_bg,
            fg=self.col_fg
        )
        self.count_lbl.place(relx=0.21, rely=0.15, anchor='n')

        view_Btn = Button(
            self.viewBtn_Frame,
            text = "View Selected",
            # height = ,
            width = 12,
            bd = 0,
            font=("Montserrat", 14),
            bg = self.col_btn_default,
            fg = self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            # command = showEntry,
        )
        view_Btn.place(relx=0.85, rely=0.15, anchor='n')

    def close(self):
        for frame in self.frame_list:
            frame.destroy()