a,b=map(int,input().split())
mat=[list(map(int,input().split()))for i in range(a)]
l=[]
for i in range(b):
    l1=[]
    for j in range(a):
        l1.append(mat[j][i])
    l.append(l1)
l2=[]
for i in l:
    l2.append(sum(i))
print(max(l2))