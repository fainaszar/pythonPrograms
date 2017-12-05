#Example on oops using Inheritance


# For python3.4+ we use ABC and pass it as class arg and for python2 we use ABCMeta and add it as __metaclass__ attrib
#For python3.0 we use metaclass=ABCMeta as class arg
from abc import ABC ,ABCMeta, abstractmethod

class Vehicle(ABC):
	base_sales_price = 0

#	__metaclass__ = ABCMeta

	wheels = 0

	def __init__(self,miles,make,model,year,sold_on):

		
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on 


	def sales_price(self):
		if self.sold_on is not None:
			return 0.0
		return 5000.0 * self.wheels


	def purchase_price(self):
		if self.sold_on is not None:
			return 0.0
		return self.base_sales_price - (.10 * self.miles)


	@abstractmethod
	def vehicle_type():
		pass





class Car(Vehicle):

	base_sales_price =8000
	wheels =4

	def vehicle_type(self):

		return 'car'




class Truck(Vehicle):
	
	base_sales_price = 10000
	wheels =4


	def vehicle_type(self):
		return 'Truck'


class Motorcycle(Vehicle):
	base_sales_price = 4000
	wheels =2

	def vehicle_type(self):
		return "Motorcycle"

maruti = Car(300,"800","Maruti",2008,None)
tata = Truck(411,"991","TATA",2009,None)
scooty = Motorcycle(0,'Elantra','Bajaj',2011,None)

bike = Vehicle(200,"Honda","Splender",2000,3000)

# print bike.sales_price()

# print maruti.sales_price()

# print tata.sales_price()


# print maruti.purchase_price()
# print tata.purchase_price()

# print scooty.sales_price()
# print scooty.purchase_price()


