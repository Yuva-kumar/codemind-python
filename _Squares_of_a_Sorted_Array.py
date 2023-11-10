n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    l.append(abs(i))
l.sort()
l1=[]
for i in l:
    l1.append(i**2)
print(*l1)
