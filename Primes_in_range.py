import math
def prime(n):
    a=int(math.sqrt(n))
    if n==1:
        return False
    for i in range(2,a+1):
        if n%i ==0:
            return False
    return True
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    if prime(i)==True:
        l.append(i)
print(len(l))
        
    