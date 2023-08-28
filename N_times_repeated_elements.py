n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s={}
for i in arr:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[]
for i in s:
    if s[i]==k:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*l)