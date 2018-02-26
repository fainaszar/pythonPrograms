import pymongo
import subprocess
import math
from random import randint
from multiprocessing import Pool
from datetime import datetime

start = datetime.now()

print start.time(), "STARTED PROCESSING".center(80,"-")

connection = pymongo.MongoClient("localhost",27017)
db = connection.multiprocessing
schools = db.schools


def uploadSchool(school_number):
	document = {
		'school_number' : school_number,
		'name': 'School ' + str(school_number),
		'no_students' : randint(5000,10000),
		'first_student': school_number

	}
	schools.insert(document)
	print(schools)



if __name__ == '__main__':
	p = Pool()

	result = p.map(uploadSchool,range(1,200001))
	p.close()
	p.join()


print schools

end = datetime.now()
print end.time() , "ENDED PROCESSING".center(80,"-")
print  "Completed in {} seconds".format((end-start).total_seconds())