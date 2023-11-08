n=int(input())
arr=list(map(int,input().split()))
c=[]
for i in arr:
    if arr.count(i)==1:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)