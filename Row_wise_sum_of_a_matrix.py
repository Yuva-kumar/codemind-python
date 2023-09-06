n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
l=[]
for i in arr:
    l.append(sum(i))
print(*l)