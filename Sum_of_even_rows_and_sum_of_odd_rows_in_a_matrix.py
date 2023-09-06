n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
c=0
d=0
for i in arr:
    if (arr.index(i))%2==0:
        c+=sum(i)
    else:
        d+=sum(i)
print(c,d)

    