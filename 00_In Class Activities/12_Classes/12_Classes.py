class Dog:
	# constructor/init method
	# creates and initalizes class variables/properties
	def __init__(self, name='Fido', age = 5, energy = 5, hunger = 5, intelligence = 5):
		self.age = age
		self.name = name
		self.energy = energy
		self.hunger = hunger
		self.intelligence = intelligence

	def sleep(self):
		self.energy += 1
		if self.energy > 10:
			self.energy = 10
			return self.name+" refuses to sleep any longer"
		else:
			return self.name+" is taking a nice nap"

	def stats(self):
		# don't want to print things in classes
		result = '-'*20
		result += '\nName: '+self.name
		result += '\nAge: '+str(self.age)
		result += '\nEnergy: '+str(self.energy)
		result += '\nHunger: '+str(self.hunger)
		result += '\nIntelligence: '+str(self.intelligence)+'\n'
		result += '-'*20
		return result

	def learn(self):
		self.intelligence += 1
		if self.intelligence > 10:
			self.intelligence = 10
			return self.name+" has learned enough"
		else:
			return self.name+" is reading a book!"

d1 = Dog()
d2 = Dog('Abigail')
d3 = Dog('River', 1, 6, 5, 7)

d1.sleep()
d3.sleep()
print(d1.stats())
print(d2.stats())
print(d3.learn())
print(d3.learn())
print(d3.learn())
print(d3.learn())
print(d3.learn())
print(d3.learn())
print(d3.stats())