import requests

base_url = "http://havoc.appliedinformaticsinc.com/"
user = "1234"
token ="4321trialx"


term = raw_input("Enter a term: ")
response = requests.get(base_url+"concepts?term="+term+"&user="+user+"&token="+token)

response = response.json()
synonyms = set()
for res in response:
	cui = res["cui"]

	resp = requests.get(base_url+"concepts/"+cui+"/synonyms?user="+user+"&token="+token)
	resp = resp.json()
	for r in resp:
		synonyms.add(r.encode("utf-8"))




parentList=list()

response = requests.get(base_url+"concepts/"+cui+"/parents?user="+user+"&token="+token)
for res in response.json():
	print res["cui"]


