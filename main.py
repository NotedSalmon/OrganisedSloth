import tkinter as tk
from ui.LoginPage import LoginPage
from ui.RegisterPage import RegisterPage

class OrganisedSloth(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OrganisedSloth")
        self.geometry("800x500")
        self.minsize(600, 400)

        self.current_user = None

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for PageClass in (LoginPage, RegisterPage):
            page = PageClass(container, self)
            self.pages[PageClass.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

if __name__ == "__main__":
    app = OrganisedSloth()
    app.mainloop()
