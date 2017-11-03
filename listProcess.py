from fuzzywuzzy import fuzz
from fuzzywuzzy import process
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


			res = process.extract(name,lst)
			for (match,percent) in res:
				if percent in range(75,99):
#					print "m11:::: ",match
					lst.remove(match)
		else:
			if lst.count(name) > 1:
				x = lst.index(name)
				for i in lst[x+1:]:
					if i == name:
						lst.remove(i)

	
#	print "111111111\n " , lst 		


	for name in lst:
		if " " in name:

			list1 = name.split()

			for n in list1:
				
				res = process.extract(n,lst)
			#	print res
			for (match,percent) in res:
				if percent in range(80,99):
					#print "222222222222222222222", match
					if len(match) > 1 and " " not in match:
					#	print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
						lst.remove(match)

		else:
			
			res = process.extract(name,lst)
			
			for (match,percent) in res:
				if percent in range (60,99):
					if len(match) > 1 and " " not in match:
						lst.remove(match)
	return lst



def listProcessing(lst,scoreParam = 70):
	drugSet = set(lst)
	drugList = list(drugSet)
#	print drugList

	#Removing Drug names that are miss spelt and have spaces in between
	for drug in drugList:
		if " " in drug:
			#print "Drug: ", drug
			res = process.extract(drug,drugList)
			#print res
			for (match,percent) in res:
				if percent in range(int(scoreParam),99): #90-99
					drugList.remove(match)


	# Rem0ving Drugs that match substrings of other drugs (drugs with spaces within them)
	for drug in drugList:
		if " " in drug:

			list1 = drug.split()

			for n in list1:
				
				res = process.extract(n,drugList)
				
			for (match,percent) in res:
				if percent in range(int(scoreParam),99): #default param is 70
					#
					if len(match) > 1 and " " not in match:
					
						drugList.remove(match)

		else:
			#Removing Drugs that do not contain any spaces and are miss spelt
			#print "Drug: " ,drug
			res = process.extract(drug,drugList)

			#print res
			
			for (match,percent) in res:
				
				if len(drug) > 1:
					if percent in range (int(scoreParam),99): #default param is 80

						if len(match) > 1 and " " not in match:
							drugList.remove(match)
							#print "Removed: " , match
						

		




     
	print "\nOutput List: "
	print drugList



def processList2(lst):
	otherList = []

	

	cmpareList=[]
	print "\n"
	for name in lst:
		
		output = process.extract(name,lst)


		#removes duplicate entries
		for (match,percent) in output:
			
			if percent == 100:
				x = lst.index(match)
				for i in lst[x+1:]:
					if i == match:
						lst.remove(i)


						
		
		
		output = process.extract(name,lst)
		
		cmpareList=[]
		for (match,percent) in output:

			if percent == 100:
				cmpareList.append(match)
				
				greatest = cmpareList[0]

				for item in cmpareList[1:]:
					if item < greatest:
						greatest=item

				

				

				for item in cmpareList:
					if item != greatest:
						lst.remove(item)
						

		
			

	

	for item in lst:
		otherList.append(item)
	
	


	for name in otherList:
		if " " in name:
			
			rs = process.extract(name,lst)
			for (match,percent) in rs:
				if percent in range(75,99):
					lst.remove(match)
					otherList.remove(match)

			print lst
		else:
			
			rs = process.extract(name,lst)
			print rs
			for (match,percent) in rs:
				if percent in range(75,99):
					if (len(match)>1):
						lst.remove(match)
						otherList.remove(match)


	print lst

	


	

			

		
		
	print "\n"


List = ["Bayer Aspirin","asprn","aspirin","asprnn","mavin","xelzange ","Bayer Aspirinn","Bayir Aspirin","lyrica","lyreca","lyrics","Xelzange Maven" ,"Bayer Aspirin","Xelzange","aspirin","Pfizer Aspirin" , "Aspirin", "s","s","s","s" ,"t","Bayer Aspirin"]
#N = int(raw_input("Enter no of list items"))

#for i in range(N):
#	inpList.append(raw_input())
inpList=[]
#print "Input List:\n",List
#print "\n"

for item in List:
	inpList.append(item.strip())

print "Input List: \n\n" ,inpList


#optList = processList(inpList)

#print "\nOutput List: >>> WITHOUT USING SETS\n\n",optList
scoreParam = raw_input("\nEnter a scoring parameter (%): ")
if scoreParam == "":
	print "Scoring Parameter set to DEFAULT"
	listProcessing(inpList)
else:
	print "Scoring Parameter set to %s%% . All Drugs matching and above the scoring parameter shall be removed.\n" % scoreParam
	listProcessing(inpList,scoreParam = scoreParam)
#print "Method 2".center(40,"-")
#processList2(inpList)






#List2 = ["Digital Computer","Scientific Calculator","calculator","Basic computer","camputer","science","scientific things","digital"]

#processList2(List2)
#print processList(List2)