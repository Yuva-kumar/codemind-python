n=int(input())
arr=list(map(int,input().split()))
s={}
for i in arr:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[]
l1=[]
for i in s:
    l.append(i)
for i in s.values():
    l1.append(i)
l2=[]
for i in range(len(l)):
    l2.append(l[i])
    l2.append(l1[i])
print(*l2)