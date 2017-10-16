input_params = raw_input().split()
lists=[]
for i in range(int(input_params[0])):
	list = raw_input().split()
	list = map(int ,list)
	lists.append(list)

sum = 0
from itertools import product
product(*lists)
print product
print "Sum is %r" % sum
for list in lists:

	
	
	maxItem =  max(list)

	
	
	square = maxItem **2

	
	
	sum +=  square

	


print sum % int(input_params[1])