class bankAccount:
	def __init__(self, accntNum, balance=0, APR=0.01):
		self.accntNum = accntNum
		self.balance = balance
		self.APR = APR

	def deposit(self, depAmnt):
		self.balance += depAmnt
		# ADD TO RECEIPT

	def withdraw(self, withAmnt):
		self.balance -= withAmnt
		# ADD TO RECEIPT

	def balCheck(self):
		result = 'Balance of Account #'+str(self.accntNum)+': $'+str(self.balance)
		return result

	def balTrans(self, transAccnt, balAmnt):
		result = '-'*20
		self.balance -= balAmnt
		result += 'Balance of Account #'+str(self.accntNum)+': $'+str(self.balance)
		return result

	#def transReceipt():

nate = bankAccount(1,5000,0.1)
jimmy = bankAccount(2,50)
print(nate.balCheck())
print(jimmy.balCheck())

