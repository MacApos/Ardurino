# Python program to trace
# variable in tkinter


from tkinter import *


root = Tk()

my_var = StringVar()

# defining the callback function (observer)
def my_callback(*args):
	print ("Traced variable {}".format(my_var.get()))
	print(type(my_var.get()))

# registering the observer
my_var.trace_add('write', my_callback)

# Label(root, textvariable = my_var).pack(padx = 5, pady = 5)
#
Entry(root, textvariable = my_var).pack(padx = 5, pady = 5)

x = ''

if x:

	y = int(x)
	print(y)

else:
	print('pusty string')
if not x==0:
	print('0')
else:
	pass

root.mainloop()

