# Author: Nate K
# Date of Creation: 01/09/2020
# Date of Last Edit: 01/09/2020
# Monte Carlo Simulation
# SOURCES: 
# REFLECTION:
# 22 walks is the best average

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 01/08/2020
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
import random, math
# home at 0,0

def changeDirect(x,y):
	chooseDirec = random.randint(1,4) #1 = north, 2 = east, 3 = south, 4 = west
	if chooseDirec == 1:
		y += 1
	elif chooseDirec == 2:
		x += 1
	elif chooseDirec == 3:
		y -= 1
	elif chooseDirec == 4:
		x -= 1
	return (x,y)

def trial(n):
	# n = number of walks
	x = 0
	y = 0
	for i in range(n):
		x,y = changeDirect(x,y)

	return math.hypot(x,y)

def runTrials(n, walkDist):
	winCount = 0
	for i in range(n):
		if trial(walkDist) <= 4:
			winCount += 1

	return winCount

trials = 10000
result = "\n\n\nWin condition satisfied when less than 4 blocks from home!"

for i in range(31):
	result += "\n"
	result += str(i)
	result += " walks: "
	result += str(runTrials(trials,i) / trials * 100)
	result += "%"
print(result)
