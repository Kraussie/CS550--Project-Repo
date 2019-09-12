# Author: Nate K
# Date of Creation: 09/12/2019
# Date of Last Edit: 09/12/2019
# More Advanced Math Problems and Coding Challenges
# SOURCE: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/12/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*


# QUESTION 1
num = float(input("\n\n\n\n\n\nplease enter a number:\n"))
numRemain = abs(num % 10)
print("\n\nnumRemain debug:", numRemain)
print("Is the # within 2 of a multiple of 10:", numRemain <= 2 or numRemain >=8)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 2
val1 = float(input("\n\n\n\n\n\nplease enter the 1st number:\n"))
val2 = float(input("\nplease enter the 2nd number:\n"))
valRemain = float(val1 % val2)
print("\n\nvalRemain debug:", valRemain)
print("Do the numbers evenly divide eachother:", valRemain == 0)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 3
year_UR = int(input("\n\n\n\n\n\nplease enter a year:\n"))
yearRemain = int(year_UR % 4)
print("\n\nyearRemain debug:", yearRemain)
print("Is", year_UR,"a leap year:", yearRemain == 0)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 4
is_summer = bool(input("\n\n\n\n\n\nis it summer: (enter True or False)\n"))
temp = float(input("enter the current temperature:\n"))
print("\n\nis_summer debug:", is_summer, "\ntemp debug:", temp)
print("\nAre squirrels playing:", (is_summer == False and temp >= 60 and temp <= 90) or (is_summer == True and temp >= 60 and temp <= 100))

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 5
a = float(input("\n\n\n\n\n\nplease enter value Alpha:\n"))
b = float(input("please enter value Bravo:\n"))
c = float(input("please enter value Charlie:\n"))
isSmall = (a/b)