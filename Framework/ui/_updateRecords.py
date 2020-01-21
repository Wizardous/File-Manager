from tkinter import *
from Framework.api.records import Records
from passlib.context import CryptContext

def hashPassword(password):
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )
    return pwd_context.hash(password)

class UpdateRecords(Frame):
    def __init__(self, parent_frame):
        self._master = parent_frame
        super().__init__(self._master)

        self.col_bg = '#2b2b3d'
        self.col_fg = '#05ff7e'
        self.entry_bg = '#1e1e2b'
        self.entry_fg_disabled = '#00e66f'
        self.col_btn_clicked = "#323247"
        self.col_btn_default = "#36364d"

        self.col_page_bg = "#3f3f5a"
        self.col_list_bg = "#34344b"
        self.col_list_fg = "#00cc63"
        self.col_selected_bg = "#2a2a3c"
        self.col_selected_fg = "#99ff99"

        self.col_log_error = "#ffad33"
        self.col_log_success = "#79ff4d"

        self.frame_list = []
        self.file_api = Records()
        self.current_record = ["", "", ""]

        self.initFrame()

    def __validateUsername(self, username):
        username_re = r"^[a-zA-Z0-9_.-]+$"
        return True if re.match(username_re, username) else False

    def __validateEmail(self, email):
        email_re = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        return True if re.match(email_re, email) else False

    def __validatePassword(self, password):
        charRegex = re.compile(r'(\w{8,})')  # Check if password has atleast 8 characters
        lowerRegex = re.compile(r'[a-z]+')  # Check if at least one lowercase letter
        upperRegex = re.compile(r'[A-Z]+')  # Check if atleast one upper case letter
        digitRegex = re.compile(r'[0-9]+')  # Check if at least one digit.
        result = charRegex.findall(password) != [] and \
                 lowerRegex.findall(password) != [] and \
                 upperRegex.findall(password) != [] and \
                 digitRegex.findall(password) != []
        return result

    def __alert(self, mode, text):
        if mode == "ERROR":
            self.error_Label['fg'] = self.col_log_error
            self.error_Label['text'] = text

        elif mode == "LOG":
            self.error_Label['fg'] = self.col_log_success
            self.error_Label['text'] = text

        self.password_String.set("")
        self.confirm_String.set("")

    def __clearForm(self):
        self.search_String.set("")
        self.username_String.set("")
        self.email_String.set("")
        self.password_String.set("")
        self.confirm_String.set("")

        self.username_check_Var.set(False)
        self.email_check_Var.set(False)
        self.password_check_Var.set(False)

    def __validateForm(self, username, email, password):
        if self.__validateUsername(username):
            if self.__validateEmail(email):
                if self.password_check_Var.get():
                    if self.__validatePassword(password):
                        return True
                    else:
                        self.__alert(mode="ERROR", text="Password Invalid.")
                        return False
                else:
                    return True
            else:
                self.__alert(mode="ERROR", text="Email Invalid")
                return False
        else:
            self.__alert(mode="ERROR", text="Username Invalid")
            return False

    def updateRecord(self):
        username = self.username_String.get()
        email = self.email_String.get()
        password = self.password_String.get() if self.password_check_Var.get() else self.current_record[2]
        confirm = self.confirm_String.get()

        if self.password_check_Var.get():
            if not len(password):
                self.__alert(mode="ERROR", text="Password Field Empty")
                return
            elif not len(confirm):
                self.__alert(mode="ERROR", text="Confirm field empty.")
                return
            elif password != confirm:
                self.__alert(mode="ERROR", text="Password Confirmations don't match.")
                return

        if self.password_check_Var.get() or self.email_check_Var.get() or self.username_check_Var.get():
            if self.__validateForm(username, email, password):
                self.__alert(mode="LOG", text="Record Added Successfully!")
                if self.password_check_Var.get():
                    password = hashPassword(password)
                data = {"username": username, "email": email, "pass": password}
                self.file_api.updateRecord(key=self.current_record[0], new_data=data)
                self.__clearForm()

    def __populateForm(self, data=None):
        if data:
            self.current_record = data
            username, email = data[0], data[1]
            self.username_String.set(username)
            self.email_String.set(email)
        else:
            username, email = "", ""
            self.username_String.set(username)
            self.email_String.set(email)

    def __searchTrace(self, *args):
        search_key = self.search_String.get()
        status, result = self.file_api.searchRecords(key=search_key, mode='username')

        if status:
            self.__populateForm(data = result[0][1])
            # print(result)
        else:
            self.__populateForm()

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
            text = "Search Username : ",
            font = "Montserrat 11",
            bg = self.col_page_bg,
            fg = self.col_fg
        )
        search_Label.place(relx=0.005, rely=0.2, anchor='w')
        search_Label.focus_force()

        self.search_String = StringVar()
        self.search_String.trace('w', self.__searchTrace)
        search_Entry = Entry(
            self.search_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            width=20,
            font="Montserrat 13",
            justify='left',
            textvariable=self.search_String
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
            disabledbackground = self.entry_bg,
            disabledforeground=self.entry_fg_disabled,
            width=27,
            font="Montserrat 15",
            justify='left',
            state = DISABLED,
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
            disabledbackground=self.entry_bg,
            disabledforeground=self.entry_fg_disabled,
            width=27,
            font="Montserrat 15",
            justify='left',
            state=DISABLED,
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
            disabledbackground = self.entry_bg,
            disabledforeground=self.entry_fg_disabled,
            width=13,
            font="Montserrat 15",
            justify='left',
            show="\u2022",
            state=DISABLED,
            textvariable=self.password_String
        )
        self.password_Entry.place(relx=0.425+x, rely=0.64, anchor='ne')

        self.confirm_String = StringVar()
        self.confirm_Entry = Entry(
            self.edit_Frame,
            bg=self.entry_bg,
            fg=self.col_fg, bd=0,
            disabledbackground=self.entry_bg,
            disabledforeground=self.entry_fg_disabled,
            width=13,
            font="Montserrat 15",
            justify='left',
            show="\u2022",
            state=DISABLED,
            textvariable=self.confirm_String
        )
        self.confirm_Entry.place(relx=0.8+x, rely=0.64, anchor='ne')

        add_Btn = Button(
            self.edit_Frame,
            text="Update",
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command = self.updateRecord,
        )
        add_Btn.place(relx=0.23, rely=0.8, anchor='n')

        self.error_Label = Label(
            self.edit_Frame,
            text="Select checkbox to edit...",
            anchor='w',
            font=("Montserrat", 11),
            bg=self.col_page_bg,
            fg=self.col_log_success,
        )
        self.error_Label.place(relx=0.4 + x, rely=0.85, anchor='nw')


    def changeStatus(self):
        self.username_Entry.config(state = "normal" if self.username_check_Var.get() else "disabled")
        self.email_Entry.config(state="normal" if self.email_check_Var.get() else "disabled")
        self.password_Entry.config(state="normal" if self.password_check_Var.get() else "disabled")
        self.confirm_Entry.config(state="normal" if self.password_check_Var.get() else "disabled")

        if not self.username_check_Var.get():
            self.username_String.set(self.current_record[0])
        if not self.email_check_Var.get():
            self.email_String.set(self.current_record[1])
        if not self.password_check_Var.get():
            self.password_String.set("")
            self.confirm_String.set("")

    def close(self):
        for frame in self.frame_list:
            frame.destroy()