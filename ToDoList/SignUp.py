import re
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import pymysql

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

signup_window = Tk()  # instantiate an instance of a window
signup_window.geometry("1000x650")
signup_window.title("ToodleDo - Sign Up")

img = ImageTk.PhotoImage(Image.open("To do list Sign Up webpage.png"))
label = Label(signup_window, image=img)
label.pack()
label.place(x=0, y=0)

fname_entry = Entry(signup_window,
                    font=("Cambria", 10)
                    )
fname_entry.pack(side=LEFT)
fname_entry.place(x=531, y=280)

lname_entry = Entry(signup_window,
                    font=("Cambria", 10)
                    )
lname_entry.pack(side=LEFT)
lname_entry.place(x=715, y=280)

uname_entry = Entry(signup_window,
                    font=("Montserrat", 10)
                    )
uname_entry.pack(side=LEFT)
uname_entry.place(x=666, y=336)

email_entry = Entry(signup_window,
                    font=("Montserrat", 10)
                    )
email_entry.pack(side=LEFT)
email_entry.place(x=666, y=400)

password_entry = Entry(signup_window,
                       show="*",
                       font=("Cambria", 10)
                       )
password_entry.pack(side=LEFT)
password_entry.place(x=526, y=498)

cpassword_entry = Entry(signup_window,
                        show="*",
                        font=("Cambria", 10)
                        )
cpassword_entry.pack(side=LEFT)
cpassword_entry.place(x=721, y=498)

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="prodigyspursuit"
)

# Create cursor object
cursor = db.cursor()


def clear():
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    uname_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    cpassword_entry.delete(0, END)


def validate_form():
    # Get user input from entry fields
    firstname = fname_entry.get().strip()
    lastname = lname_entry.get().strip()
    username = uname_entry.get().strip()
    emailid = email_entry.get().strip()
    password = password_entry.get().strip()
    cpassword = cpassword_entry.get().strip()

    # Check if all fields are filled
    if not firstname or not lastname or not username or not emailid or not password or not cpassword:
        messagebox.showerror("Error", "Please fill all the fields")
        return

        # Validate first name and last name
    if not re.match(r"^[A-Za-z ]+$", firstname) or not re.match(r"^[A-Za-z ]+$", lastname):
        messagebox.showerror("Error", "Invalid first or last name")
        return

        # Validate username (allow only alphanumeric characters and underscores)
    if not re.match(r"^\w+$", username):
        messagebox.showerror("Error", "Invalid username")
        return

        # Validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", emailid):
        messagebox.showerror("Error", "Invalid email")
        return

        # Validate password
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
        messagebox.showerror("Error",
                             "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase ""letter, and one digit ")
        return

        # Validate password
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", cpassword):
        messagebox.showerror("Error",
                             "Password must be at least 8 characters long and contain at least one uppercase "
                             "letter, one lowercase letter and one digit ")
        return

        # Check if password and confirm password match
    if password != cpassword:
        messagebox.showerror("Error", "Passwords do not match")
    return False

    return True


def connect_database():
    if not validate_form():
        return
    # Get user input from entry fields
    firstname = fname_entry.get()
    lastname = lname_entry.get()
    username = uname_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    cpassword = cpassword_entry.get()

    # Check if username already exists in database
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new info into database
        cursor.execute(
            "INSERT INTO users (firstname, lastname, username, email, password,cpassword) VALUES (%s, %s, %s, %s, %s,%s)",
            (firstname, lastname, username, email, password, cpassword))
        db.commit()
        messagebox.showinfo("Success", "Account created Successfully")

        # Clear entry fields
        clear()

        # Close sign up window and open login window
        signup_window.destroy()
        subprocess.Popen(["python", "Dashboard.py"])


signup_button = Button(signup_window,
                       text="Create Account",
                       command=connect_database,
                       font=("Montserrat Light", 12),
                       fg="#e5b3fe",
                       bg="#7b2cbf",
                       activeforeground="#e5b3fe",
                       activebackground="#7209B7",
                       state=ACTIVE)
signup_button.pack()
signup_button.place(x=700, y=550)


def on_button_click():
    # Close the current file
    signup_window.destroy()
    # Open the new file
    subprocess.Popen(["python", "HomePage.py"])


back_button = Button(signup_window,
                     text=" ← ",
                     command=on_button_click,
                     font=("Montserrat", 15),
                     fg="#E7C6FF",
                     bg="#F72585",
                     activeforeground="#E7C6FF",
                     activebackground="#7209B7",
                     state=ACTIVE)
back_button.pack()
back_button.place(x=950, y=10)

signup_window.mainloop()  # place window on computer screen, lister for events

db.close()
