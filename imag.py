from tkinter import *

root = Tk()

root.title("Images Insertion")

root.iconbitmap("image.ico")
Frame = LabelFrame(root, text ="MyFrame", padx=5, pady=5)
Frame.pack(padx=10,pady=10)

root.mainloop()