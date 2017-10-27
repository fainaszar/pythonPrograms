
def processList(lst):
	
	for name in lst:
		
		if " " in name:

			list1 = name.split()
			
			for item in list1:

				if lst.count(item.lower()) > 0:
					lst.remove(item.lower())

				if lst.count(item) > 0:
					lst.remove(item)

					
	return lst



inpList = ["Bayer Aspirin","aspirin","xelzange","lyrica","Xelzange Maven" ,"Xelzange","aspirin", "Pfizer Aspirin" , "Aspirin"]
#N = int(raw_input("Enter no of list items"))

#for i in range(N):
#	inpList.append(raw_input())

print "Input List:\n",inpList
print "\n"
optList = processList(inpList)

print "Output List:\n",optList