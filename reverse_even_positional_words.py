n=input().split()
l=[]
for i in n:
    l.append(i)
l1=[]
for i in l:
    if (l.index(i))%2==0:
        l1.append(i[::-1])
    else:
        l1.append(i)
print(*l1)
    