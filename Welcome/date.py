from calendar import FRIDAY, MONDAY, firstweekday, weekday
import calendar
import datetime  
dt = datetime.datetime.now()  
# print ("Current date and time is = %s" % dt)  
# print ("Date and time in ISO Format = %s" % dt.isoformat())  
# print ("Current year = %s" %dt.year)  
# print ("Current month is = %s" %dt.month)  
# print ("Current date (day) = %s" %dt.day )  
# print ("represent Date in dd/mm/yyyy format = %s / %s/ %s" % (dt.day, dt.month, dt.year))  
# print ("Current hour is = %s" %dt.hour)  
# print (" Current minute is = %s" %dt.minute)  
# print ("Current Second is = %s" %dt.second)  
# print ("Representation of time in hh: mm: ss format = %s: %s: %s" % (dt.hour, dt.minute, dt.second))  

# print(dt)
# print (dt.strftime ("%d / %m / %Y ")) # represents the date in DD/ MM/ YYYY  
print ("Date:" +dt.strftime (" %D")) # represents the day, month date and year  
day =dt.strftime("%a")
print("Day:" +day)
if day in ['Mon','Fri','Tue','Wen','Thur'] :
    print(" Fare:100")

if day in ['Sat']:
    print("Fare:80")

if day in ['Sun']:
    print("Fare:60")

# else:
#     print("day not found")