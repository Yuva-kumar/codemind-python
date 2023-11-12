n=int(input())
arr=list(map(int,input().split()))
k=int(input())
a=arr[:k]
b=arr[k:]
l=[]
for i in range(n//2):
    l.append(a[i])
    l.append(b[i])
print(*l)