# Author: Nate K
# Date of Creation: 10/24/2019
# Date of Last Edit: 10/24/2019
# Mandelbrot Function
# SOURCES: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 10/24/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
'''
HOMEWORK

def mandelbrot(cx,cy):
	#z[0]=x, z[1]=y
	z = [0,0]
	zCheck = 0
	passCount = 0

	while  zCheck <= 2 and passCount < 80:
		z = [(z[0]*z[0] + cx),(z[1]*z[1] + cy)]

		zCheck = z[0]*z[0] + z[1]*z[1]
		passCount += 1

	return passCount

constX = float(input("\n\n\nplease enter the x value\n>>"))
constY = float(input("\n\n\nplease enter the y value\n>>"))
iterations = mandelbrot(constX, constY)
if iterations == 80:
	print("the inputted values iterate infinitely")
else:
	print("number of iterations:", iterations)
'''


'''
CLASSREVIEW

def mandelbrot(cx, cy, zx=0, zy=0, count=0):
	zsquaredx, zsquaredy = zx**2 - zy**2, 2*zx*zy
	znewx, znewy = zsquaredz + cx, zsquaredy + cy
	count += 1

	if znewx ** 2 + znewy ** 2 >= 4 or count > maxIterations:
		return count
	return mandelbrot(cx,cy,znewx,znewy,count)

maxIterations = 3
print(mandelbrot(1,1))
print(mandelbrot(0,0))
'''

#EASIER METHOD
def mandelbrot(c, z=complex(0,0), count=0):
	z = z**2 + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,z,count)

maxIterations = 3
print(mandelbrot(complex(1,1)))
print(mandelbrot(complex(0,0)))
print(mandelbrot(complex(-2,2)))