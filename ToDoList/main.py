from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import subprocess

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets


root = tk.Tk()
root.geometry("1000x650")
root.title("ToodleDo")

img = ImageTk.PhotoImage(Image.open("To do list webpage.png"))
label = Label(root, image=img)
label.pack()
label.place(x=0, y=0)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "SignUp.py"])


button = Button(root,
                text="Get Started",
                command=on_button_click,
                font=("Norwester", 13),
                fg="#E7C6FF",
                bg="#4e4ed7",
                activeforeground="#E7C6FF",
                activebackground="#4e4ed7",
                state=ACTIVE)
button.pack()
button.place(x=65, y=380)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "ContactUs.py"])


button3 = Button(root,
                 text="CONTACT US",
                 command=on_button_click,
                 font=("Norwester", 12),
                 fg="#3A0CA3",
                 bg="#FFFFFF",
                 activeforeground="#3A0CA3",
                 activebackground="#FFFFFF",
                 state=ACTIVE)
button3.pack()
button3.place(x=763, y=54)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "About.py"])


button4 = Button(root,
                 text="ABOUT",
                 command=on_button_click,
                 font=("Norwester", 12),
                 fg="#3A0CA3",
                 bg="#FFFFFF",
                 activeforeground="#3A0CA3",
                 activebackground="#FFFFFF",
                 state=ACTIVE)
button4.pack()
button4.place(x=869, y=54)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "SignIn.py"])


button5 = Button(root,
                 text="SIGN IN",
                 command=on_button_click,
                 font=("Norwester", 12),
                 fg="#3A0CA3",
                 bg="#FFFFFF",
                 activeforeground="#3A0CA3",
                 activebackground="#FFFFFF",
                 state=ACTIVE)
button5.pack()
button5.place(x=661, y=54)

count = 0


def click():
    print("You clicked the button")


button6 = Button(root,
                 text="HOME",
                 command=click,
                 font=("Norwester", 12),
                 fg="#3A0CA3",
                 bg="#FFFFFF",
                 activeforeground="#3A0CA3",
                 activebackground="#FFFFFF",
                 state=ACTIVE)
button6.pack()
button6.place(x=562, y=54)

root.mainloop()  # place window on computer screen, lister for events
