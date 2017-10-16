commandLength = int(raw_input())

list=[]

for i in range(commandLength):
	command = raw_input().split()

	print command[0]
	if command[0] == "insert":
		pos,ele = int(command[1]),int(command[2])
		list.insert(pos,ele)

	elif command[0] == "remove":
		ele = int(command[1])
		
		list.remove(ele)

	elif command[0] == "append":
		ele = int(command[1])
		list.append(ele)
	elif command[0] == "sort":
		list.sort()
	elif command[0] == "reverse":
		list.reverse()
	elif command[0] == "print":
		print list
	elif command[0] == "pop":
		list.pop()


print list
