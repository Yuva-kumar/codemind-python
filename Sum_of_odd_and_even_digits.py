n=int(input())
arr=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==0:
        c+=arr[i]
    else:
        d+=arr[i]
if c-d==0:
    print('YES')
else:
    print('NO')