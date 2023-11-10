n=int(input())
arr=list(map(int,input().split()))
c=0
l=[]
for i in range(len(arr)):
    if arr[i]==1:
        c+=1
    else:
        c=0
    l.append(c)
print(max(l))
