#MRO - Method Resolution Order

class Base(object):


	def __init__(self):
		self.name="Name-Base1"
		print ("Base Init")


	def Func1(self):
		print("Base Func1")

	def Func2(self):
		print("Base Func2")

class Base2(object):

	def __init__(self):
		print("Base2 init")
		self.name="Name-Base2"

	def Func3(self):
		print("Base2 Func3")

	def Func4(self):
		print("Base2 Func3")


class Derived1(Base):

	def __init__(self):
		print("Derived1 init")

	def Func1(self):
		print("Derived1 Func1")

	def Func2(self):
		print("Derived1 Func2")

class Derived2(Base,Base2):

	
	def __init__(self):
		print("Derived2 init")
		Base.__init__(self)
		Base2.__init__(self)

	def A(self):
		print("Derived2 A")

	def B(self):
		print("Derived2 B")




# print ("Base - ----------------")

# print (Base.mro())

# print("Base2 - ----------------")
# print (Base2.mro())


# print("Derived1 - ---------------")
# print(Derived1.mro())


# print ("Derived2 - --------------")
# print(Derived2.mro())






d1 = Derived2()

print(d1.name)