#bound unbound methods

class Methods:

	def __init__(self):
		self.name = 'Methods'


	def getName(self):
		return self.name



m= Methods()

#Bound
print m.getName()


#UnBound
print Methods.getName(m)