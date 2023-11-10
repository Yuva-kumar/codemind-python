n=int(input())
arr=list(map(int,input().split()))
l=[]
c=1
for i in range(len(arr)):
    a=arr[c:]
    if len(a)!=0:
        l.append(max(a))
    c+=1
l.append(-1)
print(*l)