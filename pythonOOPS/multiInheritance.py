#Example on Multiple inheritance:


class Base1(object):

	def __init__(self):
		self.str1 = "Hello from Base1"
		print "Base1"

class Base2(object):

	def __init__(self):
		self.str1 = "Hello from Base 2"
		print "Base2"

	def printStr(self):
		print "Print from Base2"

class Derived(Base1,Base2):

	def __init__(self):

		#Calling base class Constructors
		Base1.__init__(self)
		Base2.__init__(self)
		self.str = "I am derived"
		print "Derived"


	def printStr(self):
		print(self.str1,self.str1,self.str)



ob = Derived()
ob.printStr()

