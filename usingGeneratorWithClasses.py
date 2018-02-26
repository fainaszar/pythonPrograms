
class Bank(object):
	crisis = False

	def create_atm(self):
		while not self.crisis:
			yield "$100"



jkBank = Bank()

print "Creating branches"
branch1 = jkBank.create_atm()
branch2 = jkBank.create_atm()

print "Getting Cash from new branches"
print branch1.next()
print branch2.next()

print "Bank under Crisis"
jkBank.crisis = True
try:
	print "Getting cash from branches"
	print branch1.next()
	print branch2.next()


	print "Creating new branch"
	branch3 = jkBank.create_atm()

	print "Getting cash from new branch"
	print branch3.next()
except StopIteration:
	print "Bank Under Crisis!! Sorry for inconvenience"



print "Creating new branch"
branch3 = jkBank.create_atm()

try:
	print "Getting cash from new branch"
	print branch3.next()
except StopIteration:
	print "Bank under crisis , Cannot produce cash"
finally:
	jkBank.crisis = False


print branch1.next()
print branch2.next()
print branch3.next()

