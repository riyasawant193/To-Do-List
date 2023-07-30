import re
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import pymysql

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

signin_window = Tk()  # instantiate an instance of a window
signin_window.geometry("1000x650")
signin_window.title("ToodleDo - Sign In")


signin_window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("To do list Sign In webpage.png"))
label = Label(signin_window, image=img)
label.pack()
label.place(x=0, y=0)


# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="todolist"
)

# Create cursor object
cursor = db.cursor()


def clear():
    username_entry.delete(0, END)
    emailid_entry.delete(0, END)
    password_entry.delete(0, END)


def validate_form():
    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    username = username_entry.get().strip()
    emailid = emailid_entry.get().strip()
    password = password_entry.get().strip()

    # Check if all fields are filled
    if not username or not emailid or not password:
        messagebox.showerror("Error", "Please fill all the fields")
        return

    # Check if the username is valid
    if not username.isalnum():
        messagebox.showerror("Error", "Invalid username")
        return

    # Check if the email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", emailid):
        messagebox.showerror("Error", "Invalid email")
        return

    # Validate password
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
        messagebox.showerror("Error",
                                 "Password must be at least 8 characters long and contain at least one uppercase "
                                 "letter, one lowercase letter and one digit ")
        return

    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    messagebox.showinfo("Success", "Account Created Successfully")
    signin_window.destroy()
    subprocess.Popen(["python", "Dashboard.py"])


def connect_database():
    if not validate_form():
        return
    # Get user input from entry fields
    username = username_entry.get()
    emailid = emailid_entry.get()
    password = password_entry.get()

    # Check if username already exists in database
    cursor.execute("SELECT * FROM login_info WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new login_info into database
        cursor.execute(
            "INSERT INTO login_info ( username, emailid, password) VALUES (%s, %s, %s)",
            (username, emailid, password))
        db.commit()
        messagebox.showinfo("Success", "Account Created Successfully")

        # Clear entry fields
        clear()

        signin_window.destroy()
        subprocess.Popen(["python", "Dashboard.py"])



def on_button_click():
    # Perform account creation logic here

    # Show a message box to indicate that the account was created successfully
    messagebox.showinfo("Success", "Account Created Successfully")
    signin_window.destroy()
    subprocess.Popen(["python", "Dashboard.py"])


button = Button(signin_window,
                text="SIGN IN",
                command=on_button_click,
                font=("Montserrat", 13),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#E7C6FF",
                activebackground="#FFFFFF",
                state=ACTIVE)
button.pack()
button.place(x=643, y=487)


def on_button_click():
    # Close the current file
    signin_window.destroy()
    # Open the new file
    subprocess.Popen(["python", "Home.py"])


button = Button(signin_window,
                text=" ← ",
                command=on_button_click,
                font=("Montserrat", 15),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#E7C6FF",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=950, y=10)

# for login id
username_entry = Entry()
username_entry.config(font=('Cambria', 15))  # change font
username_entry.config(bg='white')  # background
username_entry.config(fg='#7209B7')  # foreground
username_entry.config(width=10)  # width displayed in characters
username_entry.pack()
username_entry.place(x=643, y=296)

# for Email ID
emailid_entry = Entry()
emailid_entry.config(font=('Cambria', 15))  # change font
emailid_entry.config(bg='white')  # background
emailid_entry.config(fg='#7209B7')  # foreground
emailid_entry.config(width=10)  # width displayed in characters

emailid_entry.pack()
emailid_entry.place(x=643, y=355)

# for password
password_entry = Entry()
password_entry.config(font=('Cambria', 15))  # change font
password_entry.config(bg='white')  # background
password_entry.config(fg='#7209B7')  # foreground
password_entry.config(width=10)  # width displayed in characters
password_entry.config(show='*')  # replace characters shown with x character
password_entry.pack()
password_entry.place(x=643, y=414)

signin_window.mainloop()  # place window on computer screen, lister for events
