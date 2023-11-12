a,k=map(int,input().split())
arr=list(map(int,input().split()))
x=arr[:k]
y=arr[k:]
print(*(y+x))