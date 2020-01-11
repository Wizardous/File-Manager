from tkinter import *
import Framework.ui._handlers as handle

class Logout(Frame):
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
            text="Quit ?",
            anchor='w',
            font=("Montserrat", 30),
            width = 15,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        self.title_lbl.place(relx=0.83, rely=0.4, anchor='e')

        # ------------- Confirm Frame --------------------------------
        self.confirm_Frame = Frame(
            self._master,
            height=self._master['height'] * 0.7,
            width=self._master['width'] * 0.9,
            bg=self.col_page_bg
        )
        self.confirm_Frame.place(relx=0.5, rely=0.22, anchor="n")
        self.frame_list.append((self.confirm_Frame))

        question_Label = Label(
            self.confirm_Frame,
            text="Closing the app will log you out, are you srue?",
            anchor='w',
            font=("Montserrat", 13),
            width=35,
            bg=self.col_page_bg,
            fg=self.col_fg,
        )
        question_Label.place(relx=0.03, rely=0.0, anchor='nw')

        confirm_Btn = Button(
            self.confirm_Frame,
            text="Confirm",
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command = self.confirm_Event,
        )
        confirm_Btn.place(relx=0.05, rely=0.25, anchor='w')

        cancel_Btn = Button(
            self.confirm_Frame,
            text="Cancel",
            width=12,
            bd=0,
            font=("Montserrat", 14),
            bg=self.col_btn_default,
            fg=self.col_fg,
            activebackground=self.col_btn_clicked,
            activeforeground=self.col_fg,
            command = self.cancel_Event,
        )
        cancel_Btn.place(relx=0.4, rely=0.25, anchor='w')

    def confirm_Event(self):
        print("Confirm")
        handle.Exit()

    def cancel_Event(self):
        print("Cancel")
        handle.cancel_Exit()

    def close(self):
        for frame in self.frame_list:
            frame.destroy()