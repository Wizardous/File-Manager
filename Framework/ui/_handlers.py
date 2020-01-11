from Framework.ui._viewRecords import ViewRecords

root = None
login_frame = None
navigation_page = None

def cancel_Exit():
    print("123")
    navigation_page.change_page(ViewRecords)
    pass

def Exit():
    root.destroy()
    print('Bye')
    pass