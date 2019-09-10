# Author: Nate K
# Date of Creation: 09/10/2019
# Date of Last Edit: 09/10/2019
# Basic Formulas Math Practice
# Sources: https://docs.python.org/3/library/math.html

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/10/2019

import math

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 1
# PROBLEM: The order of operations for the algorithm is incorrectly formatted. The radius isn't squared
# and thus the equation is divided by, and then multiplied by, the radius.
# SOLUTION 1: 
# force = (G * mass1 * mass2) / (radius * radius)

# SOLUTION 2:
#force = (G * mass1 * mass2) / (radius**2)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 2
theta = float(input("\n\n\ninput theta value: "))
equSolution = (math.cos(theta)**2) + (math.sin(theta)**2)
print(equSolution)
# for some values (29, 50, etc.), the equation does not equal 1.0 because float rounds after 53 binary digits, thus, making results less precise
# source: https://stackoverflow.com/questions/14909711/python-cosine-function-precision

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

# QUESTION 3
x = input("\n\nEnter the X Value:\n")
y = input("\nEnter the Y Value:\n")
print("\n\n\nX Value Entered: ", x)
print("Y Value Entered: ", y)

distOrigin = math.hypot(float(x),float(y))
print("\n\n\n(", x,",",y,") is", distOrigin,"units from the origin")