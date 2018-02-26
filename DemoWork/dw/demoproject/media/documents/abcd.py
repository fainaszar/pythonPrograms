import json
import xmltodict
import csv
import os
import glob
import sys
reload(sys)
sys.setdefaultencoding('utf8')

path = os.getcwd();
files =  [file for file in glob.glob('*.xml')]

Ct_data = open('ClinicalTrialsData.csv','w')


csvwriter = csv.writer(Ct_data)
ct_head = []
ct_row=[]

count = 0





for file in files:
	ct_row=[]
	tree = ET.parse(file)
	root = tree.getroot()

	if count == 0: 
		
		
		breifTitle = root.find('brief_title').tag

		ct_head.append(breifTitle)

		created = root.find('study_first_submitted').tag
		ct_head.append(created)

		updated = root.find('last_update_submitted').tag
		ct_head.append(updated)

		revised = root.find('lastchanged_date').tag
		ct_head.append(revised)


		
		csvwriter.writerow(ct_head)	 
		count+=1

	breifTitle = root.find('brief_title').text
	ct_row.append(breifTitle)

	created = root.find('study_first_submitted').text
	ct_row.append(created)

	updated = root.find('last_update_submitted').text
	ct_row.append(updated)

	revised = root.find('lastchanged_date').text
	ct_row.append(revised)
	csvwriter.writerow(ct_row)




Ct_data.close()