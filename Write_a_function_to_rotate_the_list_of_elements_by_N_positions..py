k=int(input())
arr=list(map(int,input().split()))
n=int(input())
a=n%len(arr)
l=arr[:len(arr)-a]
l1=arr[len(arr)-a:]
print(*(l1+l))
