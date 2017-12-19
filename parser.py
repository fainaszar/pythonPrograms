import json
import pandas
import recordlinkage
import sys
import csv
import numpy as np
import requests
from matplotlib import pyplot

data = list()

def parse_field(filename,fieldname):
	
	List = []
	output=[]
	with open(filename) as file:
		reader = csv.DictReader(file,delimiter=',')
		for line in reader:
			List.append(line[fieldname])


	for idList in List:
		idList = idList.strip("[,]")
		idList = idList.split(", ")

		for item in idList:
			item = item.strip("\'")
			if item != '':
				if item.isnumeric():
					output.append(int(item))
				else:
					item = item.replace("u'"," ")
					item = item.strip()
					output.append(item)




	return output


def get_record(pmid):

	
	
	with open("PubmedData.csv") as file:
		reader = csv.DictReader(file,delimiter=',')
		for line in reader:
			if str(pmid) in line["PMID"]:
				print("%s\t\t%s...\t\t\t%s" % (line["PMID"],line["Title"][:50],line["Author"]))
				print("-"*100)



	
				

	# file = pandas.read_csv("PubmedData.csv")
	# index = file.set_index("PMID")

	# try:
	# 	data = index.loc[[pmid]]
	# 	print(data)
	# except Exception:
	# 	print("Unable to Load data")

		
	
def get_details(name):
	print(name,)

	
	with open("PubmedData.csv") as file:
		reader = csv.DictReader(file,delimiter=',')
		for line in reader:
			if name in line["Author"]:
				print("\t\t%s...\t\t\t\tPubmed Article" % (line["Title"][:70]))

				

	
	with open("ClinicalTrialsData.csv") as file:
		reader = csv.DictReader(file,delimiter=',')
		for line in reader:
			if name in line["Investigator"]:
				print("\t\t%s...\t\t\t\tClinical Trial\n" % (line["Title"][:70]))


				




				
	print("-"*100)



pd = pandas.read_csv("PubmedData.csv")
ct = pandas.read_csv("ClinicalTrialsData.csv")


# ctPMID = parse_field("ClinicalTrialsData.csv","PMID")

# pdPMID = parse_field("PubmedData.csv","PMID")


Investigators = set(parse_field("ClinicalTrialsData.csv","Investigator"))
Authors = set(parse_field("PubmedData.csv","Author"))
print("Author <--> Investigator Linkage Result".center(120,"*"))
print("Author/Investigator\t\t\tTitle\t\t\t\t\t\t\t\tType\t\t")
print("-"*120)
count = 0
for Investigator in Investigators:
	
	if Investigator in Authors:
		#print("-"*60)
		#print("Investigator/Author  ", Investigator )

		get_details(Investigator)

		
		count+=1


# print("A total of %d records matched" % count)





# count = 0
# for pid in pdPMID:
# 	if pid in ctPMID:
# 		#print("PMID " , pid , " exists in CTGOV DATA")
# 		count += 1

# print("A total of %d records found" % count)

# print("PMID\tTitle\t\t\t\t\tAuthor/Investigator")
# print("-"*100)
# # count = 0
# for ctID in ctPMID:
# 	if ctID in pdPMID:
# 		#print('ctID: %d' % ctID )
# 		get_record(ctID)
		

# print("A total of %d records found vice-versa" % count)

# get_record(27832834)






print(data)