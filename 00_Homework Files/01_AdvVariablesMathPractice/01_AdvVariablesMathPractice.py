# Author: Nate K
# Date of Creation: 09/10/2019
# Date of Last Edit: 09/10/2019
# More Advanced Math Problems and Coding Challenges
# SOURCE: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/10/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

import math

# QUESTION 1
actTemp = float(input("\n\n\nWhat is the current temperature:\n"))
windVelocity = float(input("\n\n\nWhat is the current wind speed:\n"))

if abs(actTemp) > 50 or windVelocity > 120 or windVelocity < 3:
	print("\n\n\nERRROR: One of the inputted values is not valid for this equation\n (if the temperature is larger than 50 in absolute value or if the wind velocity is larger than 120 or less than 3")
else:
	eTemp = 35.74 + (0.6215*actTemp) + (((0.4275*actTemp) - 35.75)*(windVelocity**0.16))
	print("\n\n\nThe Wind Chill Temperature is around", int(eTemp), "°F\n")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 2
x = float(input("\n\n\nEnter x value:\n"))
y = float(input("Enter y value:\n"))
z = float(input("Enter z value:\n"))
if x > y and y > z:
	print("\n\n\nTrue\n\n\n")
elif z > y and y > x:
	print("\n\n\nTrue\n\n\n")
else:
	print("\n\n\nFalse\n\n\n")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 3
from datetime import date

UR_month = int(input("Please enter the # of a month:\n"))
UR_day = int(input("Please enter a day:\n"))
UR_year = int(input("Please enter a year:\n"))

day = date(UR_year,UR_month,UR_day).weekday()

#year = round(UR_year - ((14 - UR_month) / 12))
#tempEquation = year + (year / 4) - (year / 100) + (year / 400)
#month = UR_month + (12 * ((14 - UR_month) / 12)) - 2
#day = (UR_day + tempEquation + ((31 * UR_month) / 12)) % 7
# EQUATION WASN'T WORKING FOR ME, CHOSE TO USE A LIBRARY

print("\n\n\n",UR_month, UR_day, UR_year, day)

if day == 6:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Sunday")
elif day == 0:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Monday")
elif day == 1:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Tuesday")
elif day == 2:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Wednesday")
elif day == 3:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Thursday")
elif day == 4:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Friday")
elif day == 5:
	print(UR_month, "/", UR_day, "/", UR_year, "was a Saturday")