
class CSStudent:

	stream = "CSE" #classVariable

	def __init__(self,name,roll):
		self.name = name
		self.roll = roll


a = CSStudent('Faizan',1)
b = CSStudent('Faisal',2)

print(a.stream)
print(b.stream)

print(a.name)
print(b.name)

print(a.roll)
print(b.roll)

print CSStudent.stream

