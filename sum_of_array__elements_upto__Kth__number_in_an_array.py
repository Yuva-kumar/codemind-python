n=int(input())
arr=list(map(int,input().split()))
m=int(input())
c=0
for i in arr:
    if i<m or i==m:
        c+=i
print(c)