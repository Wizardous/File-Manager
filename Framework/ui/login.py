from tkinter import *
import tkinter as tk
from threading import Thread

from Framework.ui.navPage import Nav_Frame
from Framework.api.login_api import Login
import Framework.ui._handlers as handle


class Login_form(Frame):
    def __init__(self, parent):
        self._master = parent
        super().__init__(self._master)

        self.height = 400
        self.width = 350

        w = self._master.winfo_screenwidth()
        h = self._master.winfo_screenheight()

        x = (w//2) - (self.width//2)
        y = (h//2) - (self.height//2)

        self.col_bg = '#2b2b3d'
        self.col_fg = '#05ff7e'
        self.entry_bg = '#1e1e2b'
        self.btn_clicked = "#323247"
        self.btn_default = "#36364d"

        self._master.title("Login")
        self._master.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))
        self._master.resizable(False, False)
        self.__auth_running = False

        self.__login_api = Login()
        self.frame_List = []
        self.initUI()
        
    
    def initUI(self):
        self.img_frame = Frame(self._master,
                                bg = self.col_bg,
                                height = int(self.height *0.35),
                                width = self.width
                                )
        self.img_frame.pack()
        self.frame_List.append(self.img_frame)

        self.label1 = Label(self.img_frame, text="{LogIn}",
                            bg = self.col_bg,
                            fg = self.col_fg,
                            font = "Montserrat 35",
                            )
        self.label1.place(relx=0.5, rely=0.2, anchor='n')

        self.login_frame = Frame(self._master,
                                bg = self.col_bg,
                                height = int(self.height*0.65),
                                width = self.width
                                )
        self.login_frame.pack()
        self.frame_List.append(self.login_frame)

        self.username_string = StringVar()
        self.password_string = StringVar()

        self.label2 = Label(self.login_frame,
                            text = 'Username :',
                            bg = self.col_bg,
                            fg = self.col_fg,
                            font = 'Montserrat 11',
                            )
        self.label2.place(relx=0.18, rely=0.01, anchor='w')

        self.username_entry = Entry(self.login_frame,
                              bg = self.entry_bg,
                              fg = self.col_fg,
                              bd = 0,
                              width = 17,
                              font="Montserrat 15",
                              justify = 'center', 
                              textvariable=self.username_string
                              )
        self.username_entry.place(relx=0.5, rely=0.06, anchor='n')

        self.label3 = Label(self.login_frame,
                            text = 'Password :',
                            bg = self.col_bg,
                            fg = self.col_fg,
                            font = 'Montserrat 11',
                            )
        self.label3.place(relx=0.18, rely=0.25, anchor='w')

        self.password_entry = Entry(self.login_frame,
                              bg = self.entry_bg,
                              fg = self.col_fg,
                              bd = 0,
                              width = 17,
                              show="\u2022",
                              font="Montserrat 15",
                              justify = 'center', 
                              textvariable=self.password_string
                              )
        self.password_entry.place(relx=0.5, rely=0.3, anchor='n')

        self.submit_button = Button(self.login_frame,
                                    text = 'Login',
                                    bg = self.btn_default,
                                    fg = self.col_fg,
                                    font = "Montserrat 12",
                                    width = 12,
                                    activebackground = self.btn_clicked,
                                    activeforeground = self.col_fg,
                                    justify = 'center',
                                    bd = 0,
                                    command = self.try_login)
        self.submit_button.place(relx=0.5, rely=0.50, anchor='n')

        self.signUP_lbl = Label(self.login_frame,
                                text = "New to this App | Sign up here",
                                justify = 'center',
                                bg = self.col_bg,
                                fg = self.col_fg
                                )
        self.signUP_lbl.place(relx=0.5, rely=0.95, anchor='s')

        

    def try_login(self):
        if not self.__auth_running:
            print("Trying Authentication...")
            self.__auth_running = True
            auth = Thread(target=self.__auth)
            auth.start()

    def __auth(self):
        result = self.__login_api.authenticate(self.username_string.get(),
                                               self.password_string.get())
        
        if result:
            print("success")
            self.close_ui()
            handle.navigation_page = Nav_Frame(self._master)
        else :
            print("Failed")

    def close_ui(self):
        for frame in self.frame_List:
            frame.destroy()



def main():
    handle.root = tk.Tk()
    
    handle.login_frame = Login_form(handle.root)

    handle.root.mainloop()


if __name__ == "__main__":
    main()