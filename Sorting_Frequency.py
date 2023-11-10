n=int(input())
l=list(map(int,input().split()))
l.sort()
s={}
for i in l:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l1=[]
for i in s:
    l1.append(s[i])
l1.sort()
l1=l1[::-1]
a=0
l2=[]
for i in range(len(s)):
    for j in s:
        if s[j]==l1[a]:
            l2.append(j)
    a+=1
l3=[]
for i in l2:
    if i not in l3:
        l3.append(i)
print(*l3)