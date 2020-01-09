from tkinter import *
from threading import Thread
from Framework.api.records_manager import *

from _viewRecords import ViewRecords
from _addRecords import AddRecords

class Nav_Frame(Frame):
    def __init__(self, parent):
        self._master = parent
        super().__init__(self._master)

        w = self._master.winfo_screenwidth()
        h = self._master.winfo_screenheight()

        self.width = int(w * 0.5)
        self.height = int(h * 0.55)

        x = (w//2) - (self.width//2)
        y = (h//2) - (self.height//2)

        self.col_bg = '#2b2b3d'
        self.col_fg = '#05ff7e'
        self.entry_bg = '#1e1e2b'
        self.btn_clicked = "#323247"
        self.btn_default = "#36364d"

        self.col_pageFrame_bg = "#3f3f5a"
        self.col_navBtn_default_bg = "#35354b" 

        self._master.title("Navigation Page")
        self._master.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))
        self._master.resizable(False, False)

        self.initUI()

        self.current_page = ViewRecords(self.pageFrame)

    def change_page(self, class_name):
        self.current_page.close()
        del self.current_page
        self.current_page = class_name(self.pageFrame)


    def initUI(self):
        self.navFrame = Frame(self._master,
                            bg = self.col_bg,
                            height = self.height,
                            width = self.width * 0.3)
        self.navFrame.grid(row=0, column=0)
        
        self.pageFrame = Frame(self._master,
                            bg = self.col_pageFrame_bg,
                            height = self.height,
                            width = self.width * 0.7)
        self.pageFrame.grid(row=0, column=1)

        self.navBtn_View = Button(self.navFrame,
                                  text = 'View Records',
                                  bg = self.col_navBtn_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                  command = lambda : self.change_page(ViewRecords)
                                )
        self.navBtn_View.place(relx=0.3, rely=0.1, anchor='w')

        self.navBtn_Add = Button(self.navFrame,
                                  text = 'Add',
                                  bg = self.col_navBtn_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                 command=lambda: self.change_page(AddRecords)
                                )
        self.navBtn_Add.place(relx=0.3, rely=0.22, anchor='w')

        self.navBtn_View = Button(self.navFrame,
                                  text = 'Update',
                                  bg = self.col_navBtn_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                )
        self.navBtn_View.place(relx=0.3, rely=0.34, anchor='w')

        self.navBtn_View = Button(self.navFrame,
                                  text = 'Delete',
                                  bg = self.col_navBtn_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                )
        self.navBtn_View.place(relx=0.3, rely=0.46, anchor='w')

        self.navBtn_View = Button(self.navFrame,
                                  text = 'Search Records',
                                  bg = self.col_navBtn_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                )
        self.navBtn_View.place(relx=0.3, rely=0.58, anchor='w')

        self.navBtn_View = Button(self.navFrame,
                                  text = 'Logout',
                                  bg = self.col_navBtn_default_bg,
                                  fg = '#00cc99', #self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = '#00cc99', #self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                )
        self.navBtn_View.place(relx=0.3, rely=0.9, anchor='w')


def main():
    root = Tk()

    nav_frame = Nav_Frame(root)

    root.mainloop()

if __name__ == "__main__":
    main()
