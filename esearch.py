import requests

from elasticsearch import Elasticsearch

res = requests.get('http://localhost:9200?pretty')

es = Elasticsearch([{'host':'localhost','port':9200}])

import json

r = requests.get('http://localhost:9200')
i=1

file = open("output.json").read()
# while r.status_code == 200 :
# 	r = requests.get('http://swapi.co/api/people/' + str(i))
es.index(index='sw',doc_type='people',body=file)
#	i += 1

result = es.get(index='sw',doc_type='people',id=5)

outputFormat = """
Name : {source[name]} ,
Height : {source[height]} ,
Gender: {source[gender]} ,
Birth Year: {source[birth_year]},
Mass : {source[mass]},
Vehicles : {source[vehicles]},
Url : {source[url]}"""


# count=0
# MissingIds=list()

# for i in range(50):
# 	try:
# 		result = es.get(index='sw',doc_type='people',id=i)
# 		source = result["_source"]
# 		print(outputFormat).format(source=source)
# 		count+=1
# 	except:
# 		MissingIds.append(i)


# print "No of records printed: {} , Missing Ids include: {}".format(count,MissingIds)





searchQueryResult = es.search(index="sw",body={"query":{"prefix": {"name" : "lu"}}})

print searchQueryResult