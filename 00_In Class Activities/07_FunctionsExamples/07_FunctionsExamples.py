import math

def greet(first_name, second_name=None, third_name=None):
	if second_name == None:
		print("Hello "+first_name+"!")
	elif third_name == None:
		print("Hello "+first_name+" and "+second_name+"!")
	else:
		print("Hello "+first_name+", "+second_name+" and "+third_name+"!")

def distance(x1, y1, x2=0, y2=0): #by adding "=0", to a parameter, if no value is sent, x2/y2 = 0
	return math.sqrt((x2-x1)**2 + (y2-y1)**2) #by using "return", sending value back to where function was called

greet("Bob") #arguments/parameters
greet("Sue", "Bob")
greet("Sue", "Bob", "Jim")

print(distance(1,0, 4, 4))
d = distance(0,0,5,0)
print(d)