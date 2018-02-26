import pymongo
import math
import sys
from datetime import datetime


def calc_student_id(school_number,student_number):
	sum = 0
	for x in range(1000):
		sum += x*x

	return str(school_number) + str(student_number) + str(sum)


school_number = int(sys.argv[1])
print datetime.now() , "STARTED PROCESSING SCHOOL {}".format(school_number).center(80,"-")

students = ["Students" + str(school_number)]
school = None
for s in schools:
	if s["school_number"] == school_number:
		school = s


		student_number = school["first_student"]
		school_number = school["school_number"]
		no_students = school["no_students"]

		documents = []

		student_index=1

		while(student_index < no_students) is True:
			student_id = calc_student_id(school_number,student_number)
			document = {
				"number":student_number,
				"name":"Student" + str(student_number),
				"school_number":school_number,
				"student_index":student_index,
				"student_id":student_id,
			}
			documents.append(document)


			remainder = no_students - student_index

			if (len(documents) % 10000 == 0):
				students.append(documents)
				documents = []

			else:
				if(remainder < 10000 and len(documents) % 1000 == 0):
					students.append(documents)
					documents = []

				else:
					if(remainder<1000 and len(documents)%100 == 0):
						students.append(documents)
						documents = []
					else:
						if(remainder < 100 and len(documents)%10 == 0):
							students.append(documents)
							documents = []
						else:
							if (remainder<10):
								students.append(documents)
								documents=[]
				student_number += 1
				student_index += 1
