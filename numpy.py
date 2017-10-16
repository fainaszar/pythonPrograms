import numpy
ar = []
ar2=[]
r,c = raw_input().split()

for i in range(int(r)):
    lst = raw_input().split()
    
    
    ar.append(map(int,lst))
    
    
array = numpy.array(ar)
result = numpy.min(array,axis=1)
print numpy.max(result)
        
print numpy.mean(array,axis=1)
print numpy.var(array,axis=0)
print numpy.std(array)

d= int(raw_input())

for i in range(d):
    lst = raw_input().split()
    
    
    ar.append(map(int,lst))
for i in range(d):
    lst = raw_input().split()
    
    
    ar2.append(map(int,lst))
    

array1 = numpy.array(ar)
array2 = numpy.array(ar2)

result = numpy.dot(array1,array2)  #performs dot product // matrix multiplication in case of 2D arrays.
print result



coeffs = raw_input().split()
value = int(raw_input())

print numpy.polyval(map(float,coeffs),value)