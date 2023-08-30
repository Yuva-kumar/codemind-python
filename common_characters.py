a=input().lower()
b=input().lower()
c="abcdefghijklmnopqrstuvwxyz"
l=[]
for i in a:
    if i in b and i in c:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    l1.sort()
    s=''
    for i in l1:
        s+=i
    print(s)
        