def prime(n):
    a=int(n**0.5)
    if n<2:
        return False
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(1,n+1):
    if prime(i):
        if n%i==0:
            l.append(i)
if len(l)==2:
    print(*l)
else:
    print(-1)

