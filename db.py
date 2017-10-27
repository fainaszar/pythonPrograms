import sqlite3

conn = sqlite3.connect('users.db')

print "Database created/opened successfully ",conn

#conn.execute(''' CREATE TABLE USER
#			(UNAME VARCHAR(50) PRIMARY KEY NOT NULL,
#			NAME	TEXT	NOT NULL,
#			ROLE    TEXT 	NOT NULL);''')


#print "Table created successfully"

#conn.execute("INSERT INTO USER VALUES ('FNZ','Faizan Naseer','Administrator')");

#conn.execute("INSERT INTO USER VALUES ('FAW','Faisal Afzal','Administrator')");

#conn.execute("INSERT INTO USER VALUES ('MA','Muneer Ashraf','Administrator')");

#conn.execute("INSERT INTO USER VALUES ('ABC','Any User','User')");

#conn.execute("INSERT INTO USER VALUES ('XYZ','Other User','User')");

#conn.commit()
#print "Records created successfully"


cursor = conn.execute("SELECT * FROM USER")

print ("USERNAME\tNAME\tROLE")

for row in cursor:
	print "%s\t%s\t%s" % (row[0],row[1],row[2])



print "Administrators List"
cursor = conn.execute("SELECT * FROM USER WHERE ROLE='Administrator'")

print ("USERNAME\tNAME\tROLE")

for row in cursor:
	print "%s\t%s\t%s" % (row[0],row[1],row[2])

print "USERS List"
cursor = conn.execute("SELECT * FROM USER WHERE ROLE='User'")

print ("USERNAME\tNAME\tROLE")

for row in cursor:
	print "%s\t%s\t%s" % (row[0],row[1],row[2])

conn.close() 