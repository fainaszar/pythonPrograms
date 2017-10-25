List1 = [x**2 for x in range(10)]
List2 = [x for x in List1 if x % 2 == 0]


print List1
print List2


#nonprime = [j for i in range(2,8) for j in range(i*2,50,i)]
#primes = [x for x in range(2,50) if x not in nonprime]

#print nonprime
#print primes
Vowels = "AaEeIiOoUu"
List3 = [x for x in raw_input("Enter a word ") if x in Vowels]
print List3

matrix =[range(0,5),range(5,10),range(10,15)]

print  [x for row in matrix for x in row]


prime = [x for x in range(2,int(raw_input("Enter Limit: "))) if all(x%y!=0 for y in range(2,x))] #printing prime numbers
print str(prime) 


N = int(raw_input())
nList = [x for x in raw_input().split()]

print all([int(i)>0 for i in nList]) and any([j == j[::-1] for j in nList])









