n=int(input())
arr=list(map(int,input().split()))
k=int(input())
a=max(arr)
l=[]
for i in arr:
    l.append(i+k)
l1=[]
for i in l:
    if i>=a:
        l1.append('True')
    else:
        l1.append('False')
print(*l1)