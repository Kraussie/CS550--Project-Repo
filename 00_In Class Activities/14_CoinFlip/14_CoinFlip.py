import random

def yahtzeePlay(n):
	yahtzeeCount = 0
	for i in range(n):
		d1 = random.randint(0,6)
		d2 = random.randint(0,6)
		d3 = random.randint(0,6)
		d4 = random.randint(0,6)
		d5 = random.randint(0,6)
		if d1 == d2 == d3 == d4 == d5:
			yahtzeeCount += 1
	print(yahtzeeCount)
	return yahtzeeCount

numtrials = 1000
totals = [0 for i in range(numtrials+1)]
for i in range(100):
	result = yahtzeePlay(numtrials)
	print(result)
	totals[result] += 1
	print(str(result/numtrials*100)+"% yahtzee")

# 5 dice, yahtzee = 5 dice all same face up







'''
import random

totalFlips = 50
repeat = totalFlips
head = 0
tail = 0
count = 0

while repeat > 0:
	coin = random.randint(0,1)
	if coin == 0:
		head += 1
	elif coin == 1:
		tail += 1

	count += 1
	repeat -= 1

	result = str(round(head/count*100,4))
	result += '%'
	result += ' heads'
	print(result)

print("\n\n\nThere were", head, "heads (i.e. around", head/totalFlips*100,"% of coin flips)")
print("\nThere were", tail, "tails (i.e. around", tail/totalFlips*100,"% of coin flips)\n\n\n")
'''