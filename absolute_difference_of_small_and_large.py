n=input().split()
l=[]
for i in n:
    a=min(i)
    b=max(i)
    c=ord(a)
    d=ord(b)
    l.append(d-c)
print(*l)