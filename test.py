from tkinter import *
master = Tk()

var_string = StringVar()


def getThrottle(event):
    var_string = str(Throttle.get())
    entry.delete(0, END)
    entry.insert(0, var_string)


entry = Entry(master)
Throttle = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=getThrottle)
slider0 = Scale(master, from_=0, to=360, orient=HORIZONTAL, length=100)
Throttle.set(0)
entry.pack()
Throttle.pack()

master.mainloop()