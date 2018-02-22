import datetime
from datetime import datetime
monday=0
y=int(input("Input the year: "))
x=int(input("Input the month: "))
months=range(1,13)
for year in range(y, (y+10)):    #For years
    for x in months:             #For months
        if datetime(year, x, 8).weekday() == 0:
            monday += 1	
print(monday)