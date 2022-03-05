from tkinter import *
import random

root = Tk()
root.minsize(350, 200)


def update(pos, slider):
    if int(pos.get()) > 180:
        pos.delete(0, END)
        pos.insert(0, '180')
    pos = int(pos.get())
    slider.set(pos)


def update_all():
    slider0.set(int(pos0.get()))
    slider1.set(int(pos1.get()))
    slider2.set(int(pos2.get()))


def restart():
    pos0.delete(0, END)
    slider0.set(0)
    pos0.insert(0, '0')

    pos1.delete(0, END)
    slider1.set(0)
    pos1.insert(0, '0')

    pos2.delete(0, END)
    slider2.set(0)
    pos2.insert(0, '0')


def random_setup():
    pos0.delete(0, END)
    random0 = random.randint(0, 180)
    pos0.insert(0, str(random0))
    slider0.set(random0)

    pos1.delete(0, END)
    random1 = random.randint(0, 180)
    pos1.insert(0, str(random1))
    slider1.set(random1)

    pos2.delete(0, END)
    random2 = random.randint(0, 180)
    pos2.insert(0, str(random2))
    slider2.set(random2)




def save():
    setup = []
    for pos in pos0, pos1, pos2:
        setup.append(int(pos.get()))
    saved_pos.append(setup)
    print(saved_pos)


def clear():
    global saved_pos
    saved_pos = []
    print(saved_pos)


saved_pos = []

pos0 = Entry(root)
pos0.insert(0, "0")
update1 = Button(root, text='UPDATE', command=lambda: update(pos0, slider0))
pos0.grid(row=1, column=1, sticky='s')
update1.grid(row=1, column=2, sticky='s')

pos1 = Entry(root)
pos1.insert(0, "0")
update2 = Button(root, text='UPDATE', command=lambda: update(pos1, slider1))
pos1.grid(row=3, column=1, sticky='s', pady=3)
update2.grid(row=3, column=2, sticky='s')

pos2 = Entry(root)
pos2.insert(0, "0")
update3 = Button(root, text='UPDATE', command=lambda: update(pos2, slider2))
pos2.grid(row=5, column=1, sticky='s', pady=3)
update3.grid(row=5, column=2, sticky='s')

update_all = Button(root, text='UPDATE\nALL', command=update_all, width=7, height=5)
update_all.grid(row=1, column=3, rowspan=4, pady=19, sticky='n')

restart = Button(root, text='RESTART', command=restart, width=7)
restart.grid(row=5, column=3, sticky='s')

random_setup = Button(root, text='RANDOM', command=random_setup, width=7)
random_setup.grid(row=4, column=3, sticky='ew')

servo0 = Label(root, text='Servo1')
slider0 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
servo0.grid(row=0, column=0, sticky='ew')
slider0.grid(row=1, column=0)

servo1 = Label(root, text='Servo2')
slider1 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
servo1.grid(row=2, column=0, sticky='ew')
slider1.grid(row=3, column=0)

servo2 = Label(root, text='Servo3')
slider2 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
servo2.grid(row=4, column=0, sticky='ew')
slider2.grid(row=5, column=0)

save = Button(root, text='SAVE', command=save)
save.grid(row=6, column=0)

clear = Button(root, text='CLEAR', command=clear)
clear.grid(row=6, column=1)

root.mainloop()
