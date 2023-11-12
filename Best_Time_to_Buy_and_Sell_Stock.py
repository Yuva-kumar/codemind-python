n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        a=arr[i:]
        k=max(a)
        l.append(abs(arr[i]-k))
if len(l)==0:
    print(0)
else:
    print(max(l))