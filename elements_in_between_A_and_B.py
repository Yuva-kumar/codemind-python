l=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
for i in arr:
    if n==i or n<i and(i==m or i<m):
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print(-1)