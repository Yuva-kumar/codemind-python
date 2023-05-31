l=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
k=sum(arr)
c=0
for i in arr:
    if n>i or i>m:
        c+=i
print(k-c)