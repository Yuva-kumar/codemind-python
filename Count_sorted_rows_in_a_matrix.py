a,b=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(a)]
c=0
for i in arr:
    l=[j for j in i]
    l.sort()
    if (i==l)or(i==l[::-1]):
        c+=1
print(c)