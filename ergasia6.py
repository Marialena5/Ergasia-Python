import datetime

x=int(input("Enter the year: "))
z=int(input("Enter the month: "))

#List with the number of days of each month 
calender=[range(1, 32),range(1, 29),range(1, 32),range(1, 31),range(1, 32),range(1, 31),range(1, 32),range(1, 32),range(1, 31),range(1, 32),range(1, 31),range(1, 32)]     

months=['January','February','March','April','May','June','July','August','September','October','November','December']
                        
print('{0} {1}'.format(months[z], x).center(20, ' '))     #Print month and year

weekdays=['Su','Mo','Tu','We','Th','Fr','Sa']

for day in weekdays:    #We print days,from weekdays list,in the same line
	print day,

print('\n')

def leap_year(calender, x):   #We check whether a given year is a leap year
	if (x % 4)==0:
		if (x % 100)==0:
			if (x % 400)==0:
				calender[1]=(range(1, 30))
				for leap in calender[1]:
					print leap,
			else:
				for leap in calender[1]:
					print leap,
		else:
			calender[1]=(range(1, 30))
			for leap in calender[1]:
				print leap,
	else:
		for leap in calender[1]:
			print leap,

if z==1:
	print(leap_year(calender, x))
else:
	for leap in calender[z]:
		print leap,

		
print('\n')
print("The starting month number in calendar is : 0")