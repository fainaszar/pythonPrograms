
list = [1,2,3]
list2 = [4,5,6]

#list operations

list.append(list2)
print list

list3 = [7,8,9]

list2.extend(list3)

print list2

list2.reverse()

print list2


print list2[3:6]

list4 = [11] * 5

print list4

list5 = list2 + [10,11,12]

print list5

print 3 in list5


print "The length of list5 is %r" % len(list5)


list6 = list5
cmpCode = cmp(list3,list5)

print "List 3 and List 6 comparison code is: %r" %cmpCode

if cmpCode == 0:
    print "Lists are equal"
else:
    print "Lists are not equal"

print "The max element of list5 is %r" % max(list5)
print "The min element of list5 is %r" % min(list5)

print list5
print list5.count(10)

print list5.index(6)
print list5
print "Poppin %r from list" % list5.pop(4) #Pops element at position provided
print list5

list5.sort()
print list5s
