import requests
import csv
base_url = "http://havoc.appliedinformaticsinc.com/"
user = "1234"
token ="4321trialx"


symtoms = list()
with open("general medicine.csv","rb") as file:
	reader = csv.DictReader(file)
	for line in reader:
		symtoms.append(line["initial_diagnosis"])


symtoms = set(symtoms)

#print symtoms


# term = raw_input("Enter a term: ")
for term in symtoms:
	response = requests.get(base_url+"concepts?term="+term+"&user="+user+"&token="+token)

	response = response.json()
	synonyms = set()
	for res in response:
		cui = res["cui"]

# 	resp = requests.get(base_url+"concepts/"+cui+"/synonyms?user="+user+"&token="+token)
# 	resp = resp.json()
# 	for r in resp:
# 		synonyms.add(r.encode("utf-8"))




# parentList=list()

# response = requests.get(base_url+"concepts/"+cui+"/parents?user="+user+"&token="+token)
# for res in response.json():
# 	print res["cui"]


