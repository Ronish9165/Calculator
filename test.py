from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#title
root.title("Image Insertion")

#icon images
# png icons does not support sometimes
root.iconbitmap("image.ico")

my_image = ImageTk.PhotoImage(Image.open("photo.png"))
my_label = Label( image = my_image)
my_label.pack()


button_quit= Button(root, text="Exit", command=root.quit, width=20)
button_quit.pack()



root.mainloop()