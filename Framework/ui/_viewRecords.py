from tkinter import *
from Framework.api.records import Records

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
        self.records_count = 0
        self.initFrame()
        self.file_api = Records()
        self.__populate_list()

    def __populate_list(self, data=None):
        #Empty List first
        self.rec_list.delete(0, END)

        if data or data==[]:
            self.records = data
            for r in self.records:
                self.rec_list.insert(END, str(r[1][0]))

        elif not data:
            status, self.records = self.file_api.readRecords()
            self.records = tuple(enumerate(self.records))
            self.records_count = len(self.records)
            if status:
                for r in self.records:
                    self.rec_list.insert(END, str(r[1][0]))
            self.count_lbl.config(text=f"Total Records : {self.records_count}")

    def __searchTrace(self, *args):
        search_key = self.search_String.get()
        status, result = self.file_api.searchRecords(key=search_key, mode='username')
        if status:
            self.__populate_list(data = result)
        elif result == 404:
            self.__populate_list(data=[])
        else:
            self.__populate_list()

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
        )
        self.search_Frame.place(relx=0.5, rely=0.7, anchor='n')
        self.frame_list.append(self.search_Frame)

        search_Label = Label(
            self.search_Frame,
            text = "Search Username: ",
            font = "Montserrat 11",
            bg = self.col_page_bg,
            fg = self.col_fg
        )
        search_Label.place(relx=0.29, rely=0.45, anchor='w')

        self.search_String = StringVar()
        self.search_String.trace('w', self.__searchTrace)
        search_Entry = Entry(
            self.search_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=18,
            font="Montserrat 13",
            textvariable=self.search_String
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
            width = 12,
            bd = 0,
            font=("Montserrat", 14),
            bg = self.col_btn_default,
            fg = self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command = self.viewSelected,
        )
        view_Btn.place(relx=0.85, rely=0.15, anchor='n')

    def viewSelected(self):
        try:
            curr_select = self.rec_list.curselection()[0]
            ResultDialog(self.records[curr_select])
        except:
            pass

    def close(self):
        for frame in self.frame_list:
            frame.destroy()


class ResultDialog():
    def __init__(self, data):
        self.dialog = Toplevel()
        self.dialog.grab_set()
        print(data)
        self.col_bg = '#2b2b3d'
        self.col_fg = '#05ff7e'
        self.col_btn_clicked = "#323247"
        self.col_btn_default = "#36364d"

        self.dialog.geometry('500x200+500+500')
        self.dialog.config(bg = self.col_bg)

        self.username = data[1][0]
        self.email = data[1][1]
        self.password = data[1][2]
        print(data, self.username, self.email, self.password, sep="\n")

        self.initUI()

    def initUI(self):
        Label(
            self.dialog,
            text=self.username,
            anchor='w',
            font=("Montserrat", 20, 'bold'),
            bg=self.col_bg,
            fg=self.col_fg
        ).place(relx=0.05, rely=0.05, anchor='nw')

        Label(
            self.dialog,
            text=self.email,
            anchor='w',
            font=("Montserrat", 17),
            bg=self.col_bg,
            fg=self.col_fg
        ).place(relx=0.05, rely=0.25, anchor='nw')

        pass_string = self.password[:40] + "..."
        Label(
            self.dialog,
            text = pass_string,
            anchor="w",
            font=("Montserrat", 11),
            bg = self.col_bg,
            fg = "#00b356"
        ).place(relx=0.05, rely=0.45, anchor='nw')

        Button(
            self.dialog,
            text="OK",
            width=10,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command=self.ok_event,
        ).place(relx=0.9, rely=0.7, anchor='ne')

    def ok_event(self):
        self.dialog.grab_release()
        self.dialog.destroy()


def main():
    root = Tk()
    root.geometry("300x300")
    ResultDialog(data=("Wizardous", "abhijitgadge5599@gmail.com", "23aADFEfsfsdfs"))
    root.mainloop()

if __name__ == "__main__":
    main()