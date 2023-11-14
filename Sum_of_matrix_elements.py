a=int(input())
b=int(input())
mat=[list(map(int,input().split())) for i in range(a)]
c=0
for i in mat:
    c+=sum(i)
print(c)