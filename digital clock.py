from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

dark_pink = "#B92162"

def time ():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("digital-dream",80), background="pink", foreground= dark_pink)
label.pack(anchor='center')
time()

mainloop()