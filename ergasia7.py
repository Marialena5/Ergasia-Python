import datetime

def MyDate(dt):
    return "%02d/%02d/%4d" % (dt.day, dt.month, dt.year)
	
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dates=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']


today=datetime.date.today() #Current date
year=today.year             #Current year
month=today.month           #Current month
day=today.day               #Current day
weekday=today.weekday()

List_of_dates=[]

for m in range(month+1, 13):

    try:
        Next_date=datetime.date(year, m, day)
        if Next_date.weekday==weekday:
            List_of_dates.append(Next_date)
    except:
        continue    
    
for y in range(year, year+11):        #For the next 10 years (with the current year)
    for m in range(1,13):
        try:
            Next_date=datetime.date(y, m, day)
            if Next_date.weekday()==weekday:
                List_of_dates.append(Next_date)
        except:
            continue

#Show the answer
print("")   
print("Current date: " + MyDate(today) + "\n" + "Day of week: " + days[weekday])
print("The number of all days, for the next 10 year (and the 2018), with:"+ "\n" + "Day of the month(number)= " + dates[day]  + " and" + "\n" +"Day of week= "+ days[weekday]+ ", is :" ) 
print(len(List_of_dates))

