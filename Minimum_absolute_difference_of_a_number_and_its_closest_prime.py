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
l2=[]
for i in range(0,(n+100)):
    if prime(i):
        l.append(i)
for i in l:
    if i>n:
        l1.append(i)
    else:
        l2.append(i)
a=l1[0]
b=l2[-1]
c=abs(n-a)
d=abs(n-b)
if c>d:
    print(abs(b-n))
elif c==d:
    print(abs(b-n))
else:
    print(abs(a-n))

    
