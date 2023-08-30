n=input().split()
a="aeiou"
l=[]
d=0
for i in n:
    l1=[]
    for j in i:
        if j in a:
            l1.append(j)
    l.append(len(l1))
c=min(l)
s={}
for i in l:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
for i in s:
    if i==c:
        print(s[i])
        break