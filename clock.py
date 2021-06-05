from tkinter import *
from tkinter.ttk import *
import datetime as dt
from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root , font=("ds-digital" , 90) , background="black" , foreground="red")
label.pack(anchor="center")

label1 = Label(root, font=("ds-digital" , 90), background='black' , foreground='red')
label1.pack(anchor='center')

def date():
    da = dt.date.today()
    label1.config(text =da)
    

time()
date()
mainloop()