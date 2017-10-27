
def processList(lst):
	
	for name in lst:
		
		if " " in name:

			list1 = name.split()
			
			for item in list1:

				if lst.count(item.lower()) > 0:
					lst.remove(item.lower())

				if lst.count(item) > 0:
					lst.remove(item)
		else:
			if lst.count(name) > 1:
				x = lst.index(name)
				for i in lst[x+1:]:
					if i == name:
						lst.remove(i)
	return lst






List = ["Bayer Aspirin","aspirin","xelzange ","lyrica","Xelzange Maven" ,"Xelzange","aspirin","Pfizer Aspirin" , "Aspirin", "s","s","s","s" ,"t"]
#N = int(raw_input("Enter no of list items"))

#for i in range(N):
#	inpList.append(raw_input())
inpList=[]
#print "Input List:\n",List
#print "\n"

for item in List:
	inpList.append(item.strip())

print "Input List: \n" ,inpList


optList = processList(inpList)

print "Output List:\n",optList

