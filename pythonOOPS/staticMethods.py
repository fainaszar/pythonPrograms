class Try:

	no = 123	

	def __init__(self,name):
		self.name = name

	def print_name():
		print self.name


	@staticmethod
	def set_no():
		Try.no = 122


t = Try("Faizan")
print t.name

print t.no

print Try.no

Try.set_no()

print t.no


print t.set_no()