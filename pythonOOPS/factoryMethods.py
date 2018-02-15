
class Car(object):

	def factory(type):
		if type=="Racecar":
			return Racecar()
		if type=="Van":
			return Van()

		raise AssertionError("Bad car creation: " + type)


	factory = staticmethod(factory)


class Racecar(Car):
	def drive(self):
		print("Racecar driving")


class Van(Car):
	def drive(self):
		print("Van driving")



obj = Car.factory("Bus")
obj.drive()