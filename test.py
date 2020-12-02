# Tkinter checkbox/check-button
from tkinter import *
master = Tk()


def var_states():
    if var1.get() and var2.get():
        print("male: %d" % var1.get())
    elif var2.get():
        print("female: %d" % var2.get())


Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()
