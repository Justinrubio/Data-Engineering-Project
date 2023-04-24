
from tkinter import ttk
from tkinter import messagebox


import tkinter as tk
import sqlite3

LARGE_FONT = ("Verdana", 12)


class InternApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in {StartPage, PageOne, PageTwo, AddInternship, mainPage}:
            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(StartPage)
        #self.frames[mainPage] = mainPage(self.container)
        #self.frames[AddInternship] = AddInternship(self.container)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Internship Application", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Register",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.parent = parent
        self.conn = sqlite3.connect("internship.db")
        self.cursor = self.conn.cursor()
        self.label_id = tk.Label(self, text="ID:")
        self.label_id.pack()
        self.enter_id = tk.Entry(self)
        self.enter_id.pack()
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.pack()
        self.enter_name = tk.Entry(self)
        self.enter_name.pack()
        self.button_register = tk.Button(self, text="Register", command=self.register)
        self.button_register.pack()


        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #button2 = tk.Button(self, text="Page Two",
          #                  command=lambda: controller.show_frame(PageTwo))
        #button2.pack()

    def register(self, **kwargs):
        ID = self.enter_id.get()
        name = self.enter_name.get()

        self.cursor.execute("SELECT COUNT(*) FROM students WHERE ID = ?", (ID,))
        result = self.cursor.fetchone()

        if result[0] > 0:
            tk.messagebox.showerror("Error", f"Student with ID {ID} already exists.")
        else:
            self.cursor.execute("INSERT INTO students (ID, name) VALUES (?, ?)", (ID, name))
            self.conn.commit()
            self.enter_name.delete(0, "end")
            self.enter_id.delete(0, "end")
            self.enter_name.focus()
            tk.messagebox.showinfo("Registration", "Student registered successfully.")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.parent = parent
        self.conn = sqlite3.connect("internship.db")
        self.cursor = self.conn.cursor()

        self.label_id = tk.Label(self, text="ID:")
        self.label_id.pack()

        self.enter_id = tk.Entry(self)
        self.enter_id.pack()

        self.label_name = tk.Label(self, text="Name:")
        self.label_name.pack()

        self.enter_name = tk.Entry(self)
        self.enter_name.pack()

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack()



        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        self.controller = controller

    def login(self):
        ID = self.enter_id.get()
        name = self.enter_name.get()

        self.cursor.execute("SELECT * FROM students WHERE ID=? AND name=?", (ID, name))
        result = self.cursor.fetchone()

        if result:
            self.controller.show_frame(mainPage)

        else:
            tk.messagebox.showerror("Error", "Invalid ID or name.")
    def showSecondaryFrame(self, myFrame):
        secFrame = self.frames[myFrame]
        secFrame.tkraise()

class mainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Add Internship",
                           command=lambda: controller.show_frame(AddInternship))
        button.pack()

        button = tk.Button(self, text="Edit Internship",
                           command=lambda controller.show_frame(editInternship))

        controller.frames[AddInternship] = AddInternship(parent, controller)

class AddInternship(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Create labels and entry fields for the internship details
        tk.Label(self, text="Internship Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Student ID:").grid(row=1, column=0, padx=10, pady=10)
        self.s_id_entry = tk.Entry(self)
        self.s_id_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Tag ID:").grid(row=2, column=0, padx=10, pady=10)
        self.tag_id_entry = tk.Entry(self)
        self.tag_id_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Start Date:").grid(row=3, column=0, padx=10, pady=10)
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self, text="End Date:").grid(row=4, column=0, padx=10, pady=10)
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="Company ID:").grid(row=5, column=0, padx=10, pady=10)
        self.c_id_entry = tk.Entry(self)
        self.c_id_entry.grid(row=5, column=1, padx=10, pady=10)

        # Create a button to add the internship to the database
        add_button = tk.Button(self, text="Add Internship", command=self.add_internship)
        add_button.grid(row=6, column=1, padx=10, pady=10)

        # Create a button to go back to the main menu
        main_menu_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("mainPage"))
        main_menu_button.grid(row=6, column=0, padx=10, pady=10)

    def add_internship(self):
        title = self.title_entry.get()
        s_id = self.s_id_entry.get()

        tag_id = self.tag_id_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        c_id = self.c_id_entry.get()

        # Connect to the database
        conn = sqlite3.connect('internship.db')
        c = conn.cursor()

        # Insert the values into the internship table
        c.execute("INSERT INTO internship (title, s_id, tag_id, start_date, end_date, c_id) VALUES (?, ?, ?, ?, ?, ?)",
                  (title, s_id, tag_id, start_date, end_date, c_id))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Clear the entry fields
        self.title_entry.delete(0, tk.END)
        self.s_id_entry.delete(0, tk.END)
        self.tag_id_entry.delete(0, tk.END)

    def go_to_mainPage(self):
        # Destroy the current window
        self.destroy()

        # Create the main menu window
        root = tk.Tk()
        main_menu = mainPage(root)
        main_menu.mainloop()



app = InternApp()
app.mainloop()