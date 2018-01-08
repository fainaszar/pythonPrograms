import pymysql
import csv
hostname = 'localhost'
username = 'root'
password = 'Password1'



connection = pymysql.connect(host=hostname,user=username,password=password,db='gems')

print "Connection Successfull"
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS diamonds(carat FLOAT(4,2),cut VARCHAR(100),color VARCHAR(10),clarity VARCHAR(10),depth FLOAT(4,2),dtable int,price int,x FLOAT(4,2),y FLOAT(4,2),z FLOAT(4,2))"
print query
cursor.execute(query)

print "Table Created"

cursor.execute("show tables")


with open("diamonds.csv","rb") as file:
	reader = csv.DictReader(file)

	for line in reader:
		carat = float(line["carat"])
		
		cut = line["cut"]
		color = line["color"]
		clarity = line["clarity"]
		depth=float(line["depth"])
		try:
			table = int(line["table"])
		except Exception:
			table = float(line["table"])
			table = int(table)
		price = int(line["price"])
		x = float(line["x"])
		y = float(line["y"])
		z = float(line["z"])

		#print(carat,cut,color,clarity,depth,table,price,x,y,z)
		query ="INSERT INTO diamonds VALUES(%f,'%s','%s','%s',%f,%d,%d,%f,%f,%f);" % (carat,cut,color,clarity,depth,table,price,x,y,z)
		#print query
		cursor.execute(query)
		#print "1 Row Inserted"

		
connection.commit()



		

print "Data Successfully loaded into DB"