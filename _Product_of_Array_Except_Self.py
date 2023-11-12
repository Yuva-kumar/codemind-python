n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    c=1
    for j in arr:
        if arr[i]!=j:
            c*=j
    else:
        pass
    l.append(c)
print(*l)
            