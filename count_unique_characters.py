n=input()
l=[]
a="abcdefghijklmnopqrstuvwxyz"
for i in n:
    if i in a:
        l.append(i)
b=l
d={}
for i in b:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
for i in d:
    if d[i]==1:
        c+=1
print(c)