import random, math

#square of width&height 4000, radius of circle will be 2000
x = 4000
y = 4000

def randomPoints(n):
	winCount = 0
	for i in range(n):
		dx = random.randint(0, x)
		dy = random.randint(0, y)

		if math.hypot(dx, dy, 2000, 2000) <= 2000:
			winCount += 1
	return winCount