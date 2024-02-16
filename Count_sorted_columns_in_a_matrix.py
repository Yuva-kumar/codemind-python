a,b=map(int,input().split())
l=[list(map(int,input().split())) for i in range(a)]
l1=[]
for i in range(b):
    l2=[]
    for j in l:
        l2.append(j[i])
    l1.append(l2)
c=0
for i in l1:
    k=[j for j in i]
    k.sort()
    if (k==i) or (i==k[::-1]):
        c+=1
print(c)