from tkinter import *

# root window
root = Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


# username
username_label = Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

username_entry = Entry(root)
username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password
password_label = Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

password_entry = Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# login button
login_button = Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)


root.mainloop()