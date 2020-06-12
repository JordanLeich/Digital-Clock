# Made by Jordan Leich on 5/31/2020

import time
from tkinter import *

root = Tk()
root.title("Digital Clock")
root.geometry("250x100+0+0")
root.resizable(0, 0)
root.configure(bg="red")

label = Label(root, font=("Arial", 45, 'bold'))
label.grid(row=0, column=1)


def clock():
    label.configure(bg="red")
    label.configure(fg='gray')
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, clock)


clock()
root.mainloop()
