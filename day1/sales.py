from locale import currency
import math
#input varibles 
floor=int(input("enter the size of wall:"))
price=int(input("enter price of paint per garlot IN $:") )
size = int(115) #define varibles
labor= float(20)
rate = 8 #hours


NumberofGalotas= int(floor / size)
print("No.of Paint Galots  required:" ,NumberofGalotas) 

Paintcost = (NumberofGalotas * price)
print("Paint Cost:",Paintcost)

hours = (NumberofGalotas * rate)
print("No.hours of labor:",hours)

Laborcost = (hours * rate)
print("Labor Cost:",Laborcost)

Totalcoast=(Paintcost + Laborcost)

print("Total Cost:",Totalcoast)
