# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xml.etree.ElementTree as ET 
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Months={
# 	"January" : 1,
# 	"February" : 2,
# 	"March" : 3,
# 	"April":4,
# 	"May":5,
# 	"June":6,
# 	"July":7,
# 	"August":8,
# 	"September":9,
# 	"October":10,
# 	"November":11,
# 	"December":12
# }



# path = os.getcwd();
# files =  [file for file in glob.glob('*.xml')]

# Ct_data = open('ClinicalTrialsData.csv','w')


# csvwriter = csv.writer(Ct_data)
# ct_head = []
# ct_row=[]

# count = 0





# for file in files:
# 	ct_row=[]
# 	tree = ET.parse(file)
	
# 	root = tree.getroot()

# 	if count == 0: 
		
# 		ct_head.append("pmid")
# 		breifTitle = root.find('brief_title').tag

# 		ct_head.append(breifTitle)

# 		created = root.find('study_first_submitted').tag
# 		ct_head.append(created)

# 		updated = root.find('last_update_submitted').tag
# 		ct_head.append(updated)

# 		revised = root.find('lastchanged_date').tag
# 		ct_head.append(revised)

# 		ct_head.append("Investigator")


		
# 		csvwriter.writerow(ct_head)	 
# 		count+=1

# 	mylist=list()
# 	myId = root.findall('reference')
# 	for ref in myId:
# 		for re in ref.getiterator():
# 			if re.tag == "PMID":
# 				mylist.append(re.text)

# 	ct_row.append(mylist)

# 	breifTitle = root.find('brief_title').text
# 	ct_row.append(breifTitle)

# 	created = root.find('study_first_submitted').text
# 	date , year = created.split(",")

# 	date = date.split()

# 	month = Months[date[0]]

# 	newdate = date[1] + "/" + str(month) + "/" + year.strip()

# 	ct_row.append(newdate)


# 	updated = root.find('last_update_submitted').text
# 	date , year = updated.split(",")

# 	date = date.split()

# 	month = Months[date[0]]

# 	newdate = date[1] + "/" + str(month) + "/" + year.strip()

# 	ct_row.append(newdate)
	

# 	revised = root.find('lastchanged_date').text
# 	date , year = revised.split(",")

# 	date = date.split()

# 	month = Months[date[0]]

# 	newdate = date[1] + "/" + str(month) + "/" + year.strip()

# 	ct_row.append(newdate)
	
# 	investigator = ""
# 	try:
# 		itag = root.find('overall_official')
# 		iname = itag.find('last_name').text.split(",")[0]
# 		investigator = iname.strip()
		
		
# 	except Exception:
# 		pass

# 	print(investigator)
# 	ct_row.append(investigator)

# 	csvwriter.writerow(ct_row)



# Ct_data.close()

tree = ET.parse("medline17n0263.xml")
root = tree.getroot()


#Ct_data = open('ClinicalTrialsData.csv','w')


# #csvwriter = csv.writer(Ct_data)
# ct_head = []
# ct_row=[]

# #tags = root.findall('clinical_study')


# count = 0

# ct_row=[]
# if count == 0: 
		
		
# 	breifTitle = root.find('brief_title').tag

# 	ct_head.append(breifTitle)

# 	created = root.find('study_first_submitted').tag
# 	ct_head.append(created)

# 	updated = root.find('last_update_submitted').tag
# 	ct_head.append(updated)

# 	revised = root.find('lastchanged_date').tag
# 	ct_head.append(revised)


		
# #	csvwriter.writerow(ct_head)	 
# 	count+=1

# # breifTitle = root.find('brief_title').text
# # ct_row.append(breifTitle)

# created = root.find('study_first_submitted').text
# date , year = created.split(",")

# date = date.split()

# month = Months[date[0]]

# newdate = date[1] + "/" + str(month) + "/" + year.strip()

# ct_row.append(newdate)


# # updated = root.find('last_update_submitted').text
# # ct_row.append(updated)

# # revised = root.find('lastchanged_date').text
# # ct_row.append(revised)
# #csvwriter.writerow(ct_row)



# tree = ET.parse("medline17n0001.xml")
# root = tree.getroot()

Article_data = open('PubmedData.csv','a')


csvwriter = csv.writer(Article_data)
article_head = []
article_row=[]

tags = root.findall('PubmedArticle')


count = 0
for member in tags:
	article_row=[]
	# if count == 0: 
	# 	citation = member.find('MedlineCitation')
		
	# 	pmid = citation.find('PMID').tag
	# 	article_head.append(pmid)
	# 	article = citation.find('Article')
	# 	articleTitle = article.find('ArticleTitle').tag
	# 	article_head.append("Title")
	# 	createddate = citation.find('DateCreated').tag
	# 	article_head.append(createddate)
	# 	completeddate = citation.find('DateCompleted').tag
	# 	article_head.append(completeddate)
	# 	datemodified = citation.find('DateRevised').tag
	# 	article_head.append(datemodified)
	# 	article_head.append("Author")
	# 	csvwriter.writerow(article_head)	 
	# 	count+=1

	

	citation = member.find('MedlineCitation')
	pmid = citation.find('PMID').text
	article_row.append(pmid)
	article = citation.find('Article')
	articleTitle = article.find('ArticleTitle').text
	article_row.append(articleTitle)
	createddate = citation.find('DateCreated')
	article_row.append(createddate[2].text + "/" + createddate[1].text +"/"+ createddate[0].text)
	
	try:
		completeddate = citation.find('DateCompleted')
		article_row.append(completeddate[2].text + "/" + completeddate[1].text +"/"+ completeddate[0].text)
	except Exception:
		article_row.append("")
	try:
		datemodified = citation.find('DateRevised')
		article_row.append(datemodified[2].text + "/" + datemodified[1].text +"/"+ datemodified[0].text)
	except Exception:
		article_row.append("")

	authorlist = article.find('AuthorList')
	authors = []
	try:
		for author in authorlist.findall("Author"):
			authors.append(author[1].text + " " + author[0].text)
	except Exception:
		pass

	article_row.append(authors)
	csvwriter.writerow(article_row)







			
	
	


	# if count == 0:
	# 	article = member.find('Article').tag
	# 	article_head.append(article)
	# 	articleTitle = member.find('ArticleTitle').tag
	# 	article_head.append(articleTitle)
	# 	author = member.find('AuthorList').tag
	# 	article_head.append(author)
	# 	publication = member.find('Journal').tag
	# 	article_head.append(publication)

	# 	csvwriter.writerow(article_head)
	# 	count += 1

	# article = member.find('Article').text
	# articles.append(article)
	# articleTitle = member.find('ArticleTitle').text
	# articles.append(articleTitle)
	# author = member.find('AuthorList').text
	# article.append(author)
	# publication = member.find('Journal').text
	# article.append(publication)

	# csvwriter.writerow(articles)
	
Article_data.close()








