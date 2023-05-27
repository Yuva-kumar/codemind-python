n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
lst=[]
for j in mat:
    for k in j:
        lst.append(k)
print(sum(lst))
