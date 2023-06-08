import math
def prime(n):
    a=int(math.sqrt(n))
    if n<=1:
        return False
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
l1=[]
for i in range(2,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if prime(i):
        l1.append(i)
if len(l1)==2:
    print(*l1)
else:
    print(-1)