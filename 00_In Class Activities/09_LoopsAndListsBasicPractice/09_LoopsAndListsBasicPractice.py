#Loops and Lists Basic Practice
import random
import math
 
# 1. Create a list that holds the numbers 1-99 in reverse order.
'''
COMPLETE

###a = list(range(99,0,-1))
###print(a)
'''
 
# 2. Create a loop that loops through a list of random numbers (ranging from 0-100) and throws away or removes any number greater than 10. This should work for lists of any length.
'''
COMPLETE

purgeList = [random.randint(0,100) for i in range(30)]
print(purgeList)
purgedList = [i for i in purgeList if i < 10]
print(purgedList)
'''
 
# 3. Write a function that will return a list of the first n numbers in the fibonacci sequence. No recursion allowed!
'''
COMPLETE

phi = ( 1 + math.sqrt(5) ) / 2
numberFib_UR = int(input("\n\n\nHow many values of the fibonacci sequence would you like to see?\n>>"))
fibPrint = []
for i in range(numberFib_UR):
	fibPrint.append(round((((phi)**i)-((1-phi)**i)) / (math.sqrt(5))))
print(fibPrint)
'''

# 4. Write some code that, given a list, will tell you if a given value is in the list. 
'''
COMPLETE

valList = [1,4,5,6,9,10]
if int(input("Enter Number\n>>")) in valList:
	print("\nYes it is in the list!")
'''
 
# 5. Write some code that, given a list of 30 random numbers between 1 and 30, will print to the screen "Yahtzee!" if the first six multiples under 30 of any number 1-6 are all in the list. For example, 1, 2, 3, 4, 5, and 6 = yahtzee, 3, 6, 9, 12, 15 = yahtzee, etc.
'''
INCOMPLETE

ranList = [random.randint(1,30) for i in range(30)]
if X:
	print("Yahtzee!")
'''
 
 
# 6. Write a function that accepts an array of numbers, and returns the sum of the numbers in the array, except sections of numbers starting with a 6 and extending to the next 7 will be ignored in the sum (every 6 will be followed by at least one 7). Return 0 for no numbers. For example: 1, 2, 3, 6, 4, 5, 7, 7 would return 13.