
class MyClass:

	__hiddenVariable = 0

	def add(self,increment):
		self.__hiddenVariable += increment
		print self.__hiddenVariable


myObject = MyClass()
myObject.add(2)
myObject.add(5)


#print myObject.__hiddenVariable  # Not directly accessible

#Accessing hidden values

print myObject._MyClass__hiddenVariable