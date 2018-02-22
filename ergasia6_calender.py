import calendar
c=calendar.TextCalendar(calendar.SUNDAY)
y=int(input("Input the year: "))
x=int(input("Input the month: "))
str=c.formatmonth(y, x)
print(str)