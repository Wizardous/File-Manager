from tkinter import *
import re
from Framework.api.records import Records
from passlib.context import CryptContext

def hashPassword(password):
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )
    return pwd_context.hash(password)


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

        self.col_log_error = "#ffad33"
        self.col_log_success = "#79ff4d"

        self.frame_list = []
        self.initFrame()
        self.file_api = Records()

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
        self.userName_String.set("")
        self.email_String.set("")
        self.password_String.set("")
        self.confirm_String.set("")

    def __validateForm(self, username, email, password):
        if self.__validateUsername(username):
            if self.__validateEmail(email):
                if self.__validatePassword(password):
                    return True
                else:
                    self.__alert(mode="ERROR", text="Password Invalid.")
                    return False
            else:
                self.__alert(mode="ERROR", text="Email Invalid")
                return False
        else:
            self.__alert(mode="ERROR", text="Username Invalid")
            return False

    def addRecord(self):
        username = self.userName_String.get()
        email = self.email_String.get()
        password = self.password_String.get()
        confirm = self.confirm_String.get()

        if password == confirm and len(password):
            if self.__validateForm(username, email, password):
                self.__alert(mode="LOG", text="Record Added Successfully!")
                data = {"username": username, "email": email, "pass": hashPassword(password)}
                self.file_api.addRecord(data)
                self.__clearForm()

        elif not len(password):
            self.__alert(mode="ERROR", text="Password Field Empty")
        elif not len(confirm):
            self.__alert(mode="ERROR", text="Confirm field empty.")
        elif password != confirm:
            self.__alert(mode="ERROR", text="Password Confirmations did not matched.")

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
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command = self.addRecord,
        )
        add_Btn.place(relx=0.23, rely=0.72, anchor='n')

        self.error_Label = Label(
            self.input_Frame,
            text="",
            anchor='w',
            font=("Montserrat", 11),
            bg=self.col_page_bg,
            fg=self.col_log_success,
        )
        self.error_Label.place(relx=0.08, rely=0.9, anchor='nw')

    def close(self):
        for frame in self.frame_list:
            frame.destroy()