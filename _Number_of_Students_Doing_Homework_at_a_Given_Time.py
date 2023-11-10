n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr1=list(map(int,input().split()))
k=int(input())
c=0
for  i in range(n):
    for j in range(arr[i],arr1[i]+1):
        if j==k:
            c+=1
print(c)
