from Bio import Entrez

data = open("medline17n0001.xml")

records = Entrez.read(data,validate=False)


#print records


for record in records["PubmedArticle"]:
	print record

# for record in records:
# 	print  record['PubmedArticle']
# for i , paper in enumerate(records['PubmedArticle']):
# 	print("%d) %s" % (i+1,paper['MedilineCitation'] ['Article']['ArticleTitle'])