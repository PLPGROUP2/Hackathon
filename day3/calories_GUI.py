
from tkinter import *
from turtle import title

from locale import currency
import math
from webbrowser import get
root = Tk()
root.geometry("800x300")
root.title("Power Learning Hackathon")
#root.icpnbitmap()
root.geometry("400x200")

plp_menu = Menu(root)
root.config(menu=plp_menu)

w = Label(root, justify=LEFT, padx=10, font="Calibri, 18", text="Hackathon Day 3: Challenge Task Two (Day 3)")
w.pack()

Label(root,text="[Fat and Carbohydrates for Health Living ", font="Calibri,16", fg="green").pack()
Label(root,text="[Enter the number of fat grams", font="Calibri,12", fg="blue").pack()
fats_entry= Entry(root).pack()

Label(root,text="[Enter the number of carbohydrate grams", font="Calibri,12", fg="blue").pack()
carbo_entry= Entry(root).pack()


def compute(fats_entry):

    fats=float(fats_entry.get())
    fat_calories=(fats * 9)
    carbo_calories =(carbo_entry.get() * 4)

    total_calories= (fat_calories + carbo_calories)

    print("Fat Calories = " ,fat_calories)
    print("Carbohydrate Calories = " , carbo_calories )
    print("Total Calories = " , total_calories )

Button(root,text="Compute number of calories", command=compute).pack()

root.mainloop()