from PIL import Image
import numpy

dimx = 1000
dimy = 1000

mPic = Image.new("RGB",(dimx,dimy))

def mandelbrot(c, z=complex(0,0), count=0):
	z = z**2 + c
	count += 1
	if abs(z) >= 2 or count > maxIterations:
		return count
	return mandelbrot(c,z,count)

def pixelPlace(mandelSave,count=0):
	for x in range(0,dimx):
		for y in range(0,dimy):
			for pixelVal in range(0,dimx*dimy):
				pixelColor = int(numpy.interp(mandelSave[pixelVal],[0,maxIterations],[0,255]))
				mPic.putpixel((x,y),(pixelColor,pixelColor,pixelColor))
				count+=1
				print(count)

maxIterations = 3
mandelSave = []

def mandelFunc():
	for x in numpy.linspace(-2,2,dimx):
		for y in numpy.linspace(-2,2,dimy):
			mandelSave.append(mandelbrot(complex(x,y)))
	pixelPlace(mandelSave)

mandelFunc()
mPic.save("demo_image.png","PNG")