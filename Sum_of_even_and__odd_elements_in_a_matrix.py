n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
c=0
d=0
for i in arr:
    for j in i:
        if j%2==0:
            c+=j
        else:
            d+=j
print(c,d)