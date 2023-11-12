n=int(input())
arr=list(map(int,input().split()))
k=int(input())
l=[]
for i in range(n):
    if arr[i]==k:
        l.append(i)
if len(l)==0:
    print(-1,-1)
else:
    print(min(l),max(l))