n=int(input())
arr=list(map(int,input().split()))
s={}
for i in arr:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[]
for i in s:
    l.append(i)
l1=[]
for i in s.values() :
    l1.append(i)
l2=[]
for i in range(0,len(l)):
    if l[i]==l1[i]:
        l2.append(l[i])
if len(l2)==0:
    print(-1)
else:
    print(*l2)