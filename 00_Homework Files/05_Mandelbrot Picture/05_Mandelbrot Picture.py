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

def pixelPlace(mandelSave,x,y):
	pixelTransX, pixelTransY = int(numpy.interp(x,[-2,2],[0,1000])), int(numpy.interp(y,[-2,2],[0,1000]))
	pixelColor = int(numpy.interp(mandelSave,[0,maxIterations],[0,255]))
	print(pixelColor,pixelTransX,pixelTransY)
	try:
		mPic.putpixel((pixelTransX,pixelTransY),(pixelColor,pixelColor,pixelColor))
	except IndexError:
		print("oopsie")

def mandelFunc(count=0):
	for x in numpy.linspace(-2,2,dimx):
		for y in numpy.linspace(-2,2,dimy):
			pixelPlace(mandelbrot(complex(x,y)),x,y)
			count += 1
			print(count, x, y)


maxIterations = 100

mandelFunc()
mPic.save("demo_image.png","PNG")