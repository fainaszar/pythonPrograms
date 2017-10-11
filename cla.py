from sys import argv


argList = []

for arg in argv:
	argList.append(arg)


print "Arguments passed  to  program %r are: " % argList[0]

argList.pop(0)
for item in argList:
	print item
