from tkinter import *
from Framework.ui._viewRecords import ViewRecords
from Framework.ui._addRecords import AddRecords
from Framework.ui._updateRecords import UpdateRecords
from Framework.ui._deleteRecords import DeleteRecords
from Framework.ui._logout import Logout
import  Framework.ui._handlers as handle


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
        self.col_tab_default_bg = "#34344b"
        self.col_activeTab_fg = '#4dffa3'

        self._master.title("Navigation Page")
        self._master.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))
        self._master.resizable(False, False)

        self.button_dict = {}

        self.initUI()

        self.current_page = ViewRecords(self.pageFrame)
        self.change_page(ViewRecords)

    def change_page(self, class_name):
        if class_name.__name__ != type(self.current_page).__name__:
            self.current_page.close()
            del self.current_page
            self.current_page = class_name(self.pageFrame)
            current_class = class_name.__name__
            self._master.title('NavPage - '+current_class)
            for c in self.button_dict:
                if c != current_class:
                    self.button_dict[c]['bg'] = self.col_tab_default_bg
                    self.button_dict[c]['fg'] = self.col_fg
                else:
                    self.button_dict[c]['bg'] = self.col_pageFrame_bg
                    self.button_dict[c]['fg'] = self.col_activeTab_fg


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
                                  bg = self.col_pageFrame_bg,
                                  fg = self.col_activeTab_fg,
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
        self.button_dict['ViewRecords'] = self.navBtn_View

        self.navBtn_Add = Button(self.navFrame,
                                 text = 'Add',
                                 bg = self.col_tab_default_bg,
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
        self.button_dict['AddRecords'] = self.navBtn_Add

        self.navBtn_Update = Button(self.navFrame,
                                  text = 'Update',
                                  bg = self.col_tab_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                  command=lambda: self.change_page(UpdateRecords)
                                  )
        self.navBtn_Update.place(relx=0.3, rely=0.34, anchor='w')
        self.button_dict['UpdateRecords'] = self.navBtn_Update

        self.navBtn_Delete = Button(self.navFrame,
                                  text = 'Delete',
                                  bg = self.col_tab_default_bg,
                                  fg = self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                  command=lambda: self.change_page(DeleteRecords)
                                  )
        self.navBtn_Delete.place(relx=0.3, rely=0.46, anchor='w')
        self.button_dict['DeleteRecords'] = self.navBtn_Delete

        self.navBtn_Exit = Button(self.navFrame,
                                  text = 'Exit',
                                  bg = self.col_tab_default_bg,
                                  fg = '#00cc99',  #self.col_fg,
                                  activebackground = self.btn_clicked,
                                  activeforeground = '#00cc99',  #self.col_fg,
                                  width = 20,
                                  font = "Montserrat 12",
                                  justify= 'left',
                                  anchor = 'w',
                                  bd = 0,
                                  command=lambda: self.change_page(Logout)
                                  )
        self.navBtn_Exit.place(relx=0.3, rely=0.9, anchor='w')
        self.button_dict['Logout'] = self.navBtn_Exit


def main():
    handle.root = Tk()

    handle.navigation_page = Nav_Frame(handle.root)

    handle.root.mainloop()

if __name__ == "__main__":
    main()
