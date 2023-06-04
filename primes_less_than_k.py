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
m=int(input())
l=[]
for i in lst:
    if prime(i):
        l.append(i)
l1=[]
for i in range(0,m+1):
    if i in l:
        l1.append(i)
print(len(l1))
        
