import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        tk.Label(self,text="OrganisedSloth", font=("Arial", 20, "bold")).pack(pady=(60, 20))

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.login).pack(pady=15)

        # Sends user to the RegisterPage defined in the main.py PageClass
        tk.Button(self, text="Register", command=lambda: app.show_page("RegisterPage")).pack()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        """ This will be changed to call the service once it is implemented """

