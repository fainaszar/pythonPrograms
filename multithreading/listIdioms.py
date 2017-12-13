
a_list = ['a','b','c','d','e']
print(a_list)


(first,second,*rest) = a_list
print(first)
print(second)
print(rest)


(first,*middle,last) = a_list
print(first)
print(middle)
print(last)


(*head,penultimate,last) = a_list
print(head)
print(penultimate)
print(last)