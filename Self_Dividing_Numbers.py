def self(n):
    l=[]
    l1=[]
    tmp=n
    while n:
        r=n%10
        n=n//10
        l.append(r)
    a=len(l)
    for i in l:
        if i==0:
            return False
        elif tmp%i==0:
            l1.append(i)
    b=len(l1)
    if a!=b:
        return False
    else:
        return True
n=int(input())
m=int(input())
l1=[]
for i in range(n,m+1):
    if self(i):
        l1.append(i)
print(*l1)       