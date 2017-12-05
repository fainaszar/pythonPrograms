
def shout(text):
	return text.upper()


def whisper(text):
	return text.lower()


print shout("Hello")

#Assigning Function to a variable
yell = shout

print yell("Hello")


#Passing function as objects

def greet(func):
	greeting = func("Hi, I am created using argument")
	print greeting



greet(shout)
greet(whisper)



#Function returning fuctions

def create_adder(x):
	def adder(y):
		return x+y

	return adder


add_15 = create_adder(15)

#print add_15

print add_15(10)