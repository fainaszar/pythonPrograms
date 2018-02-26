import json
import xmltodict



with open('NCT00000104.xml' ,"rb") as file:
	data = xmltodict.parse(file)


#print data
output = json.dumps(data)
print output


with open('output.json' , 'w') as f:
	f.write(output)
