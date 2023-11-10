n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr1=list(map(int,input().split()))
l=[]
for i in  range(len(arr1)):
    l.insert(arr1[i],arr[i])
print(*l)