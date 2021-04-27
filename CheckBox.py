from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Check Box")
root.iconbitmap("image.ico")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
#Anything can be written in on or off string input
checkButton = Checkbutton(root, text="Check this box!", variable = var, onvalue='On', offvalue="Off")
#Automatic selection on check box will be removed
checkButton.deselect()
checkButton.pack()

myButton = Button(root, text= "Show selection", command=show).pack()

mainloop()