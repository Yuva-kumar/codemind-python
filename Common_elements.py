n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
l=[]
l1=[]
for i in arr:
    if i in arr1:
        l.append(i)
for i in arr1:
    if i  in arr:
        l.append(i)
for i in l:
    if i not in l1:
        l1.append(i)
print(*l1)
