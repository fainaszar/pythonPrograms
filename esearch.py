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

result = es.get(index='sw',doc_type='people',id=33)




