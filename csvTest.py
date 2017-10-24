import csv
#----------------------------------------------------------------------
#Method 1
def csv_reader(file_obj):

    """

    Read a csv file

    """

    rdr = csv.reader(file_obj)

    for row in rdr:

        print(" ".join(row))

#----------------------------------------------------------------------

#Method 2

def csv_dict_reader(file_obj):
	print "DictReader Fuction"
	reader = csv.DictReader(file_obj,delimiter=',')
	for lines in reader:
		print lines["FirstName"]
		print lines["Age"]
		
		

#-------------------------------------------------------------------------


def csv_writer(data,path):
	with open(path,"wb") as csv_file:
		writer = csv.writer(csv_file,delimiter=',')
		for line in data:
			writer.writerow(line)


def  csv_dict_writer(path,fieldnames,data):
	with open(path,"wb") as outfile:
		writer = csv.DictWriter(outfile,delimiter=',',fieldnames = fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)

if __name__ == "__main__":

    csv_path = "csvFile.csv"
    with open(csv_path, "rb") as f_obj:
    	#csv_reader(f_obj)
		csv_dict_reader(f_obj)


    data = ["FirstName,LastName,Age".split(","),"Sahil,Ahmad,25".split(","),"Basit,Ahmad,22".split(","),"Aqib,Bashir,21".split(",")]
    mylist=[]
    #path = "csvFile.csv"
    fieldnames = data[0]
    for values in data[1:]:
    	inner_dict = dict(zip(fieldnames,values))
    	
    	mylist.append(inner_dict)

    path = "csvOutFile.csv"
    csv_dict_writer(path,fieldnames,mylist)
    

#    csv_writer(data,path)
