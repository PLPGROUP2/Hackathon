

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

w = Label(root, justify=LEFT, padx=10, font="Calibri, 18", text="Hackathon Day 2: Personality test program")
w.pack()
def books(books_purchased):
    if books_purchased<1:
        print("Sorry You have not earned any points")

    #if number of books are 1
    elif books_purchased<=1:
        print("Good You have earned 6 points")

    #if number of books are 2
    elif books_purchased<=2:
        print("Very Good You have earned 16 points")

    #if number of books are 3
    elif books_purchased<=3:
        print("Great You have earned 32 points")

    #if number of books greater than or equals 4
    else:
        print("Wow! You have earned 60 points")
    return  books_purchased
#ask for number of books purchased

Label(root,text="[Book Club Points Serendipity Booksellers", font="Calibri,16", fg="green").pack()

books_purchased =  int ()
b_purchased= Entry(root).pack()

Button(root,text="Compute rewards", command=books).pack()

#if number of books are zero



root.mainloop()