#Example on oops using Inheritance


class Vehicle(object):
	base_sales_price = 0

	def __init__(self,wheels,miles,make,model,year,sold_on):

		self.wheels = wheels
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




class Car(Vehicle):

	def __init__(self,wheels,miles,make,model,year,sold_on):
		self.wheels=wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
		self.base_sales_price = 8000




class Truck(Vehicle):
	def __init__(self,wheels,miles,make,model,year,sold_on):
		self.wheels=wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
		self.base_sales_price = 10000




maruti = Car(4,300,"800","Maruti",2008,None)
tata = Truck(4,411,"991","TATA",2009,None)

v = Vehicle(4,0,'Honda','Accord',2014,None)



print maruti.sales_price()

print tata.sales_price()


print maruti.purchase_price()
print tata.purchase_price()


print v.sales_price()
print v.purchase_price()