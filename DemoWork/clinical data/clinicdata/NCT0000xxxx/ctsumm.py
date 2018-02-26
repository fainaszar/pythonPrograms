import json
import xml.etree.ElementTree as ET 
import xmltodict
import csv
import os
import glob
import nltk
from nltk.corpus import stopwords
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def checkForAbstract(root):

	
	try:
		description = root.find("detailed_description")


		return True
	except:

		return False
	
		

path = os.getcwd();
files =  [file for file in glob.glob('*.xml')]

Ct_data = open('Summarizer.csv','w')


csvwriter = csv.writer(Ct_data)
ct_head = []
ct_row=[]

count = 0





for file in files:

	print "Processing file {}".format(file)
	ct_row=[]
	tree = ET.parse(file)
	
	root = tree.getroot()

	if count == 0: 
		
		ct_head.append("Breif Title")
		ct_head.append("Abstract Text")
		ct_head.append("Concept")


		
		csvwriter.writerow(ct_head)	 
		count+=1

	

	breifTitle = root.find('brief_title').text
	ct_row.append(breifTitle)

	
	

	if checkForAbstract(root):

		

		description = root.find("detailed_description")

		
		
		text=""
		try:
			for element in description:
				text = element.text
		except:
			pass

		ct_row.append(text)


		tokensWithoutStopWords = [t for t in text.split() if t not in stopwords.words('english')]

		#print tokensWithoutStopWords

		freq = nltk.FreqDist(tokensWithoutStopWords)
		print freq
		


	else:

		ct_row.append("None")
		ct_row.append("None")








	csvwriter.writerow(ct_row)



Ct_data.close()