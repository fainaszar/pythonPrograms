
def binarySearch(list,num):

	print list
	print len(list)
	if len(list)==0:
		print "False"
		return False

	mid = len(list)//2

	print mid

	if(list[mid] == num):
		print "True"
		return True

	
		if (num < list[mid]):
			binarySearch(list[:mid],num)
		else:
			binarySearch(list[mid+1:len(list)],num)






numList = [1,2,3,4,5,6,7,8]
result = binarySearch(numList,4)
print result