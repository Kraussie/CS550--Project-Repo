# Author: Nate K
# Date of Creation: 01/07/2020
# Date of Last Edit: 01/08/2020
# Monty Hall Simulation
# SOURCES: 
# - https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540

# REFLECTION
'''
When I first heard the assignment, I remembered watching a video on the problem. However, I thought that the video had said that sticking with one's gut is the way to go. However, I was completely wrong. On every trial, I won the car more often when I switched after a door was revealed (~50% of the time vs ~33%). After re watching the video, I re-understood what was happening. The 2nd door is always going to be more likely to be the car than the first chosen door because of the statistics of the situation. I watched this video: 
https://www.youtube.com/watch?v=9vRUxbzJZ9Y
'''

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 01/08/2020
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
import random
#3 doors
#door #1 is the car
#door #2 and #3 are the pennies

def trial(switch=False):
	doorsList = [1,2,3]
	doorChoose = random.choice(doorsList)

	if switch == True:
		if doorChoose == 2:
			#open door 3, remove it from available list
			doorRevealed = doorsList.pop(2)
		else:
			#open door 2, remove it from available list
			doorRevealed = doorsList.pop(1)

		doorChoose = random.choice(doorsList)

	#win condition
	if doorChoose == 1:
		return True

def trialRun(switch=False):
	winCount = 0
	for i in range(100000):
		if trial(switch) == True:
			winCount += 1

	return winCount

stickWithGut = trialRun() / 100000 * 100
noTrustOfGut = trialRun(True) / 100000 * 100

result = "Didn't switch doors win %: "
result += str(stickWithGut)
result += "\nDid switch doors win %: "
result += str(noTrustOfGut)
print(result)