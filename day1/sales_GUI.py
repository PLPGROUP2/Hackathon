

#Using tkinter module for UI

from tkinter import *
from turtle import title

from locale import currency
import math
from webbrowser import get
root = Tk()
root.geometry("800x300")
def getvals():
    wall_sizevalue  = wall_sizeEntry.get()
    price_value_1 = price_value.get()
    size = int(115) #define varibles
    labor= float(20)
    rate = 8 #hours

    NumberofGalotas= int()
    print("No.of Paint Galots  required:" ,NumberofGalotas) 

    Paintcost = (NumberofGalotas * price_value)
    print("Paint Cost:",Paintcost)

    hours = (NumberofGalotas * rate)
    print("No.hours of labor:",hours)

    Laborcost = (hours * rate)
    print("Labor Cost:",Laborcost)

    Totalcoast=(Paintcost + Laborcost)

    print("Total Cost:",Totalcoast)
    return None

#tiltle 

root.title("Sales Tax Challenge  Task Two (Day 1)")

# header title 
Label(root, text= "Power Learn Project Hackathon Event", font="Calibri, 20",).grid(row=0, column=3)

#declaring the two variables needed
wall_size = Label(root, text="Enter the square feet")
price = Label(root, text="Price of paint /gallon")


# creating labels of the two inputs

wall_size.grid(row=1, column=2)
price.grid(row=2, column=2)

#variables for storing our data 

wall_sizevalue = float
price_value_1= float


# packing entry fields 
wall_sizeEntry = Entry(root,textvariable=wall_sizevalue, width=20)
price_value = Entry(root, textvariable=price_value_1, width=20)

# inserting grid for visibility 
wall_sizeEntry.grid(row=1, column=3)
price_value.grid(row=2, column=3)

# submit button 

Button(text="Compute ", command=getvals).grid(row=4, column=3)

#design layout size 



root.mainloop()
