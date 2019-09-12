# QUESTION 3
#from datetime import date

UR_month = int(input("Please enter the # of a month:\n"))
UR_day = int(input("Please enter a day:\n"))
UR_year = int(input("Please enter a year:\n"))

#day = date(UR_year,UR_month,UR_day).weekday()

year = UR_year - ((14 - UR_month) // 12)
tempEquation = year + (year // 4) - (year // 100) + (year // 400)
month = UR_month + (12 * ((14 - UR_month) // 12)) - 2
day = ((UR_day + tempEquation + ((31 * month) // 12))) % 7

#print("\n\n\n",UR_month, UR_day, UR_year)
#print("yearCalc debug:", year)
#print("tempEquation debug:", tempEquation)
#print("monthCalc debug:", month)
#print("dayCalc1 debug:", day1)
#print("dayCalc2 debug:", day2)

if day == 0:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Sunday")
elif day == 1:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Monday")
elif day == 2:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Tuesday")
elif day == 3:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Wednesday")
elif day == 4:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Thursday")
elif day == 5:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Friday")
elif day == 6:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Saturday")