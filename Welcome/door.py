
import datetime
import argparse
from random import choice
from selectors import EpollSelector
from xml.dom.expatbuilder import ElementInfo
dt = datetime.datetime.now()  

password = "mulika"
userpass = str(input("enter password:"))
while password == userpass:
    print("choices 1 TO OPEN")
    print("choice 2 to close ")
    print("choice 3 to QUit")
    choice = int(input("ENter choicelse:"))
if (choice == 1):
    print("door open",("Date:" +dt.strftime (" %D")))
elif choice == 2:
    print("door locked")
elif choice == 3:
    print("Quit")

else:
    print("Wrong Password enter again")

print ("Date:" +dt.strftime (" %D"))