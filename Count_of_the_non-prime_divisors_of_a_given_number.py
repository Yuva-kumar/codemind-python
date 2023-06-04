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
l=[]
l1=[]
l2=[]
for i in range(1,a+1):
    if prime(i)==True:
        l.append(i)
for i in range(1,a+1):
    if a%i==0:
        l1.append(i)
for i in l:
    if i in l1:
        l2.append(i)
print(len(l1)-len(l2))
