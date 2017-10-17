import string
alpha = string.ascii_lowercase


n = int(raw_input())
L= []

for i in range(n):
	s = "-".join(alpha[i:n])
	

	L.append((s[::-1]+s[1:]).center(4*n-3, "-"))

print('\n'.join(L[:0:-1]+L))

string = "Hello world"
print string.capitalize()