from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
from time import strftime


win = Tk()
win.iconbitmap("123.ico")
win.title("Часы)")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(win, font =("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')

time()

win.mainloop()
