import random

a = [[3,7,4],[1,1,1],[5,8,9],[2,3,7],[1,2,3,4],[1,6,4]]

'''
def niceprint(a)
	for i in a:
		print(i) #print each list item individually
		print(*i) #removes brackets and commas
'''

'''
#print each list's list item individually
for row in a:
	for col in row:
		print(col)
		#print(col+5) can manipulate values 

for row in range(len(a)):
	for col in range(len(a[row])):
		a[row][col] += 5

#print(a)
'''

b=[[random.randint(1,5) for x in range(5)] for y in range(7)]
#print(b)

# PRACTICE
#2x8 list of values btwn 0, 1
c = [[random.random() for x in range(2)] for y in range(8)]
#print(c)

#10x10 list, starting at 2 and going up by 2 incrementally
d = [[range(2,)] for y in range(10)]

count = 2;
seconda = []
for row in range(10):
	temprow = []
	for col in range(10):
		temprow.append(count)
		count+=2
	seconda.append(temprow)
print(seconda)

#OR

secondb = []
for row in range(10):
	temprow = []
	for col in range(10):
		temprow.append(col*2+row*20+2)
	secondb.append(temprow)
print(secondb)

secondc = [[x+y*20 for x in range(2, 21, 2)] for y in range(0,10)]
print(secondc)