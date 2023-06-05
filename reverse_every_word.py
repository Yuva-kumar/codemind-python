n=input()
a=n.split()
l=[]
for i in a:
    l.append(i[::-1])
print(*l)
    