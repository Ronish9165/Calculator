from tkinter import *

root = Tk()

#Vertical Slider
vertical = Scale(root, from_=0, to=400)
vertical.pack()

#Horizontal Slder
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

#my_label = Label(root, text=horizontal.get()).pack()

#Function Slide created
def slide():
    my_Label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#Function called
my_btn = Button(root, text="Click Me", command=slide).pack()


mainloop()
