
def processList(lst):
	
	for name in lst:
		
		if " " in name:

			list1 = name.split()
			
			for item in list1:

				if lst.count(item.lower()) > 0:
					lst.remove(item.lower())

				if lst.count(item) > 0:
					lst.remove(item)

			if lst.count(name) > 1:
				x=lst.index(name)
				for i in lst[x+1:]:
					if i == name:
						lst.remove(i)

		else:
			if lst.count(name) > 1:
				x = lst.index(name)
				for i in lst[x+1:]:
					if i == name:
						lst.remove(i)
	return lst


def processList2(lst):

	for i in range(len(lst)):
		lst[i] = lst[i].strip()


	singleItemsList=[]
	multiItemsList=[]

	for name in lst:
		if (len(name.split())) > 1:
			multiItemsList.append(name.split())
		else:
			singleItemsList.append(name)


	


	for nameList in multiItemsList:
		
		for name in nameList:
			

			if name in singleItemsList:
				singleItemsList.remove(name)
				lst.remove(name)
				
			if name.lower() in singleItemsList:
				singleItemsList.remove(name.lower())
				lst.remove(name.lower())


				
			
		for item in singleItemsList:
			
			if lst.count(item) > 1:
				x = lst.index(item)
				for i in lst[x+1:]:
					if i == item:
						lst.remove(i)


		for name in lst:
			if lst.count(name) > 1:
					x=lst.index(name)
					for i in lst[x+1:]:
						if i == name:
							lst.remove(i)
		op = []


		for item in lst:
			op.append(item.strip())

	return op



List = ["Bayer Aspirin","aspirin","xelzange ","lyrica","Xelzange Maven" ,"aspirin", "Xelzange","aspirin","Pfizer Aspirin" , "Aspirin", "s","s","s","s" ,"t","Bayer Aspirin"]
#N = int(raw_input("Enter no of list items"))

#for i in range(N):
#	inpList.append(raw_input())
inpList=[]
print "Input List:\n",List
#print "\n"

for item in List:
	inpList.append(item.strip())

print "Input List: \n" ,inpList

#processList2(List)
optList = processList(inpList)

print "Output List:\n",optList

#print "Output method2: "
#print processList2(List)