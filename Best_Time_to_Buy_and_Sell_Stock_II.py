n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        c+=abs(arr[i]-arr[i+1])
print(c)