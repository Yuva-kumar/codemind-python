import math
def prime(n):
    a=int(math.sqrt(n))
    if n==1:
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
c=sum(l)
d=len(l)
k=c/d
print("{:.2f}".format(k))