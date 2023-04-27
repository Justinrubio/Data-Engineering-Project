
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

        for F in {StartPage, PageOne, PageTwo, AddInternship, editInternship, ListInternship, SearchInternship, mainPage}:
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
    def __init__(self, parent, controller, ):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Add Internship",
                           command=lambda: controller.show_frame(AddInternship))
        button.pack()
        controller.frames[AddInternship] = AddInternship(parent, controller)

        button2 = tk.Button(self, text="Edit Internship",
                           command=lambda: controller.show_frame(editInternship))
        button2.pack()


        controller.frames[editInternship] = editInternship(parent, controller)

        button2 = tk.Button(self, text="Internship List",
                            command=lambda: controller.show_frame(ListInternship))
        button2.pack()
        controller.frames[ListInternship] = ListInternship(parent, controller)

        button3 = tk.Button(self, text="Search for internship",
                            command=lambda: controller.show_frame(SearchInternship))
        button3.pack()
        controller.frames[SearchInternship] = SearchInternship(parent, controller)


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
        button_cancel = tk.Button(self, text="Cancel", command=self.cancel_add)
        button_cancel.grid(row=6, column=1, padx=10, pady=10)


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
        #May changes (s_id doesnt need to be filled out)
        c.execute("INSERT INTO internship (title, s_id, tag_id, start_date, end_date, c_id) VALUES (?, ?, ?, ?, ?, ?)",
                  (title, s_id, tag_id, start_date, end_date, c_id))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Clear the entry fields
        self.title_entry.delete(0, tk.END)
        self.s_id_entry.delete(0, tk.END)
        self.tag_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.c_id_entry.delete(0, tk.END)

    def cancel_add(self):
        # Destroy the current window
        self.controller.show_frame(mainPage)



class editInternship(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent




        label = tk.Label(self, text="Edit Internship", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.conn = sqlite3.connect("internship.db")
        self.cursor = self.conn.cursor()

        self.student_id_label = tk.Label(self, text= "Enter Student ID: ")
        self.student_id_label.pack()

        self.student_id_enter = tk.IntVar()
        self.student_id_enter_dig = tk.Entry(self, textvariable=self.student_id_enter)
        self.student_id_enter_dig.pack()

        self.label_title = tk.Label(self, text="Edit Title: ")
        self.label_title.pack()

        self.title_edit = tk.StringVar()
        self.enter_title = tk.Entry(self, textvariable=self.title_edit)
        self.enter_title.pack()

        self.label_tag_id = tk.Label(self, text="Edit Tag Id: ")
        self.label_tag_id.pack()

        self.tag_id_edit = tk.IntVar()
        self.tag_id_enter = tk.Entry(self, textvariable=self.tag_id_edit)
        self.tag_id_enter.pack()

        self.label_start_date = tk.Label(self, text="Edit Start Date: ")
        self.label_start_date.pack()

        self.start_date_edit = tk.IntVar()
        self.start_date_enter = tk.Entry(self, textvariable=self.start_date_edit)
        self.start_date_enter.pack()

        self.label_end_date = tk.Label(self, text="Edit End Date: ")
        self.label_end_date.pack()

        self.end_date_edit = tk.IntVar()
        self.end_date_enter = tk.Entry(self, textvariable=self.end_date_edit)
        self.end_date_enter.pack()

        self.label_c_id = tk.Label(self, text="Edit Company ID: ")
        self.label_c_id.pack()

        self.c_id_edit = tk.IntVar()
        self.c_id_enter = tk.Entry(self, textvariable=self.c_id_edit)
        self.c_id_enter.pack()

        self.button_edit = tk.Button(self, text="Edit Internship", command=self.edit_internship)
        self.button_edit.pack()

        self.button_cancel = tk.Button(self, text="Cancel", command=self.cancel_edit)
        self.button_cancel.pack()

        self.load_intern_data()


    def load_intern_data(self):
        new_data = self.student_id_enter.get()
        self.cursor.execute("SELECT * FROM internship WHERE s_id=?", (new_data,))
        load_data_result = self.cursor.fetchone()

        if load_data_result:
            self.title_edit.set(load_data_result[1])
            self.tag_id_edit.set(load_data_result[2])
            self.start_date_edit.set(load_data_result[3])
            self.end_date_edit.set(load_data_result[4])
            self.c_id_edit.set(load_data_result[5])

    def edit_internship(self):
        title = self.title_edit.get()
        tag_id = self.tag_id_edit.get()
        start_date = self.start_date_edit.get()
        end_date = self.end_date_edit.get()
        c_id = self.c_id_edit.get()

        self.cursor.execute("UPDATE internship SET title=?, tag_id=?, start_date=?, end_date=?, c_id=? WHERE ID=?", (title, tag_id, start_date, end_date, c_id))
        self.conn.commit()
        tk.messagebox.showinfo("Success", "Internship updated successfully.")

    def cancel_edit(self):
        self.controller.show_frame(mainPage)

class ListInternship(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Internship List", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.tree = ttk.Treeview(self, columns=("ID", "title", "Tag ID", "Start Date", "End Date", "Company ID"))
        self.tree.heading("ID", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("Tag ID", text="Tag ID")
        self.tree.heading("Start Date", text="Start Date")
        self.tree.heading("End Date", text="End Date")
        self.tree.heading("Company ID", text="Company ID")
        self.tree.pack()

        self.conn = sqlite3.connect("internship.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM internship")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        self.button_cancel = tk.Button(self, text="Cancel", command=self.cancel_list)
        self.button_cancel.pack()

    def cancel_list(self):
        self.controller.show_frame(mainPage)


class SearchInternship(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Search Internship", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.parent = parent
        self.conn = sqlite3.connect("internship.db")
        self.cursor = self.conn.cursor()

        self.label_c_id = tk.Label(self, text="Enter Comapny ID:")
        self.label_c_id.pack()

        self.enter_c_id = tk.Entry(self)
        self.enter_c_id.pack()

        self.label_tag_id = tk.Label(self, text="Enter Tag ID:")
        self.label_tag_id.pack()

        self.enter_tag_id = tk.Entry(self)
        self.enter_tag_id.pack()

        self.label_Start_date = tk.Label(self, text="Enter Start Date:")
        self.label_Start_date.pack()

        self.enter_Start_date = tk.Entry(self)
        self.enter_Start_date.pack()

        self.label_End_date = tk.Label(self, text="Enter End Date:")
        self.label_End_date.pack()

        self.enter_End_date = tk.Entry(self)
        self.enter_End_date.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.pack()


    def search(self):
        c_id = self.enter_c_id.get()
        tag_id = self.enter_tag_id.get()
        start_date = self.enter_Start_date.get()
        end_date = self.enter_End_date.get()

        self.cursor.execute("SELECT * FROM internship WHERE c_id=? OR tag_id=? OR start_date=? OR end_date=?", (c_id, tag_id, start_date, end_date))
        results = self.cursor.fetchall()

        if results:
            self.display_results(results)
    def display_results(self, results):

        results_frame = tk.Frame(self)
        results_frame.pack()

        header = ["ID", "Company ID", "Tag ID", "Start Date", "End Date"]
        for i, col_name in enumerate(header):
            header_label = tk.Label(results_frame, text=col_name, font=('Arial', 14, 'bold'))
            header_label.grid(row=0, column=i, padx=5, pady=5)

        for row_num, row_data in enumerate(results):
            for col_num, col_data in enumerate(results):
                result_label = tk.Label(results_frame, text=str(row_data[col_num]))
                result_label.grid(row=row_num+1, column=col_num, padx=5, pady=5)













app = InternApp()
app.mainloop()