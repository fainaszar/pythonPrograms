
number =int(raw_input("Enter a number: "))

for i in range(2,number):

	if number % i ==0 :
		print "%d is not a Prime Number" % number
		break

else:
	print "%d is a Prime Number" % number