
from datetime import date


#Class Vs Static methods:
#A class method takes cls as first parameter while a static method needs no specific parameters
#A class method can access or modify class state state while a static method can't access or modify it
#We use @classmethod decorator to create a class method and @staticmethod decorator to create a static method

class Person:

	def __init__(self,name,age):
		self.name = name
		self.age = age


	@classmethod
	def fromBirthYear(cls,name,year):
		return cls(name,date.today().year-year)


	@staticmethod
	def isAdult(age):
		return age>18




person1 = Person('Mayank',21)
person2 = Person.fromBirthYear('Faizan',1992)

print person1.age
print person2.age


print Person.isAdult(22)