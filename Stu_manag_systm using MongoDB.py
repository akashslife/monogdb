from pymongo import MongoClient
from random import randint
import tkinter as tk
from tkinter import messagebox
#https://pymongo.readthedocs.io/en/stable/tutorial.html batter ways 
try:
    client = MongoClient(port=27017)
    db = client.Assignment08
    print("Connected to MongoDB")
except Exception as e:
    print("Database connection Error:", e)
    messagebox.showerror("Error", "Connection Error")
    exit(1)

root = tk.Tk()
root.geometry('400x350')
root.title("Student Management System")

# adding the and update or entring the students or we can change the data 
def add_students():
    def add_query():
        reg_no = reg_no_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        batch = batch_entry.get()
        mobile = mobile_entry.get()
        
        # Validate inputs
        if not all((reg_no, name, email, batch)):
            messagebox.showwarning("WARNING", "All fields are compulsory (Except: Mobile number)")
            return

        if "@" not in email:
            messagebox.showwarning("WARNING", "Please enter a valid email address")
            return
        
        # Additional validation checks
        if len(reg_no) != 8 or not reg_no.isdigit():
            messagebox.showwarning("WARNING", "Registration Number must be an 8-digit number")
            return
        
        if not name.isalpha():
            messagebox.showwarning("WARNING", "Name should only contain alphabets")
            return
        ####
        # it can add or removing condition for ex. 2020 to 2024 or like completion cour. subject...

        # if len(batch) != 4 or not batch.isdigit():
        #     messagebox.showwarning("WARNING", "Batch should be a 4-digit year")
        #     return
        
        if mobile and (not mobile.isdigit() or len(mobile) != 10):
            messagebox.showwarning("WARNING", "Mobile number should be a 10-digit number")
            return


#if ' it can adding more check points for error or improving the conditions else gets the error massGE well be pop up


        student = {
            'Registration_No': reg_no,
            'Name': name,
            'Email': email,
            'Batch': batch,
            'Mobile': mobile
        }
        
        db.students.insert_one(student)
        newwin.destroy()
        messagebox.showinfo("Add Student", "Student Added")

    newwin = tk.Toplevel(root)
    newwin.geometry('400x400')
    newwin.title("Add Students")

    tk.Label(newwin, text="Registration Number").grid(row=0, column=0)
    tk.Label(newwin, text="Name").grid(row=1, column=0)
    tk.Label(newwin, text="Email").grid(row=2, column=0)
    tk.Label(newwin, text="Batch").grid(row=3, column=0)
    tk.Label(newwin, text="Mobile").grid(row=4, column=0)

    reg_no_entry = tk.Entry(newwin, bd=7)
    reg_no_entry.grid(row=0, column=1)
    name_entry = tk.Entry(newwin, bd=7)
    name_entry.grid(row=1, column=1)
    email_entry = tk.Entry(newwin, bd=7)
    email_entry.grid(row=2, column=1)
    batch_entry = tk.Entry(newwin, bd=7)
    batch_entry.grid(row=3, column=1)
    mobile_entry = tk.Entry(newwin, bd=7)
    mobile_entry.grid(row=4, column=1)

    tk.Button(newwin, text="Submit", command=add_query).grid(row=5, column=1, pady=10)



def delete_student():
    def delete():
        reg_no = reg_no_entry.get()
        if not reg_no:
            messagebox.showwarning("WARNING", "Enter a Valid Registration Number")
            return
        
        if db.students.count_documents({'Registration_No': reg_no}, limit=1) == 0:
            messagebox.showwarning("ERROR", "Student with this Registration Number Does Not Exist")
            return
        else:
            db.students.delete_one({'Registration_No': reg_no})
            newwin.destroy()
            messagebox.showinfo("Delete Student", "Student Deleted")

    newwin = tk.Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Delete Student")

    tk.Label(newwin, text="Registration Number").grid(row=0, column=0)
    reg_no_entry = tk.Entry(newwin, bd=5)
    reg_no_entry.grid(row=0, column=1)

    tk.Button(newwin, text="Delete Entry", command=delete).grid(row=1, column=1, pady=10)


def update_student():
    def update():
        reg_no = reg_no_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        batch = batch_entry.get()
        mobile = mobile_entry.get()
        
        if not reg_no:
            messagebox.showwarning("WARNING", "Enter a Valid Registration Number")
            return

        if db.students.count_documents({'Registration_No': reg_no}, limit=1) == 0:
            messagebox.showwarning("ERROR", "Student with this Registration Number Does Not Exist")
            return

        update_dict = {}
        if name:
            update_dict['Name'] = name
        if email:
            update_dict['Email'] = email
        if batch:
            update_dict['Batch'] = batch
        if mobile:
            update_dict['Mobile'] = mobile
        
        if update_dict:
            db.students.update_one({'Registration_No': reg_no}, {'$set': update_dict})
            newwin.destroy()
            messagebox.showinfo("Update Student", "Student Updated")
        else:
            messagebox.showinfo("Update Student", "No changes to update")

    newwin = tk.Toplevel(root)
    newwin.geometry('400x400')
    newwin.title("Update Students")

    tk.Label(newwin, text="Registration Number").grid(row=0, column=0)
    tk.Label(newwin, text="Name").grid(row=1, column=0)
    tk.Label(newwin, text="Email").grid(row=2, column=0)
    tk.Label(newwin, text="Batch").grid(row=3, column=0)
    tk.Label(newwin, text="Mobile").grid(row=4, column=0)

    reg_no_entry = tk.Entry(newwin, bd=7)
    reg_no_entry.grid(row=0, column=1)
    name_entry = tk.Entry(newwin, bd=7)
    name_entry.grid(row=1, column=1)
    email_entry = tk.Entry(newwin, bd=7)
    email_entry.grid(row=2, column=1)
    batch_entry = tk.Entry(newwin, bd=7)
    batch_entry.grid(row=3, column=1)
    mobile_entry = tk.Entry(newwin, bd=7)
    mobile_entry.grid(row=4, column=1)

    tk.Button(newwin, text="Submit", command=update).grid(row=5, column=1, pady=10)


def display_students():
    newwin = tk.Toplevel(root)
    newwin.geometry('400x400')
    newwin.title("Student Details")

    tk.Label(newwin, text="Registration Number").grid(row=0, column=0)
    tk.Label(newwin, text="Name").grid(row=0, column=1)
    tk.Label(newwin, text="Email").grid(row=0, column=2)
    tk.Label(newwin, text="Batch").grid(row=0, column=3)
    tk.Label(newwin, text="Mobile").grid(row=0, column=4)

    i = 1
    for student in db.students.find():
        tk.Label(newwin, text=student['Registration_No']).grid(row=i, column=0)
        tk.Label(newwin, text=student['Name']).grid(row=i, column=1)
        tk.Label(newwin, text=student['Email']).grid(row=i, column=2)
        tk.Label(newwin, text=student['Batch']).grid(row=i, column=3)
        tk.Label(newwin, text=student.get('Mobile', '')).grid(row=i, column=4)
        i += 1

tk.Button(root, text='Add New Students', command=add_students).place(x=100, y=100)
tk.Button(root, text='Delete Student Entry', command=delete_student).place(x=100, y=150)
tk.Button(root, text='Update Student Info', command=update_student).place(x=100, y=200)
tk.Button(root, text='Show Student Details', command=display_students).place(x=100, y=250)

root.mainloop()


