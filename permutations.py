from itertools import permutations
string , no = raw_input().split()
output = list(permutations(string,int(no)))
output.sort()

for item in output:
    x = len(item)
    print "%c"* x % (item)
