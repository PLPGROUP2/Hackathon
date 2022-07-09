from curses import echo
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
root.geometry("800x500")


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


# Day 2 Challenge 

w = tk.Label(root, justify=tk.LEFT, padx=10, font="Calibri, 18", text="Hackathon Day 1: Sales Tax Challenge")
w.pack()

message_1 = tk. Label(root, text="[Painting Company -- Marangi Limited", font="Calibri,18", fg="blue")
message_1.pack()

square_feet = float()
gallons_entry = float()
hours_required_entry = float()
cost_paint_entry = float()
labour_charges = float()

#enter the square feets  
square_feet_label = Label(root,text="Enter the square feets required") 
square_feet_label.pack()
square_feet = tk.Entry()
square_feet.pack()

#Gallons required 

gallons_label = tk.Label(root,text="Number of gallons of paint required")
gallons_label.pack()
gallons_entry = tk.Entry(root)
gallons_entry.pack()

# hours required 

hours_required = tk.Label(root,text=" The hours of labor required ")
hours_required.pack()
hours_required_entry = tk.Entry(root)
hours_required_entry.pack()


#cost of the paint 

cost_paint = tk.Label(root,text="The cost of the paint per gallon in Ksh")
cost_paint.pack()
cost_paint_entry = tk.Entry(root)
cost_paint_entry.pack()

# Labour charges 

labour_charges = tk.Label(root,text="labour charges per hour")
labour_charges.pack()
labour_charges_entry = tk.Entry(root)
labour_charges_entry.pack()

#calculation of the total cost 
