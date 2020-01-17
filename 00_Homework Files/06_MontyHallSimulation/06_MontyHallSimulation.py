import random
# 3 doors with 2 pennies and 1 car
# pennie = 1
# car = 2

box1 = 0
box2 = 0
box3 = 0

carWin = 0

def boxSet(box1, box2, box3):
	box1 = random.randint(1,2)
	if box1 == 2:
		box2 = 1
		box3 = 1
	else:
		box2 = random.randint(1,2)
		if box2 == 2:
			box3 = 1
		else:
			box3 = 2

def boxRound1(contRound2):
	autoSelect = random.randint(1,3)
	if autoSelect == 1:
		if box1 == 2:
			carWin += 1
	elif autoSelect == 2:
		if box2 == 2:
			carWin += 1
	elif autoSelect == 3:
		if box3 == 2:
			carWin +=1

	if contRound2 == 1:
		boxRound2(autoSelect)

def boxRound2(autoSelect):
	if autoSelect == 1:
		if box1 != 2:
			carWin += 1
	elif autoSelect == 2:
		if box2 != 2:
			carWin += 1
	elif autoSelect == 3:
		if box3 != 2:
			carWin +=1

def trial(n,contRound2):
	for i in range(n):
		boxRound1(contRound2)

trialNum = 500
result1 = trial(trialNum,0)
print(result1)

result2 = trial(trialNum,1)
print(result2)
