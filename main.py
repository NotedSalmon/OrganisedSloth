import tkinter as tk
from ui.LoginPage import LoginPage
from ui.RegisterPage import RegisterPage

class OrganisedSloth(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main window settings
        self.title("OrganisedSloth")
        self.geometry("800x500")
        self.minsize(600, 400)

        # Will come in handy later on
        self.current_user = None 

        # Container holds all the pages and makes it fill the window
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creates each pages and iterates through PageClass which is then used to navigate between pages
        # Makes it so it doesn't open a new window each time the page changes i.e Login -> Register
        self.pages = {}

        for PageClass in (LoginPage, RegisterPage):
            page = PageClass(container, self)
            self.pages[PageClass.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Shows login page first, could be changed later
        self.show_page("LoginPage")

    def show_page(self, page_name):
        # Since the pages are all stacked on top of each other, this brings requested page to the front
        page = self.pages[page_name]
        page.tkraise()

if __name__ == "__main__":
    app = OrganisedSloth()
    app.mainloop()
