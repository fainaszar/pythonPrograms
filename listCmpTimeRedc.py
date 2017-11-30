from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def checkMatches(List,drug):

	print List

	length = len(List)
	mid = length/2

	#print "EQUAL %r , LESS %r , GREATER %r " % (drug == List[mid] , drug < List[mid] , drug > List[mid])
	
	if List[mid] > drug:
		res = process.extractOne(drug,List[:mid+1])
		print res
	else:
		res = process.extractOne(drug,List[mid:])
		print res




alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]




dictList=[]
List = ["Bayer Aspirin","mavin","crosin","xelzange","cipla","lyreca","lyrics","dolo","Tramadol","ibuprofin","Gabapentin","Xelzange Maven","Pfizer Aspirin" ,"Atorvastatin Calcium",
"Levothyroxine","Lisinopril","Omeprazole" ,"Metformin" ,"Simvastatin", "Hydrocodone" ,"Metoprolol ER","Azithromycin" ,"Zolpidem" ,
"Hydrochlorothiazide" ,"Furosemide" ,"Metoprolol", "Pantoprazole", "Gabapentin", "Amoxicillin","Prednisone", "Sertraline ","Tamsulosin", 
"Fluticasone", "Pravastatin", "Tramadol", "Montelukast", "Escitalopram", "Carvedilol", "Alprazolam"]

List = [i.lower() for i in List]
#print List

for alphabet in alphabets:
	letter = alphabet
	alphabet = dict()

	for item in List:
		if item.startswith(letter.lower()):

			alphabet.update({item.lower(): ''})
	dictList.append(alphabet)



print dictList


inpList = ["maven","pantop","mitropolo"]

for item in inpList:
	index = ord(item[0].upper()) - 65

	checkMatches(sorted(dictList[index].keys()),item)

