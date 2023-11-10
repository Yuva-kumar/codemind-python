n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    c=0
    for j in range(0,len(arr)):
        if arr[i]>arr[j]:
            c+=1
    l.append(c)
print(*l)
            
        