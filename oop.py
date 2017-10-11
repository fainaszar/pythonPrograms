
class cars(object):
	model=""
	make=""
	def __init__(self,model,make):

		self.model = model
		self.make = make


	def getCar(self):
		print "%r %r" % (self.make,self.model)

	def Show(self):
		print "Show of Parent"



car1 = cars("i10","Hyundai")
car1.getCar()

car2 = cars("Swift", "Maruti Suzuki")
car2.getCar()


class SUV(cars):

	def __init__(self,model,make):
		self.name =model
		super(SUV,self).__init__(model,make)


	def getName(self):
		print self.name

	def Show(self):
		#super(SUV,self).Show() #redirect overridden funciton to base class function
		print "Show of Child"


suv = SUV("Tegor","Tata")
suv.getCar()
suv.getName()

suv.Show() #function overriding



#Composition

class First(object):

	

	def __init__(self):
		self.name="First"

	def display(self):
		print self.name
		

class Second(object):

	__hits = 0 #hidden_attribute

	def __init__(self):
		self.ref = First()
		self.name = "Second"

	def disp(self):
		print self.name
		print self.ref.name
		self.__hits += 1



obj = Second()

obj.disp();

print obj._Second__hits #accessing hiddent attribute outside function