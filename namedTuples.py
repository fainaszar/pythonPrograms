from collections import namedtuple

Student = namedtuple('Student','Name Coarse Roll')
SList = []

n = int(raw_input("Enter no of students: "))

for i in range(n):
	name , coarse , roll = raw_input("Enter details>>").split()

	obj = Student(Name = name , Coarse = coarse , Roll = int(roll))
	SList.append(obj)


for student in SList:
	print student.Name


