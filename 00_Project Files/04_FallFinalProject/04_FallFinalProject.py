# Author: Nate K
# Date of Creation: 11/07/2019
# Date of Last Edit: 11/16/2019
# Fall Final Project
# SOURCES/USEFUL LINKS:
# https://nyu-cds.github.io/python-performance-tips/03-builtin/

''' CONCLUSIONS FROM TESTING
The time to run the custom complex class was a lot longer than the built-in complex class. For the first image, it was 8x slower. For the second, 5.5x slower. For the third, 10x slower. After re-executing this program a few times, these results were the same throughout the tests. 

Because Python's inbuilt functions are programmed using C, they will execute much faster than user-defined classes. C is a much faster programming language than Python. This was concluded using the NYU github referenced linked above. The difference in speeds between images is also likely because of the varying complexities of the calculations. The third image has much more calculations than the second, and is thus less efficient.
'''

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 11/20/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM SETUP
from PIL import Image
from progressbar import progressbar as bar
import os, time, math

images = []

os.system('clear')
print("FRACTAL IMAGE RENDERING:")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# PROGRAM FUNCTIONS

class newComplex:
	#initialization of class arguments, re = x, im = y * i
	def __init__(self, re, im):
		self.re = re
		self.im = im

	#custom addition/subtraction function, sourced from:
	#https://www2.clarku.edu/faculty/djoyce/complex/plane.html
	def __add__(self, other):
		#adds the real parts and the imaginary parts (separately) of each complex number
		return newComplex(self.re + other.re, self.im + other.im)

	#custom multiplication function, equation sourced from:
	#https://www2.clarku.edu/faculty/djoyce/complex/mult.html
	def __mul__(self, other):
		# multiples real/imaginary parts following the equation linked above. 
		mulRE1 = self.re * other.re
		mulRE2 = self.im * other.im
		mulIM1 = self.re * other.im
		mulIM2 = self.im * other.re
		return newComplex(mulRE1 - mulRE2, mulIM1 + mulIM2)

	#custom power function, will multiply itself as many times as specificied by the other variable
	def __pow__(self, other):
		for powerReps in range(other):
			newSelf = self.__mul__(self)
		return newSelf

	#custom absolute value function, equation sourced from:
	# https://www2.clarku.edu/faculty/djoyce/complex/abs.html
	def __abs__(self):
		# calculates the dist of the hypot of the real/imaginary parts using the equation linked above
		return math.hypot(self.re, self.im)

	#custom string representation
	def __str__(self):
		result = str(self.re)
		result += " + "
		result += str(self.im)
		result += "i"
		return result

def mandelbrotNew(c, power=2, z=newComplex(0,0), count=0):
	z = z**power + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,power,z,count)

def mandelbrot(c, power=2, z=complex(0,0), count=0):
	z = z**power + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,power,z,count)

def timeCalc(startTime, endTime, imageDesc):
	#calculates total time elapsed
	totalTime = endTime - startTime
	#translate total time into minutes and seconds
	totalTimeMin = int(totalTime//60)
	totalTimeSec = totalTime%60
	print("IMAGE", imageDesc, "RUN-TIME:", totalTimeMin, "Minutes and", totalTimeSec, "Seconds")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 1 RUN [custom complex]
# saves the start time of the program
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1151953125
xmax = -0.0962109375
ymin = -0.935302734375
ymax = -0.916318359375

image1 =  Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 1 [custom complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = newComplex(cx,cy)
		fractResult = mandelbrotNew(c)

		r = (((fractResult+1)//6)**2)
		g = 0
		b = (fractResult*50)%256
		image1.putpixel((x,y),(r,g,b))

#saves the end time of the program and calculates time to run
endTime = time.time()
timeCalc(startTime, endTime, "1 [custom complex]")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 1 RUN [built-in complex]
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1151953125
xmax = -0.0962109375
ymin = -0.935302734375
ymax = -0.916318359375

image1 =  Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 1 [built-in complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		fractResult = mandelbrot(c)

		r = (((fractResult+1)//6)**2)
		g = 0
		b = (fractResult*50)%256
		image1.putpixel((x,y),(r,g,b))

endTime = time.time()
timeCalc(startTime, endTime, "1 [built-in complex]")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 2 RUN [custom complex]
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1594882621765136
xmax = -0.1537981567382812
ymin = -1.1101653785705567
ymax = -1.1158554840087893

image2 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 2 [custom complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = newComplex(cx,cy)
		fractResult = mandelbrotNew(c)

		if fractResult > 14:
			r = int((fractResult**2)/2)
			g = int((fractResult**2)/2) 
			b = 0
		elif fractResult > 9:
			r = int((fractResult**3)/20)
			g = int((fractResult**3)/20)
			b = int((fractResult**2.1)/2.5)
		elif fractResult > 7:
			r = 0
			g = 0
			b = 0
		else:
			r = 0
			g = fractResult*15
			b = 0
		image2.putpixel((x,y),(r,g,b))

endTime = time.time()
timeCalc(startTime, endTime, "2 [custom complex]")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 2 RUN [built-in complex]
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -0.1594882621765136
xmax = -0.1537981567382812
ymin = -1.1101653785705567
ymax = -1.1158554840087893

image2 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 2 [built-in complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		fractResult = mandelbrot(c)

		if fractResult > 14:
			r = int((fractResult**2)/2)
			g = int((fractResult**2)/2) 
			b = 0
		elif fractResult > 9:
			r = int((fractResult**3)/20)
			g = int((fractResult**3)/20)
			b = int((fractResult**2.1)/2.5)
		elif fractResult > 7:
			r = 0
			g = 0
			b = 0
		else:
			r = 0
			g = mandelbrot(c)*15
			b = 0
		image2.putpixel((x,y),(r,g,b))

endTime = time.time()
timeCalc(startTime, endTime, "2 [built-in complex]")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 3 RUN [custom complex]
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -1
xmax = 1
ymin = -1
ymax = 1

image3 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 3 [custom complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = newComplex(cx,cy)
		fractResult = mandelbrotNew(c, 5)
		r = int(((int(fractResult**2.25))%256)*1.25)
		g = int(((int(fractResult**2.25))%256)*0.6) #*0.6 creates the orange in combination with the red
		b = 0

		image3.putpixel((x,y),(r,g,b))

endTime = time.time()
timeCalc(startTime, endTime, "3 [custom complex]")

# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
# IMAGE 3 RUN [built-in complex]
startTime = time.time()

maxIterations = 255
imgx,imgy = 1000,1000
xmin = -1
xmax = 1
ymin = -1
ymax = 1

image3 = Image.new("RGB",(imgx,imgy))

print("\n\n\nIMAGE 3 [built-in complex] PROGRESS:")
for y in bar(range(imgy)):
	cy = ((ymax-ymin)/imgy)*y + ymin
	for x in range(imgx):
		cx = ((xmax-xmin)/imgx)*x + xmin
		c = complex(cx,cy)
		fractResult = mandelbrot(c, 5)
		r = int(((int(fractResult**2.25))%256)*1.25)
		g = int(((int(fractResult**2.25))%256)*0.6) #*0.6 creates the orange in combination with the red
		b = 0

		image3.putpixel((x,y),(r,g,b))

endTime = time.time()
timeCalc(startTime, endTime, "3 [built-in complex]")