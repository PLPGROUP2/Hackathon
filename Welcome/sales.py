from locale import currency
import math
floor=int(input("enter the size of wall:"))
price=int(input("enter price of paint per garlot:") )
size = int(115)
labor= float(20)
rate = 8 #hours


NumberofGalotas= int(floor / size)
print("No.of Paint required:" ,NumberofGalotas)

Paintcost = (NumberofGalotas * price)
print("Paint Cost:",Paintcost)

hours = (NumberofGalotas * rate)
print("No.hours of labor:",hours)

Laborcost = (hours * rate)
print("Labor Cost:",Laborcost)

Totalcoast=(Paintcost +Laborcost)

print("Total Cost:",Totalcoast)
