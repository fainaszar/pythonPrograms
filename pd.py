import pandas as pd
import recordlinkage
import xml.etree.ElementTree as ET

import xmldataset
import json
import xmltodict

xml_data = open("ct.xml")


# profile="""
# PubmedArticleSet
# 	PubmedArticle
# 		MedlineCitation
# 			Article
# 				ArticleTitle = dataset:ArticleTitle
# 			AuthorList
# 				Author=dataset:Author



# """

# output = xmldataset.parse_using_profile(xml_data,profile)
# print(output)

#print pd.DataFrame.from_csv("AritcleData.csv")

# tree = ET.parse(xml_data)
# root = tree.getroot()

# all_records=[]

# for i, child in enumerate(root):
# 	record={}
# 	for subchild in child:
# 		record[subchild.tag] = subchild.text
# 		all_records.append(record)


# print pd.DataFrame(all_records)

jsonfile = open("output.json")
print  pd.read_json(jsonfile)


# with open('try.xml' ,"rb") as file:
# 	data = xmltodict.parse(file)


# #print data
# output = json.dumps(data)


# with open("op2.json","w") as file:
# 	file.write(output)



# jsonfile2 = open("op2.json")
# b = pd.read_json(jsonfile2) 
# print b

# #print pd.read_json(output)


# c= recordlinkage.Compare()


