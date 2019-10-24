# Author: Nate K
# Date of Creation: 10/24/2019
# Date of Last Edit: 10/24/2019
# Mandelbrot Function
# SOURCES: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 10/24/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

def mandelbrot(cx,cy):
	z = [0,0]
	zCheck = 0
	passCount = 0
	while  zCheck <= 2 and passCount < 4:
		z = [(z[0]*z[0] + cx),(z[1]*z[1] + cy)]

		zCheck = z[0]*z[0] + z[1]*z[1]
		passCount += 1

	return passCount

constX = float(input("\n\n\nplease enter the x value\n>>"))
constY = float(input("\n\n\nplease enter the y value\n>>"))

print(mandelbrot(constX, constY))