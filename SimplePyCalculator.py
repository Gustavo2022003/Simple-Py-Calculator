from tkinter import *

root = Tk()
root.title("Simple Py Calculator")

# OTHERS
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# FUNCTIONS

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
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    elif math == 'division':
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


# BUTTONS

botao_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
botao_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
botao_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
botao_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
botao_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
botao_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
botao_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
botao_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
botao_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
botao_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=38, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=89, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=78, pady=20, command=button_clear)

button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text='x', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_divide)

# BUTTONS ON SCREEN

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
