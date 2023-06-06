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
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if prime(i):
        l.append(i)
a=min(lst)
b=max(lst)
c=lst.index(a)
d=lst.index(b)
if c<d:
    k=lst[c:d+1]
    c=0
    for i in l:
        if i in k:
            c+=1
    print(c)
else:
    k=lst[d:c+1]
    c=0
    for i in l:
        if i in k:
            c+=1
    print(c)
        
