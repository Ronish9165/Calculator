from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

def show():
    myLabel = Label(root, text=clicked.get()).pack()

#Making options into list
# options = ["Monday",
#             "Tuesday",
#            "Wednesday",
#            "Thursday",
#            "Friday"
# ]

clicked = StringVar()
clicked.set("Days")

drop = OptionMenu(root, clicked,"Monday", "Tuesday","Wednesday", "Thursday","Friday")
drop.pack()


myButton = Button(root, text= "Show Selection", command=show).pack()

mainloop()