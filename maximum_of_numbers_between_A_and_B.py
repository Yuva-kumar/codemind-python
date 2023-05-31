l=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
for i in arr:
    if n==i or n<i and(i==m or i<m):
        l.append(i)
a=len(l)
if a!=0:
    print(max(l))
else:
    print(-1)