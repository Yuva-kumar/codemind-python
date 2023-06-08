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
m=int(input())
x=n+m
l=[]
for i in range(0,(x+100)):
    if prime(i):
        l.append(i)
l1=[]
for i in l:
    l1.append(i-x)
l2=[]
l3=[]
for i in l1:
    if i<=0:
        l2.append(i)
for i in l1:
    if i not in l2:
        l3.append(i)
print(min(l3))