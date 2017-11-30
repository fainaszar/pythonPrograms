class RationalNumber:

	def __init__(self,numerator,denominator=1):
		self.n = numerator
		self.d = denominator


	def __add__(self,other):
		if not isinstance(other,RationalNumber):
			other = RationalNumber(other)

		n = self.n *other.d + self.d * other.n
		d = self.d * other.d

		return RationalNumber(n,d)



	def __sub__(self,other):
		if not isinstance(other,RationalNumber):
			other = RationalNumber(other)


		n1,d1 = self.n , self.d
		n2,d2 = other.n , other.d

		return RationalNumber(n1*d2 - n2*d1,d1*d2)




	def __mul__(self,other):
		if not isinstance(other,RationalNumber):
			other = RationalNumber(other)


		n1,d1 = self.n , self.d
		n2,d2 = other.n, other.d 
		return RationalNumber(n1*n2,d1*d2)



	def __div__(self,other):
		if not isinstance(other,RationalNumber):
			other = RationalNumber(other)


		n1,d1 = self.n,self.d 
		n2,d2 = other.n, other.d 

		return RationalNumber(n1*d2,d1*n2)


	def __str__(self):
		return "%s/%s" % (self.n,self.d)


	__repr__ = __str__






a = RationalNumber(1,2)
b = RationalNumber(1,3)

print("Using + operator ")
print (a+b)

print("Using __add__ function")

print(a.__add__(b))




print("Using - operator ")
print (a-b)

print("Using __sub__ function")

print(a.__sub__(b))



print("Using * operator ")
print (a*b)

print("Using __mul__ function")

print(a.__mul__(b))


print("Using / operator ")
print (a/b)

print("Using __div__ function")

print(a.__div__(b))

