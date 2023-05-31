l=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
a=min(arr)
for i in arr:
    if n>i or i>m:
        l.append(i)
a=len(l)
if a!=0:
    print(min(l))
else:
    print(-1)