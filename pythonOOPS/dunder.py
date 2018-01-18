#Python program to show use of dunder functions.
from functools import total_ordering


@total_ordering
class Account:

	#Object Initialization
	def __init__(self,owner,amount=0):

		self.owner = owner
		self.amount = amount
		self._transactions = []


	def add_transaction(self,amount):
		if not isinstance(amount,int):
			raise ValueError('Please Use int for amount')

		self._transactions.append(amount)


	



	@property
	def balance(self):
		return self.amount + sum(self._transactions)

	#Object Representation
	def __repr__(self):
		return "Account ({},{})".format(self.owner,self.amount)


	def __str__(self):
		return "Account of  {} with Starting amout: {}".format(self.owner,self.amount)


	#Item Iteration

	def __len__(self):
		return len(self._transactions)

	def __getitem__(self,position):
		return self._transactions[position]

	def __reversed__(self):
		return self[::-1]


	#Operatior Overloading

	def __eq__(self,other):
		return self.balance == other.balance

	def __lt__(self,other):
		return self.balance < other.balance

	def __add__(self,other):
		owner = '{}&{}'.format(self.owner,other.owner)
		start_amount = self.amount + other.amount
		acc = Account(owner,start_amount)
		for t in list(self) + list(other):
			acc.add_transaction(t)

		return acc


	#Callable Objects

	def __call__(self):
		print("Account Holder: {}".format(self.owner))
		print('Starting amount: {}'.format(self.amount))
		print("_transactions:")
		for transaction in self:
			print transaction

		print("\nBalance: {}".format(self.balance))


	#Context Managers

	def __enter__(self):
		print ("Enter WITH: Making Backup of transaction for rollback")
		self._copy_transactions = list(self._transactions)
		return self



	def __exit__(self,exec_type,exec_val,exec_tb):

		print('EXIT WITH: ')

		if exec_type:
			self._transactions = self._copy_transactions
			print('Rolling back to previous transactions')
			print('Transaction resulted in {} ({})'.format(exec_type.__name__,exec_val))

		else:
			print('Transaction OK')



def validate_transaction(acc,amount_to_add):
		with acc as a:
			print('Adding {} to account'.format(amount_to_add))
			a.add_transaction(amount_to_add)
			print("New balance : {}".format(a.balance))
			if a.balance < 0:
				raise ValueError('-ve Balance in your acc')




acc = Account('Faizan',10000)

print acc


acc.add_transaction(2000)
acc.add_transaction(-100)
acc.add_transaction(400)
acc.add_transaction(-2000)
acc.add_transaction(3000)



print acc.balance

print len(acc)

for t in acc:
	print t

print(list(reversed(acc)))


acc2 = Account('Muneer',10000)

acc2.add_transaction(200)
acc2.add_transaction(-3000)
acc2.add_transaction(500)
acc2.add_transaction(5000)


print (acc2 > acc)

print (acc == acc2)

grpAcc = acc + acc2

print grpAcc


grpAcc()


print "*********"
acc3 = Account("Faisal",10000)

try:
	validate_transaction(acc3,-5000)
	validate_transaction(acc3,4000)
	validate_transaction(acc3,-10000)
	validate_transaction(acc3,1000)
	validate_transaction(acc3,5000)
except ValueError as e:
	print e


acc3()