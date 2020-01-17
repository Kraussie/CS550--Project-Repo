# Author: Nate K
# Date of Creation: 01/16/2020
# Date of Last Edit: 01/16/2020
# Monte Carlo Simulation

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 01/23/2020
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
#GAS DETAILS
#average cost of gas = $2.567, sourced from https://gasprices.aaa.com/?state=CT
#average fuel efficiency of domestic passenger car = 34.6 mpg, sourced from https://www.bts.gov/content/average-fuel-efficiency-us-light-duty-vehicles

#POPULATION
#57 3rd form day students, assume 2/3 carpool and 1/3 with parent or sibling
#42 4th form day students, assume 2/3 carpool and 1/3 with parent or sibling
#69 5th form day students, assume 1/2 carpool, 1/4 with parent or sibling, and 1/4 drive themselves
#44 6th form day students, assume 2/5 carpool and 3/5 drive themselves
#sourced from Choate Directory
#######
#=212 day students
#-12 faculty students = 200

#FREQUENCY
#everyone Monday-Friday
#3/4 of day students on Saturday because of games/sports/events
#1/4 of day students on Sunday
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# SETUP
from numpy.random import choice

thirdPop, fourthPop, fifthPop, sixthPop, facPop = 57, 42, 69, 44, 12
drivePop = thirdPop+fourthPop+fifthPop+sixthPop-facPop
distList = [5,10,15,20,25,30,35]

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*


def drive(cars):
	#generates the amount of miles travelled by day students in X number of 'cars'
	distanceDraw = choice(distList, cars, p=[.15,.25,.35,.15,.06,.03,.01])
	return distanceDraw

def trialWeek(n):
	distTraveled = 0
	distanceDraw = []
	for i in range(n):
		distanceDraw.append(drive(drivePop))
		distTraveled += sum(distanceDraw)

	return distanceDraw, distTraveled

trials = 100
distanceDraw, distTraveled = trialWeek(trials)
distTraveled = distTraveled / trials

result = "\n\n\nDistance Travelled by Day Student Cars:\n>>> "
result += str(distTraveled)
result += " Miles"
print(result)

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
#CREATE DISTRBUTION GRAPH
import matplotlib.pyplot as plt
import numpy
plt.style.use('ggplot')

data, x = numpy.histogram(distanceDraw, bins=7, range=(5, 35))
print(data)
x = distList
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, data, color='brown')
plt.xlabel("Miles from Choate")
plt.ylabel("# of Cars")
plt.xticks(x_pos, x)
plt.show()

