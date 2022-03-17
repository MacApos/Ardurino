from tkinter import *

global magnet
magnet=0


def switch():
    global magnet
    if not magnet:
        magnet = 1
    else:
        magnet = 0

root = Tk()

switch = Button(root, text='switch',command=switch)
switch.grid(row=0, column=0, sticky='ew')

while True:
    print(magnet)
    root.update()