import sqlite3
from tkinter import *




root = Tk()

Label(root, text="Student Name").grid(row=0, column=0)
student_name_entry = Entry(root)
student_name_entry.grid(row=0, column=1)

Label(root, text="Student ID").grid(row=1, column=0)
id_entry = Entry(root)
id_entry.grid(row=1, column=1)

def register():
    student_name = student_name_entry.get()
    student_id = id_entry.get()

    conn = sqlite3.connect('internship.db')
    myCursor = conn.cursor()
    myCursor.execute("SELECT ID FROM students WHERE ID = ?", (student_id,))
    existing_student = myCursor.fetchone()

    if existing_student:
        # update existing row
        myCursor.execute("UPDATE students SET name = ? WHERE ID = ?", (student_name, student_id))
    else:
        # insert new row
        myCursor.execute("INSERT INTO students (ID, name) VALUES (?, ?)", (student_id, student_name))
    conn.commit()
    conn.close()
def login():
    student_id = id_entry.get()
    login_conn = sqlite3.connect('internship.db')
    my_cursor = login_conn.cursor()

    

Button(root, text="Register", command=register).grid(row=3, column=0, columnspan=2)

root.mainloop()
