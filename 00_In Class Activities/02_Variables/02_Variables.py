# Author: Nate K
# Date of Creation: 09/10/2019
# Date of Last Edit: 09/10/2019
# Variable Lesson

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/10/2019

import math as m #don't have to type math.XXX, can say m.XXX

ur = int(input("Give me some data!"))

#good variable names:
#user_response, hello1, cookieSypplyChain, x, y, z
#bad variable names:
#1234, 1hello, True, input (conflicts with pre-made function)
#field day (two words), PHYSICS (indicates constant), Physics (indicates class)

x = 1
y = 2
z = 3

result = x+y
print(result) # 3

result = result - z
#result -= z
print(result) # 0

result = z * y
print(result) # 6

result /= y #same thing as "result = result/y"
print(result) # 3.0, division automatically results in a float

#result++, not possible, must use "result += 1"
#print(result) #4?

result = z % y # "modulus"
print(result) #1, remainder of division, can tell if a number is evenly divisible or not

result = z ** y
print(result) #9, z to the power of y

result = z // y #floored division, takes off the decimal (i.e. rounding down)
print(result) #1

#result += ur
print(ur,result, x, y, z, "hello")

a = 9
result = a ** (1/2)
print(result)

result = m.sin(a)
print(result)