
class Test:

	def __init__(self,a,b):
		self.a = a
		self.b = b


	def __str__(self):

		return "Test a: %s b: %s "%(self.a,self.b)

	def __repr__(self):
		return "Test a: %s b: %s " % (self.a,self.b)



t = Test(1234,5678)
print t  # calls __str__ method if specified  , uses __repr__ if specified , otherwise uses default
print  [t] # calls  __repr__ method if specified , otherwise uses default


