import re
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("ToodleDo - Sign In")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("To do list Profile webpage.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

name_entry = Entry(window,
                   font=("Cambria", 15)
                   )
name_entry.pack(side=LEFT)
name_entry.place(x=746, y=233)

username_entry = Entry(window,
                       font=("Cambria", 15)
                       )
username_entry.pack(side=LEFT)
username_entry.place(x=746, y=284)

dob_entry = Entry(window,
                  font=("Cambria", 15)
                  )
dob_entry.pack(side=LEFT)
dob_entry.place(x=746, y=334)

email_entry = Entry(window,
                    font=("Cambria", 15)
                    )
email_entry.pack(side=LEFT)
email_entry.place(x=746, y=391)

mobile_entry = Entry(window,
                     font=("Cambria", 15)
                     )
mobile_entry.pack(side=LEFT)
mobile_entry.place(x=746, y=447)


def on_button_click():
    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    name = name_entry.get().strip()
    username = username_entry.get().strip()
    dob = dob_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()

    # Check if the fields are not empty
    if not name or not username or not dob or not email or not mobile:
        messagebox.showerror("Error", "All fields are required")
        return

    # Check if the name is valid
    if not all(char.isalpha() or char.isspace() for char in name):
        messagebox.showerror("Error", "Invalid name")
        return

    # Check if the username is valid
    if not username.isalnum():
        messagebox.showerror("Error", "Invalid username")
        return

    # Check if the date of birth is valid
    def validate_dob(dob):
        try:
            dob_entry = datetime.datetime.strptime(dob, '%Y-%m-%d')
            if dob_entry > datetime.datetime.now():
                return False
            return True
        except ValueError:
            return False

        dob_valid = validate_dob(dob)
        if not dob_valid:
            messagebox.showerror("Error", "Invalid date of birth. Please enter in DD-MM-YYYY format")
            return

    # Check if the email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email")
        return

    # Check if the mobile number is valid
    if not re.match(r"\d{10}$", mobile):
        messagebox.showerror("Error", "Invalid mobile number")
        return

    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    messagebox.showinfo("Success", "Submitted Successfully")


submit_button = Button(window,
                       text="SUBMIT",
                       command=on_button_click,
                       font=("Jacques Francois", 15),
                       fg="#E7C6FF",
                       bg="#F72585",
                       activeforeground="#E7C6FF",
                       activebackground="#7209B7",
                       state=ACTIVE)
submit_button.pack(side=RIGHT)
submit_button.place(x=500, y=520)

window.mainloop()
