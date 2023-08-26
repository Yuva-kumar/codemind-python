import math
def prime(n):
    a=int(math.sqrt(n))
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
def pal(n):
    a=str(n)
    b=int(a[::-1])
    if n!=b:
        return False
    else:
        return True
l=[]    
n=int(input())
for i in range((n+1),(n*150)):
    if prime(i) and pal(i):
        l.append(i)
print(l[0])
        