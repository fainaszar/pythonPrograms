from itertools import combinations
no_of_letters = int(input())
letters = input().split()
indices = int(input())




list = list(combinations(letters,indices))



count = 0



for i in range(0,len(list)):
	
	if 'a' in list[i]:
		count+=1

prob = count/len(list)
print (prob)