

#Blocking.csv - PMID,ArticleTitle,Authors,Abstract,Date,country
#clinicalTrials3.csv contains-brief_title,condition,study_first_submitted,nct_id,PMID,last_update_submitted,lastchanged_date,name 
import pandas as pd
import csv
import json
# this thing returns the values' based on the original file


def get_info(pmid):
   f = pd.read_csv("PubmedData.csv",encoding = "ISO-8859-1")
   #df=f.set_index('PMID',inplace=True)
   # for index, row in f.iterrows():
   #    if int(row['PMID'])==int(pmid):
   #      return {'PMID':row['PMID'],'ArticleTitle':row['ArticleTitle'],'Authors':row['Authors']}
   pmid=int(pmid)
   print( int(pmid))
   try:
     f.loc[pmid]
   except:
    return 0
   return f.loc[[pmid]] 
#def get_info_from_file()

#f = pd.read_csv("Whole_Data_Record.csv",encoding = "ISO-8859-1")
dg= pd.read_csv("ClinicalTrialsData.csv",encoding = "ISO-8859-1")




# print(f['PMID'].tolist())

# for i in [
# 27899016,
# 27899017,
# 27899019,
# 27899020,
# 27899021,
# 27899025,
# 27899027,
# 27899028,
# 27899031,
# 27899043,
# 27899047,
# 27899055,
# 27899065,
# 27899071,
# 27899075,
# 27919888,
# 27919889,
# 27919906,
# 27919916,
# 27919925,
# 27919935,
# 27919938,
# 27919942]:

  # try:
  #  print(get_info(i))
  #  print("*"*15)

  # except:
  #   pass
  ###########################################


################################################
list_PM_Clin=dg['PMID'].tolist()
#ncter_id= dg['nct_id'].tolist()
# #print(ncter_id)
# #print (f['PMID'].tolist())

count=0
#for ran, nct_id in zip(list_PM_Clin,ncter_id):
  
for ran in list_PM_Clin:
    count+1
    man= ran.strip("[,],\'")
    tan=man.split("', '")
    #print(tan,len(tan))
    appendedRecord=list()
    if len(tan)>1:
       for index, value in enumerate(tan):
          appendedRecord.append(get_info(value))
       print({'nct_id':count,'record':appendedRecord}) 
    elif len(ran)==1:
        record=get_info(value)
        if record!=0:
          print ({'nct_id':count,'record':record})
    else:    
       print ({'nct_id':count,'record':0})  # This condition checks for empty  pmid 
##############################################