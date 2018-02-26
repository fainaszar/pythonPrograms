import requests
import csv
import json

base_url = "http://havoc.appliedinformaticsinc.com/"
user = "155"
token ="4qt-e35c90993c794d8911a4"


symtoms = list()
with open("endocrinology.csv","rb") as file:
	reader = csv.DictReader(file)
	for line in reader:
		symtoms.append(line["initial_diagnosis"])


symtoms = set(symtoms)



terms = list(symtoms)



for term in terms[70:100]:
	
	response = requests.get(base_url+"concepts?term="+term+"&user="+user+"&token="+token)
	
	response = response.json()
	CuiList = list()
	alias=list()
	childs=set()
	
	if not response == []:

		print "-"*70

		print "\nTerm: {}\n".format(term)
		
		for data in response:
			CuiList.append(data["cui"].encode('utf-8'))

		
		terms = set()
		for cui in CuiList:
			resp = requests.get(base_url+"concepts/"+cui+"/parents?user="+user+"&token="+token)
 			resp = resp.json()
			for data in resp:
				t = data["terms"]
				for term in t:
					terms.add(term.encode('utf-8'))

			resp2 = requests.get(base_url+"concepts/"+cui+"/synonyms?user="+user+"&token="+token)
 			resp2 = resp2.json()
			for data in resp2:
				alias.append(data.encode('utf-8'))



			resp3 = requests.get(base_url+"concepts/"+cui+"/children?user="+user+"&token="+token)
 			resp3 = resp3.json()
			for data in resp3:
				
				t= data["terms"]
				for term in t:
					childs.add(term.encode('utf-8'))





		print "Synonyms for the TERM : \n"
		for synonym in (set(alias)):
			print synonym + ",",
		print "\n"

		print "Parents for term: \n"
		for term in terms:
			print term + ",",


		print "\nChildrens for term: \n"
		for term in childs:
			print term + ",",

		print "-"*70

	else:
		print "Diagonosis {} not properly defined. Unable to fetch parents/synonyms list".format(term)


	

	


