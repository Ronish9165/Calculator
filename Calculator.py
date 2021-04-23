from _ast import Lambda
from tkinter import *

root = Tk()

# Defining the title of the project*
root.title("Simple Ca lculator")
root.resizable(0,0,)
e = Entry(root, width=35, font=("Times New roman", 18) , bg="skyblue", borderwidth=20)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtract":
        e.insert(0, f_num - int(second_number))

    if math == "multiply":
        e.insert(0, f_num * int(second_number))

    if math == "divide":
        e.insert(0, f_num / int(second_number))


def button_subract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


# Defining the buttons
button_1 = Button(root, text="1", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=("Times New Roman", 20,), padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", font=("Times New Roman", 20,), padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", font=("Times New Roman", 20,), padx=40, pady=20, command=button_subract)
button_multiply = Button(root, text="×", font=("Times New Roman", 20,), padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text="÷", font=("Times New Roman", 20,), padx=39, pady=20, command=button_divide)
button_equal = Button(root, bg="skyblue  ", font=("Times New Roman", 20,), text="=", padx=39, pady=20,
                      command=button_equal)
button_clear = Button(root, text="Clear", bg="red", font=("Times New Roman", 20, ""), padx=20, pady=20,
                      command=button_clear)

# Putting button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_add.grid(row=4, column=4)
button_subtract.grid(row=3, column=4)
button_multiply.grid(row=2, column=4)
button_divide.grid(row=1, column=4)
button_equal.grid(row=4, column=2)

root.mainloop()
