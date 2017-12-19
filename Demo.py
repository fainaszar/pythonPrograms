import json
import pandas
import recordlinkage
import sys
import csv
import numpy as np
from matplotlib import pyplot

#reload(sys)
#sys.setdefaultencoding('utf8')


#pd , ct = pandas.DataFrame.from_csv("ArticleData.csv") , pandas.DataFrame.from_csv("ClinicalTrialsData.csv")

pd = pandas.read_csv("PubmedData.csv")
ct = pandas.read_csv("ClinicalTrialsData.csv")

#print pd
investigators=[]
with open("ClinicalTrialsData.csv") as file:
	reader = csv.DictReader(file,delimiter=',')
	for line in reader:
		investigators.append(line["Investigator"])



auth=[]
authors=[]
with open("PubmedData.csv") as file:
	reader = csv.DictReader(file,delimiter=',')
	for line in reader:
		authors.append(line["Author"])


for author in authors:
	author = author.strip("\",[,]")
	author = author.split(",")

	

	for name in author:
		name = name.strip()
		auth.append(name)




for Investigator in investigators:
	if Investigator in auth and Investigator != "":
		print("Investigator " , Investigator , " present in Author List")
		
		
		



indexer = recordlinkage.SortedNeighbourhoodIndex(on="Title")
pairs = indexer.index(pd,ct)











compare_cl = recordlinkage.Compare()

compare_cl.string('Title', 'Title', method='levenshtein',label="Levenshtein - Method")
compare_cl.string('Title', 'Title', method='jarowinkler',label="Jarowinkler - Method")


#compare_cl.string('DateRevised','DateRevised',method='jarowinkler' ,label="Date")

#compare_cl.exact('DateCreated','DateCompleted', label="DateCompleted")

# compare_cl.exact('DateRevised','DateCompleted', label="DateCompleted")

# compare_cl.exact('DateRevised','DateRevised',label="DateRevised")


print("RecordLinkage based on DateRevised Comparison\n")


features = compare_cl.compute(pairs,pd,ct)

#print (features)
#print (features.describe())


jsonData = features.describe().to_json()

#print("Records Compared: " , int(jsonData["Jarowinkler - Method"]["count"]))
with open("rlDateRevised.json","w") as file:
	file.write(jsonData)

labels=["L-Method","J-Method","Date"]
values=[]




for item in features.mean():
	item = item * 100
	values.append(item)


# trace = go.Pie(labels=labels,values=values)
# py.iplot([trace],filename='title_match')


# print(values)
# figure = pyplot.figure(figsize=(7,7))

# pyplot.pie(values,labels=labels,startangle=90,autopct='%1.1f%%')
# pyplot.title('Match Based on DateCreated and MEAN() from feature set',bbox={'facecolor':'0.8','pad':5})
# pyplot.show()





#print features.sum(axis=1)
#Matching Titles


# aCompDates=[]
# with open("ArticleData.csv") as file:
# 	reader = csv.DictReader(file,delimiter=',')
# 	for line in reader:
# 		aCompDates.append(line["DateCompleted"].split("/")[-1])
# D = set(aCompDates)
# D = tuple(sorted(D))

# cCompDates=[]
# with open("ClinicalTrialsData.csv") as file:
# 	reader= csv.DictReader(file,delimiter=',')
# 	for line in reader:
# 		cCompDates.append(line["DateCompleted"].split("/")[-1])

# A=[]
# C=[]

# dates = open("CmpDates.csv","w")
# cd = csv.writer(dates)

# row=["Year","Clinical Trials","Pubmed Articles"]
# cd.writerow(row)

# for i in range(1976,2018):
# 	row=[]
# 	aCount=0
# 	cCount=0
# 	for year in cCompDates:
# 		if year == str(i):
# 			cCount+=1

# 	for year in aCompDates:
# 		if year == str(i):
# 			aCount+=1

# 	A.append(aCount)
# 	C.append(cCount)
# 	#print("Year %d:\nClinical Trials: %d\nPubmedArticle: %d\n" % (i,cCount,aCount))
# 	row.append(i)
# 	row.append(cCount)
# 	row.append(aCount)
# 	cd.writerow(row)



# # A = tuple(A)
# # C = tuple(C)


# # N=42
# # ind = np.arange(N)
# # width=0.6

# # fig,ax = pyplot.subplots()

# # rects1 = ax.bar(ind,A,width,color='r')
# # rects2 = ax.bar(ind,C,width,color='y')

# # ax.set_ylabel('No of Studies/Trials')
# # ax.set_title('No of Articles/Trials Completed in Years')
# # ax.set_xticks(ind + width/2)
# # ax.set_xticklabels(D)


# # ax.legend((rects1[0],rects2[0]),('Pubmed Articles','Clinical Trials'))

# # def autolabel(rects):
# #     """
# #     Attach a text label above each bar displaying its height
# #     """
# #     for rect in rects:
# #         height = rect.get_height()
# #         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
# #                 '%d' % int(height),
# #                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)






# # pyplot.show()


# obj = pandas.read_csv("CreatedDates.csv");
# output = json.loads(obj.to_json())






