
import tkinter as tk


class RegisterPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        tk.Label(self, text="Create an Account", font=("Arial", 20, "bold")).pack(pady=(60, 20))

        tk.Label(self, text="Choose a username").pack()
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Choose a password").pack()
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Create Account").pack(pady=15)

        tk.Button(self, text="Back to Login", command=lambda: self.app.show_page("LoginPage")).pack()
