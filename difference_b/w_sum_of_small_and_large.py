n=input().split()
l=[]
l1=[]
for i in n:
    a=min(i)
    b=max(i)
    c=ord(a)
    d=ord(b)
    l.append(c)
    l1.append(d)

e=sum(l)
f=sum(l1)
print(f-e)