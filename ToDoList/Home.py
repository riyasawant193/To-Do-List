from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

# widget =GUI elements: button, textbox,labels, images
# windows= serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("ToodleDo - Sign In")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("To do list Home webpage.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

task = StringVar()
task_entry = Entry(window,
                   font=("Cambria", 15)
                   )
task_entry.pack(side=LEFT)
task_entry.place(x=612, y=185)
task_entry.focus()

task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "/n")

        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open("task.png", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close()


# listbox
frame1 = Frame(window, bd=3, width=295, height=295, bg="#32405b")
frame1.pack(pady=(160, 0))
frame1.place(x=623, y=242)

listbox = Listbox(frame1, font=('arial', 12), width=28, height=15, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

submit_button = Button(window,
                       text="ADD",
                       command=addTask,
                       font=("Jacques Francois", 10),
                       fg="#E7C6FF",
                       bg="#F72585",
                       activeforeground="#E7C6FF",
                       activebackground="#7209B7",
                       state=ACTIVE)
submit_button.pack(side=RIGHT)
submit_button.place(x=842, y=186)

Delete_icon = PhotoImage(file="delete.png")
button = Button(window, image=Delete_icon, command=deleteTask)
button.pack(side=BOTTOM, pady=13)
button.place_configure(x=735, y=540)


window.mainloop()
