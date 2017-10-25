

#S = input()


#print(*(sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    a=0
    b=1
    sum=0
    fList=[]
    fList.append(a)
    fList.append(b)
    for i in range(n-2):
        sum = a+b
        fList.append(sum)
        a=b
        b=sum
        
    return fList




if __name__ == '__main__':
    n = int(input())
    fib = fibonacci(n)
    fibcube = list(map(cube, fibonacci(n)))

    