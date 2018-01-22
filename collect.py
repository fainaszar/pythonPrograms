import collections

#DeQueues
print("DeQueues".center(100,"*"))
numbers = [n for n in range(1,21) if n %2 == 0]
dq = collections.deque(numbers)

print (dq)

dq.append(22)

print("DeQueue after appending is  {}".format(dq))

dq.appendleft(0)

print("DeQueue after appending left is {}".format(dq))

dq.pop()

print("DeQueue after pop is {}".format(dq))

dq.popleft()

print("DeQueue after popleft is {}".format(dq))



#print("Index of 18 in DeQueue is {}".format(dq.index(18)))  Not Working

#print dq.insert(0,0) Not Working

dq.remove(20)
print(dq)

dq.extend([n for n in range(20,30) if n%2 == 0])
print("DeQueue after extending is {}\n".format(dq))

dq.extendleft([n for n in range(30,41) if n%2==0])

print("DeQueue after extendleft is \n{}".format(dq))

dq.rotate(-6)
print("DeQueue after rotation of -6 is \n{}".format(dq))

dq.reverse()

print("DeQueue after reverse is \n{}".format(dq))

print("*"*100)


print("Named Tuples".center(100,"*"))


Student = collections.namedtuple('Student',['name','course'])

S1 = Student('Faizan','MCA')
S2 = Student('Muneer','BTech CSE')



print (S1)
print (getattr(S2,'course'))

li = ['Faisal','BTech CSE']
print (Student._make(li))

di = {'name':'Umar','course':'MCA'}
print(Student(**di))

print(S1._asdict())



print("Fields of Students include : {}".format(S1._fields))

print("*"*100)



print("Heaps".center(100,"*"))
import heapq

heapq.heapify(numbers)
print("The created heap is {}".format(list(numbers)))
heapq.heappush(numbers,22)
print(list(numbers))
heapq.heappop(numbers)
#print(heapq.heappop(numbers))


