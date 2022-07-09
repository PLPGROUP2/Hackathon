#from curses import echo
from cProfile import label
from cgitb import text
from re import M
from tkinter import *
import datetime as dt
import datetime
import tkinter as tk
import math
from webbrowser import get

from pip import main

root = Tk()
root.title("Power Learning Hackathon")
#root.icpnbitmap()
root.geometry("400x200")


plp_menu = Menu(root)
root.config(menu=plp_menu)

#create the menu item here

#creating label to display the them of the date 
#w = tk.Label(root, text="Hackathon Day 1")
w = tk.Label(root, justify=tk.LEFT, padx=10, font="Calibri, 18", text="Hackathon Day 1: Bus Fare Challenge")
w.pack()

# display the date 


datetime = datetime.datetime.now()
year = datetime.strftime("%Y")
month = datetime.strftime("%m")
day = datetime.strftime("%d")
date = "{}-{}-{}".format(year, month, day)

day = datetime.strftime("%a")

if day == "Mon" or day =="Tue" or day == "Wed" or day == "Thu" or day == "Fri":
    fare = "Ksh 100.00"
elif day == "Sat":
    fare = "Ksh 60.00"
else:
    fare = "Ksh 80.00"

# Labels for output on the screen 

date_1 = tk. Label(root, text="Date"+date, font="Calibri,16", fg="green")
date_1.pack()
date_2 = tk. Label(root,text="Day: "+day, font="Calibri, 16", fg="red")
date_2.pack()

date_3 = tk. Label(root, text="Fare: "+fare, font="Calibri, 20", fg="red")
date_3.pack()

file_menu = Menu(plp_menu)
plp_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Exit",command=root.quit)

root.mainloop()