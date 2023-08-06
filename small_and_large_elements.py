n=input().split()
a=n[0]
b=n[-1]
l=[]
l1=[]
l2=[]
for i in a:
    l.append(ord(i))
c=chr(min(l))
l2.append(c)
for i in b:
    l1.append(ord(i))
d=chr(max(l1))
l2.append(d)
print(*l2)
    
