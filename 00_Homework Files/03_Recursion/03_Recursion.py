# Author: Nate K
# Date of Creation: 10/14/2019
# Date of Last Edit: 10/14/2019
# GCD Recusion
# SOURCES: 
# - https://introcs.cs.princeton.edu/python/23recursion/

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 10/14/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
import os

def gcd(num1, num2):
	if num2 == 0:
		return num1
	return gcd(num2, num1 % num2)

os.system('clear')
GCD_UR = input("Enter two numbers you want to find the GCD of (separated with a space)\n>> ").split(" ")
print("\n\n\nThe GCD of",GCD_UR[0],"and",GCD_UR[1],"is:",gcd(int(GCD_UR[0]),int(GCD_UR[1])))