n=int(input())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(arr[i]+arr1[i])
print(*l)