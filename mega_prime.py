import math
def prime(n):
    a=int(math.sqrt(n))
    if n<=1:
        return False
    for i in range(2,a+1):
        if n%i ==0:
            return False
    return True
n=int(input())
l=[]
if prime(n):
    while n:
        r=n%10
        n=n//10
        l.append(r)
    x=len(l)
    l1=[]
    for i in l:
        if prime(i):
            l1.append(i)
    k=len(l1)
    if x==k:
        print("Mega Prime")
    else:
        print("Not Mega Prime")      
else:
    print("Not Mega Prime")