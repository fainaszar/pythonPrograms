import MySQLdb as mdb
import sys ,json
import xmltodict
import mysql.connector

with open('try.xml' ,"rb") as file:
	data = xmltodict.parse(file)


#print data
output = json.dumps(data)






conn = mysql.connector.connect(user="root",password="Password1",database="pubmedData")

cur = conn.cursor()



insert = "INSERT INTO data (item) VALUES (%s)"
cur.execute(insert,(json.dumps(data),))
conn.commit()

print "Data Written"

conn.close()
# try:
# 	con = mdb.connect('localhost','root','Password1','pubmedData');

# 	cur = con.cursor()
# 	cur.execute("SELECT VERSION()")

# 	ver = cur.fetchone()

# 	print "Database Version : %s " % ver



# 	with con:
# 		cur.execute("DROP TABLE IF EXISTS Articles")
# 		cur.execute("CREATE TABLE Article(PMID INT PRIMARY KEY, DateCreated DATE ,DateCompleted DATE ,DateRevised DATE , \
# 					 ISSN INT,JournalIssue VARCHAR(500),PubDate DATE,ArticleTitle VARCHAR(500),AuthorList VARCHAR(900), \
# 					 Language VARCHAR(30),NlmUniqueID INT , ChemicalList VARCHAR(900),ArticleId INT)")


# 		print "Table created"
# except mdb.Error,e:
# 	print "Error %d: %s" % (e.args[0],e.args[1])
# 	sys.exit(1)

# finally:

# 	if con:
# 		con.close()
