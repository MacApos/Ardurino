from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


def global_var(text):
    global first_number
    global math
    first_number = int(e.get())
    math = text
    return first_number, math


def add():
    first_number, math = global_var('add')
    e.delete(0, END)


def divide():
    first_number, math = global_var('divide')
    e.delete(0, END)


def multiply():
    first_number, math = global_var('multiply')
    e.delete(0, END)


def substract():
    first_number, math = global_var('substract')
    e.delete(0, END)


def clear():
    e.delete(0, END)


def equal():
    second_number = int(e.get())
    e.delete(0, END)
    if math == 'add':
        e.insert(0, str(first_number + second_number))
    if math == 'divide':
        e.insert(0, str(first_number / second_number))
    if math == 'multiply':
        e.insert(0, str(first_number * second_number))
    if math == 'substract':
        e.insert(0, str(first_number - second_number))


button_clear = Button(root, text='C', padx=39, pady=20, command=clear)
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
button_equal = Button(root, text='=', padx=39, pady=20, command=equal)
button_add = Button(root, text='+', padx=39, pady=20, command=add)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button_divide = Button(root, text='/', padx=40, pady=20, command=divide)

button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button_multiply = Button(root, text='x', padx=40, pady=20, command=multiply)

button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button_substract = Button(root, text='–', padx=40, pady=20, command=substract)

buttons = [button_clear, button_0, button_equal, button_add, button_1, button_2, button_3, button_divide,
           button_4, button_5, button_6, button_multiply, button_7, button_8, button_9, button_substract]

row = 4
column = 0
for button in buttons:
    button.grid(row=row, column=column)
    column += 1
    if column == 4:
        row -= 1
        column = 0


root.mainloop()
