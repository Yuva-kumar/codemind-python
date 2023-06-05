n=input()
a=n.split()
l=[]
for i in a:
    l.append(i[::-1])
x=l[::-1]
print(*x)